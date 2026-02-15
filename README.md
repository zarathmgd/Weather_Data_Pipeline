# 🌧️ European Weather Data Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Business_Intel-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

> **Business Case:** A retail chain operating in major European capitals needs to optimize its inventory (e.g., umbrellas, winter coats) based on local weather patterns. This project automates the data ingestion to provide actionable logistics insights.

![Dashboard Preview](img/dashboard.png)

## 📋 Table of Contents
- [Architecture](#-architecture)
- [Key Features](#-key-features)
- [Data Model](#-data-model)
- [Prerequisites & Installation](#-prerequisites--installation)
- [Business Insights](#-business-insights)
- [Author](#-author)

## 🏗 Architecture

This project implements a robust **ELT (Extract, Load, Transform)** pipeline.

```mermaid
graph LR
    A[Open-Meteo API] -->|Extract JSON| B(Python ETL Script)
    B -->|Clean & Format| B
    B -->|Upsert Data| C[(PostgreSQL DWH)]
    C -->|DirectQuery| D[Power BI Dashboard]
    subgraph Docker Container
    C
    end
    style C fill:#336791,stroke:#fff,stroke-width:2px,color:#fff
    style D fill:#F2C811,stroke:#333,stroke-width:2px
