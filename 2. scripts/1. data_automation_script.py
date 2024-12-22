import os
from kaggle.api.kaggle_api_extended import KaggleApi
from google.cloud import bigquery
import time

# Kaggle API setup
os.environ['KAGGLE_CONFIG_DIR'] = 'C:\\Users\\loydt\\Documents\\.kaggle'  # Path to your Kaggle credentials
api = KaggleApi()
api.authenticate()

# Dataset information
dataset_name = 'adarsh0806/influencer-merchandise-sales'  # The dataset you want to download
download_dir = 'C:\\Users\\loydt\\Documents\\kaggle_datasets'  # Temporary storage directory for downloaded files

def download_dataset():
    """Downloads the dataset from Kaggle if not already downloaded."""
    # Create download directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Download the dataset
    print(f"Downloading dataset: {dataset_name}")
    api.dataset_download_files(dataset_name, path=download_dir, unzip=True)
    print("Dataset downloaded successfully!")

def upload_to_bigquery(file_path, project_id, dataset_id, table_id):
    """Uploads the dataset to BigQuery."""
    # Set up BigQuery client
    client = bigquery.Client(project=project_id)

    # Set the destination table in BigQuery
    destination_table = f"{project_id}.{dataset_id}.{table_id}"

    # Load data from local file to BigQuery
    job_config = bigquery.LoadJobConfig(
        autodetect=True,  # Automatically detect schema
        source_format=bigquery.SourceFormat.CSV,  # Assuming the dataset is in CSV format
    )

    with open(file_path, "rb") as source_file:
        load_job = client.load_table_from_file(source_file, destination_table, job_config=job_config)

    load_job.result()  # Wait for the job to complete
    print(f"Dataset uploaded to BigQuery: {destination_table}")

    # Verify if the data was uploaded successfully
    verify_upload_success(client, project_id, dataset_id, table_id)

def verify_upload_success(client, project_id, dataset_id, table_id):
    """Verifies if the dataset was uploaded successfully to BigQuery by checking the row count."""
    # Construct the table reference
    table_ref = bigquery.Client(project=project_id).dataset(dataset_id).table(table_id)

    try:
        # Fetch the table metadata
        table = client.get_table(table_ref)
        print(f"Table {table_id} exists in BigQuery with {table.num_rows} rows.")

        # Check if rows are present in the table
        if table.num_rows > 0:
            print(f"Data successfully uploaded to {table_id}. Total rows: {table.num_rows}")
        else:
            print("The table was created but contains no data. Please check the upload process.")
    except Exception as e:
        print(f"Error verifying table {table_id}: {str(e)}")

def automate_etl():
    """Automates the ETL process by downloading and uploading the dataset at regular intervals."""
    while True:
        # 1. Download the dataset
        download_dataset()
        
        # 2. Get the downloaded file's path (assuming it's CSV)
        downloaded_file = os.path.join('C:\\Users\\loydt\\Documents\\kaggle_datasets', 'merch_sales.csv')  # Adjust this path based on your dataset

        # 3. Upload the dataset to BigQuery
        upload_to_bigquery(downloaded_file, "data-analysis-404209", "sales_data", "influencer_merchandise_sales")  # Replace with your actual BigQuery project and table names
        
        # 4. Sleep for a set interval before checking again (simulate scheduling)
        print("Waiting for the next iteration...")
        time.sleep(7 * 24 * 60 * 60)  # Waits for 1 week before it checks for new data to download and upload again

if __name__ == "__main__":
    automate_etl()
