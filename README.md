# Global Sales Data Pipeline

## Overview
This project automates the sales data ingestion and reporting process for multiple regions — France, Netherlands, and Portugal — using Google Cloud Platform (GCP) services.
Each regional user uploads their CSV sales files via a web application, which triggers a fully automated pipeline from upload to visualization in Looker.

## Archtecture

<img width="1234" height="568" alt="Screenshot 2025-10-20 195137" src="https://github.com/user-attachments/assets/502302f9-5531-445e-9008-b7128e9341ce" />

## Data Flow

Each country team uploads a sales_data.csv file through a secure web interface in the frontend web application. Once uploaded, the web app sends the file to a Google Cloud Storage bucket, which serves as the raw data zone. When a new file arrives in Cloud Storage, a Cloud Function is automatically triggered. The function reads the CSV file, cleans and validates the data, and then loads it into BigQuery for centralized analytics. BigQuery stores all the processed sales data in a single dataset, and Looker (or Looker Studio) connects directly to BigQuery to generate dashboards and reports showing sales trends, country performance, and product analytics.

