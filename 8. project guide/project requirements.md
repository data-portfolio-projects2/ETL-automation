# Requirements for Automated ETL Process

**Objective:** Automate the ETL process to extract, transform, and load data efficiently, enabling seamless data storage, visualization, and analysis for sales monitoring and advanced insights.

## General Requirements

### Tools & Technologies:

*   **Kaggle:** Data source.
*   **Google Cloud Platform (GCP):** Cloud services for automation and storage.
*   **BigQuery:** Automated data storage and backup.
*   **Docker:** Containerized ETL scripts for consistent execution.
*   **Tableau:** Automated data visualizations and dashboard updates.
*   **Streamlit:** Interactive visualization for advanced analytics and ML results.

### Automation Tools:

*   **Cloud Scheduler:** Automate periodic execution of ETL scripts.
*   **Pub/Sub:** Event-driven triggers for ETL workflows.
*   **Cloud Functions:** Lightweight functions to manage specific tasks.
*   **Cloud Run:** Host and deploy the Streamlit app as a scalable service.

### Skills & Knowledge Needed:

*   Expertise in **Python** for scripting and automation.
*   Proficiency with **GCP services** for automation and scaling.
*   Experience with **Docker** for containerization.
*   Familiarity with **Tableau** and **Streamlit** for visualization.

## Phase 1: Automated ETL for Sales Monitoring

### Data Extraction

*   **Source:** Kaggle datasets.
*   **Automation Steps:**
    *   Use Kaggle API to programmatically fetch datasets.
    *   Store raw data temporarily in GCP Cloud Storage.

### Data Transformation

*   **Requirements:**
    *   Dockerized Python ETL script to handle data preprocessing (missing values, encoding, normalization).
    *   Include error handling and logging for automated monitoring.
    *   Perform in-memory processing for optimized performance.

### Data Loading

*   **Destination:**
    *   Transformed data stored temporarily in GCP.
    *   Automatically back up data to BigQuery.

### Visualization Pipeline

*   **Automation Steps:**
    *   Automate Tableau's connection to BigQuery for real-time updates.
    *   Schedule dashboard updates using Tableau's automation tools or API.

## Phase 2: Automated ETL for Advanced Analytics and ML

### Data Extraction

*   **Source:** Kaggle datasets (same as Phase 1).
*   **Automation Steps:**
    *   Automate data fetching via Kaggle API.

### Data Transformation

*   **Requirements:**
    *   Enhanced ETL script to include advanced feature engineering.
    *   In-memory data processing using parallelization (Dask or PySpark).
    *   Automated error detection and recovery mechanisms.

### Data Loading & Visualization

*   **Automation Steps:**
    *   Store processed data temporarily in GCP.
    *   Deploy Streamlit app via Cloud Run for automated visualization updates.

## Optimization & Automation Requirements

### Scheduling:

*   **Cloud Scheduler** for timed automation (daily, weekly, or on-demand).

### Trigger Mechanisms:

*   **Pub/Sub** to initiate ETL workflows based on events (e.g., new data upload).

### Containerization:

*   Use **Docker** for reproducible and consistent environments.

### Monitoring & Alerts:

*   Use **GCP Monitoring** to track performance and send alerts for failures.

## Deliverables

### Phase 1:

*   Automated ETL pipeline: Kaggle → GCP → BigQuery → Tableau.
*   Real-time Tableau dashboard for sales monitoring.

### Phase 2:

*   Automated ETL pipeline: Kaggle → GCP → Streamlit via Cloud Run.
*   Interactive Streamlit app for advanced analytics and ML insights.
