import requests
import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "database": "weather_data",
    "user": "admin",
    "password": "adminpassword"
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None

def fetch_weather_data(longitude, latitude):
    URL = f"https://archive-api.open-meteo.com/v1/archive"

    params = {
        "longitude": longitude,
        "latitude": latitude,
        "start_date": "2024-01-01",
        "end_date": "2024-12-31",
        "daily": "temperature_2m_mean,precipitation_sum,wind_speed_10m_max",
    }

    response = requests.get(URL, params=params)

    return response.json()

def main():

    conn = get_db_connection()
    if not conn:
        return
    
    cur = conn.cursor()
    cities_request = "SELECT * FROM cities;"
    weather_request = "INSERT INTO weather_daily (city_id, date, avg_temp_c, precipitation_mm, max_wind_kmh) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (city_id, date) DO NOTHING;"

    cur.execute(cities_request)

    rows = cur.fetchall()

    for city in rows:
        id_city = city[0]
        latitude = city[3]
        longitude = city[4]

        data = fetch_weather_data(longitude, latitude)
        date = data["daily"]["time"]
        temperature = data["daily"]["temperature_2m_mean"]
        precipitation = data["daily"]["precipitation_sum"]
        wind = data["daily"]["wind_speed_10m_max"]
    
        weather_datas = list(zip(date, temperature, precipitation, wind))

        for day_data in weather_datas:
            cur.execute(weather_request, (id_city, day_data[0], day_data[1], day_data[2], day_data[3]))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()