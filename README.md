# Global Sales Data Pipeline

## Overview
This project automates the sales data ingestion and reporting process for multiple regions — France, Netherlands, and Portugal — using Google Cloud Platform (GCP) services.
Each regional user uploads their CSV sales files via a web application, which triggers a fully automated pipeline from upload to visualization in Looker.

## Archtecture

<img width="1234" height="568" alt="Screenshot 2025-10-20 195137" src="https://github.com/user-attachments/assets/502302f9-5531-445e-9008-b7128e9341ce" />

## Data Flow

User Upload (Frontend Web App):
  “*” Each country team uploads a sales_data.csv file through a secure web interface.

File Storage (Cloud Storage):
  “*” The web app sends the uploaded file to a Google Cloud Storage bucket (raw sales data zone).

Automated Processing (Cloud Functions):
  “*” A Cloud Function is triggered when a new file arrives. It:

    “*” Reads the CSV file from Cloud Storage

    “*” Cleans and validates the data

   “*”  Loads it into BigQuery for centralized analytics

“*” Analytics & Reporting (BigQuery + Looker):

  “*” BigQuery stores all cleaned sales data in one dataset.

  “*” Looker (or Looker Studio) connects to BigQuery for dashboards and reports showing trends, country performance, and product analytics.
