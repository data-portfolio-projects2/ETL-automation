### **Overview**

This document outlines the steps to securely store your Kaggle and Google Cloud credentials as secrets in your GitHub repository. These secrets will be used in the GitHub Actions workflow to authenticate with Kaggle and Google Cloud for your automated ETL process.

#### **1. Add Kaggle Credentials**

To authenticate with Kaggle, you need to add your Kaggle username and API key as secrets in your GitHub repository.

**Steps to Add Kaggle Credentials:**

1. Go to your GitHub repository.

2. Navigate to the Settings tab.

3. In the left sidebar, click `Secrets and variables`, then select Actions.

4. Click on New repository secret to add the following secrets:
   
    ```
    KAGGLE_USERNAME: Enter your Kaggle username as the secret's value.
    KAGGLE_KEY: Enter your Kaggle API key as the secret's value.
    ```

6. Click Add secret after entering each value.

   **Secrets Added:**
   ```
   KAGGLE_USERNAME: Your Kaggle username.
   KAGGLE_KEY: Your Kaggle API key.
   ```
   
#### **2. Add Google Cloud Credentials**

To authenticate with Google Cloud, you will use a service account JSON key. You will add the contents of your Google Cloud service account JSON key file as a secret in GitHub.

**Steps to Add Google Cloud Credentials:**

1. In the Secrets and variables section of your GitHub repository settings, click New repository secret.

2. Enter the following information:
   
    ```
    Name: Enter GOOGLE_CLOUD_KEY as the secret name.
    Secret: Paste the entire contents of your Google Cloud service account JSON key file as the secret's value.
    ```
    
4. Click Add secret.

**Secret Added:**

    GOOGLE_CLOUD_KEY: The content of your Google Cloud service account JSON key file.

**Summary of Secrets Created**

You should now have three repository secrets:

1. KAGGLE_USERNAME: Your Kaggle username.
2. KAGGLE_KEY: Your Kaggle API key.
3. GOOGLE_CLOUD_KEY: The contents of your Google Cloud service account JSON key file.

These secrets will be used in the GitHub Actions workflow to authenticate with Kaggle and Google Cloud.

