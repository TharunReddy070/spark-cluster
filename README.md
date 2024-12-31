# MovieLens Tags Analyzer

This repository contains a Dockerized Apache Spark cluster setup designed to analyze the MovieLens dataset using PySpark. It performs a MapReduce-like operation to group and aggregate movie tags.

---

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Output](#output)
- [License](#license)

---

## Overview

This project uses Apache Spark to process the MovieLens dataset and generate a list of tags associated with each movie. The output is saved as a CSV file for further analysis.

Key Features:
- Dockerized Spark cluster with one master and two workers.
- PySpark program for grouping and concatenating movie tags.
- Output stored in CSV format.

---

## Setup

### Requirements

- Docker and Docker Compose
- MovieLens dataset files (`movies.csv` and `tags.csv`) placed in the `data` directory.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/TharunReddy070/spark-cluster.git
    cd spark-cluster
    ```

# Build the Docker Images and Start the Spark Cluster

To build the Docker images and start the Spark cluster, run the following command:

```bash
docker-compose up --build

## Usage

1. Place the `movies.csv` and `tags.csv` files in the `data` directory.

2. Execute the PySpark program inside the cluster:

   ```bash
   docker exec -it spark-master bash
   spark-submit /data/mapreduce_tags.py

## Files

### Data Files
- `data/movies.csv`: Movie metadata.
- `data/tags.csv`: Tags applied to movies by users.

### Code Files
- `requirements/requirements.txt`: Python dependencies.
- `data/mapreduce_tags.py`: PySpark program for tag aggregation.

### Docker Configurations
- `spark-cluster.Dockerfile`: Dockerfile for Spark cluster nodes.
- `hetzner-base.Dockerfile`: Base Dockerfile for Spark and Hadoop setup.
- `docker-compose.yml`: Docker Compose configuration for setting up the cluster.

### Script
- `entrypoint.sh`: Entry point script for Spark containers.

---

## Output

The output will be a CSV file containing two columns:

- `title`: Movie title.
- `tags`: Comma-separated list of tags associated with the movie.

### Example Output

```csv
title,tags
"Inception","mind-bending,dream,thriller"
"The Dark Knight","batman,hero,action"
