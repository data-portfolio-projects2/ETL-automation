## Reopening Command Prompt

**Open Command Prompt:**

*   Press **Windows + R** keys to open the Run dialog.
*   Type `cmd` and press **Enter** to open a new Command Prompt window.
*   Alternatively, you can search for "Command Prompt" in the Start menu and open it from there.

## Deploying ETL Script

**Navigate to Your Project Directory:**

*   Use the `cd` command to change the directory to where your ETL scripts and Dockerfile are located. For example:

    ```sh
    cd path\to\your\project\directory
    ```

**Build and Deploy Docker Container:**

*   If you haven't built your Docker container yet, build it using:

    ```sh
    docker build -t etl-pipeline .
    ```
*   To run your Docker container locally for testing:

    ```sh
    docker run etl-pipeline
    ```

**Deploy Cloud Function:**

*   Use the `gcloud` command to deploy your Cloud Function. Ensure you have the Google Cloud SDK installed and configured as per the earlier steps.
*   Deploy the Cloud Function with the appropriate settings. For example:

    ```sh
    gcloud functions deploy process_data \
      --runtime python39 \
      --trigger-http \
      --allow-unauthenticated
    ```

## Additional Commands and Configurations

**Authenticate with Google Cloud (if not already authenticated):**

```sh
gcloud auth login
```

**Set the Default Project (if not set):**

```sh
gcloud config set project your-project-id
```

**Enable Required Services:**

```sh
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable bigquery.googleapis.com
```

## Summary

*   Type `exit` to close the current CMD session.
*   Reopen CMD using **Windows + R -> cmd**.
*   Navigate to your project directory.
*   Build and test your Docker container.
*   Deploy your Cloud Function using `gcloud`.

