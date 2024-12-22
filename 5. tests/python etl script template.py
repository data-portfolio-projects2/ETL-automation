import os
import kaggle
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Set up Kaggle API credentials
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

# Download data from Kaggle
kaggle.api.dataset_download_files('dataset-owner/dataset-name', path='data/', unzip=True)

# Load and preprocess data
data = pd.read_csv('data/dataset.csv')

# Add your preprocessing steps here
# Example preprocessing
data.dropna(inplace=True)

# Set up BigQuery credentials
credentials = service_account.Credentials.from_service_account_info({
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key_id": "your-private-key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "your-service-account-email",
    "client_id": "your-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-email"
})

# Initialize BigQuery client
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define BigQuery table ID
table_id = 'your-project.your_dataset.your_table'

# Upload preprocessed data to BigQuery
job = client.load_table_from_dataframe(data, table_id)
job.result()  # Waits for the job to complete

print("Data loaded to BigQuery successfully.")
