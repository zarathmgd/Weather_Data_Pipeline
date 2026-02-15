-- 1. Table Dimension : VILLES
CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    country VARCHAR(50),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

-- 2. Table de Faits : MÉTÉO QUOTIDIENNE
CREATE TABLE IF NOT EXISTS weather_daily (
    id SERIAL PRIMARY KEY,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    avg_temp_c DECIMAL(4,1),       -- Température moyenne (°C)
    precipitation_mm DECIMAL(5,1), -- Pluie cumulée (mm)
    max_wind_kmh DECIMAL(5,1),     -- Vent max (km/h)
    
    -- Contrainte importante : On ne veut pas 2 lignes pour la même ville à la même date
    CONSTRAINT unique_city_date UNIQUE (city_id, date)
);

-- 3. Pré-remplissage des villes cibles (Retail Stores)
INSERT INTO cities (name, country, latitude, longitude) VALUES 
('Paris', 'France', 48.8566, 2.3522),
('London', 'UK', 51.5074, -0.1278),
('Berlin', 'Germany', 52.5200, 13.4050),
('Madrid', 'Spain', 40.4168, -3.7038),
('Rome', 'Italy', 41.9028, 12.4964)
ON CONFLICT (name) DO NOTHING;