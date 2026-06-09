# **Data Engineering Project**

## **Team Members**

* Hiral Kukadia  
* Aadi Kumbhar  
* Achyut Chaturvedi

## **Overview**

This project implements a complete data engineering pipeline for processing, partitioning, and ingesting a Parquet dataset into DuckDB.

The pipeline performs the following tasks:

1. Data cleaning and preprocessing  
2. Partitioning the dataset by year, month, and day  
3. Ingesting the partitioned data into DuckDB for efficient querying and analysis

## **Dataset**

The project uses the dataset:

```
team2.parquet
```

## **Required Libraries**

Install the required Python libraries before running the project:

```shell
pip install pandas pyarrow numpy duckdb
```

The following modules are also used:

* pathlib  
* sqlite3  
* time  
* warnings

## **Repository Setup**

Clone the repository:

```shell
git clone https://github.com/hiralkukadia/Data-Eng-2.git
cd Data-Eng-2
```

## **Execution Order**

Run the scripts in the following sequence.

### **Step 1: Data Preprocessing**

Run the data preprocessing script. (**team\_2\_preprocessing.ipynb)**

**Purpose:**

* Cleans and transforms the raw dataset  
* Handles preprocessing tasks required for downstream processing

**Output:**

* Cleaned dataset stored as a Parquet file

---

### **Step 2: Data Partitioning**

Run the partitioning script. (**partition-code.py)**

**Purpose:**

* Reads the cleaned Parquet dataset  
* Partitions data by:  
  * Year  
  * Month  
  * Day

**Output:**

* Partitioned directory structure optimized for analytics workloads

---

### **Step 3: DuckDB Ingestion**

Run the DuckDB ingestion script. (**deproject\_team2.py)**

**Purpose:**

* Reads the partitioned dataset  
* Loads data into DuckDB  
* Creates a queryable analytical database

**Output:**

* DuckDB database containing the partitioned data

## **Workflow**

```
team2.parquet
        │
        ▼
Data Preprocessing
        │
        ▼
Cleaned Parquet File
        │
        ▼
Partitioning by Year / Month / Day
        │
        ▼
Partitioned Dataset
        │
        ▼
DuckDB Ingestion
        │
        ▼
DuckDB Database
```

## **Repository Structure**

The repository contains scripts for:

* Data preprocessing  
* Data partitioning  
* DuckDB ingestion

## **Notes**

* Ensure all dependencies are installed before execution.  
* Run each stage only after the previous stage has completed successfully.  
* Verify that the cleaned Parquet file is generated before starting the partitioning process.  
* Verify that partitioned data exists before running the DuckDB ingestion step.  
* The partitioned structure improves query performance and data organization within DuckDB.

## **Technologies Used**

* Python  
* Pandas  
* NumPy  
* PyArrow  
* DuckDB  
* SQLite3  
* Parquet

