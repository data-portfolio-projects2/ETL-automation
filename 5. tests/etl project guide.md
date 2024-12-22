### **ETL Automation Project**

**Objective**

Automate the extraction, transformation, and loading (ETL) process for a dataset from Kaggle to Google BigQuery using GitHub Actions. The process will:

1. Download the dataset from Kaggle.
2. Preprocess the data.
3. Upload the preprocessed data to BigQuery.

**Prerequisites**

1. Kaggle Account: Ensure you have a Kaggle account and API credentials.
2. Google Cloud Account: Ensure you have a Google Cloud account with BigQuery enabled.
3. GitHub Repository: Ensure you have a GitHub repository for your project.
4. GitHub Secrets: Add your Kaggle and Google Cloud credentials as secrets in your GitHub repository.

**Setup GitHub Secrets**

1. Kaggle API Credentials:

    - KAGGLE_USERNAME: Your Kaggle username.
    - KAGGLE_KEY: Your Kaggle API key.

2. Google Cloud Credentials:

    - BIGQUERY_CREDENTIALS: Your Google Cloud service account JSON credentials (encoded as a single line).

**GitHub Actions Workflow**

Create a GitHub Actions workflow file in your repository at .github/workflows/etl.yml:

```yaml
name: ETL Automation

on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 0 * * *' # Runs daily at midnight UTC

jobs:
  etl-job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run ETL script
        env:
          KAGGLE_USERNAME: ${{ secrets.KAGGLE_USERNAME }}
          KAGGLE_KEY: ${{ secrets.KAGGLE_KEY }}
          BIGQUERY_CREDENTIALS: ${{ secrets.BIGQUERY_CREDENTIALS }}
        run: |
          python etl_script.py
```

**Python ETL Script**

Create the ETL script etl_script.py in your repository:

```python
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
```

**Dependencies**

Create a requirements.txt file in your repository to list the required Python packages:

```python
pandas
kaggle
google-cloud-bigquery
google-auth
google-auth-oauthlib
google-auth-httplib2
```
**Running the Workflow**

1. Push the changes to your GitHub repository.
2. The GitHub Actions workflow will trigger automatically based on the specified schedule or on a push to the main branch.
3. The workflow will:
   
      - Check out the repository.
      - Set up the Python environment.
      - Install dependencies.
      - Run the ETL script to download, preprocess, and upload data to BigQuery.

**Conclusion**
This setup allows for automated ETL processes using GitHub Actions. The data is fetched directly from Kaggle, processed within the script, and uploaded to BigQuery without needing to store intermediate files on GitHub.










