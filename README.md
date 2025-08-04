# DSAN 6000: Big Data and Cloud Computing - Fall 2025

Georgetown University M.S. Data Science and Analytics Program

## Course Overview

This comprehensive course introduces students to the fundamental concepts and practical applications of big data technologies and cloud computing. Throughout the semester, students will learn cutting-edge technologies including:

- **Apache Spark**: Master distributed computing with RDDs, DataFrames, Spark SQL, and Spark ML
- **Modern Data Warehouses**: Work with cloud-native solutions like Amazon Athena, Presto, and Snowflake
- **Data Pipeline Orchestration**: Build and manage complex workflows using Apache Airflow
- **Modern Data Stack**: Explore DuckDB, Polars, Apache Iceberg, and vector databases for RAG applications
- **Cloud Infrastructure**: Understand serverless computing and container orchestration

The course culminates in a final project where students integrate these technologies to solve real-world big data challenges, demonstrating their ability to design and implement scalable data solutions.

## Course Website Structure

The course website is built using Quarto and organized into the following sections:

- **Schedule**: Weekly topics and session planning
- **Lectures**: Course materials and presentations
- **Labs**: Hands-on exercises and assignments
- **Resources**: Additional learning materials and references

### Building the Website

1. **Set up Python environment**:
   ```bash
   # Install uv if not already installed
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Create Python 3.12 environment
   uv venv --python 3.12
   
   # Activate the environment
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Install dependencies
   uv pip install -r pyproject.toml
   ```

2. **Install Quarto**:
   - Download and install Quarto from: https://quarto.org/docs/get-started/
   - Verify installation: `quarto --version`

3. **Render the website**:
   ```bash
   # Make sure you're in the uv environment
   quarto render
   ```
   
   The website will be generated in the `docs/` folder.

### Deployment

The website is automatically deployed via GitHub Pages from the `main` branch. Any push to `main` will trigger an automatic update of the live website.

## GitHub Repository Structure

This course utilizes three main GitHub repositories:

### 1. Course Website Repository (This Repository)
- Contains all course content, schedules, and materials
- Hosts the Quarto-based course website

### 2. Student Organization Repository
- **URL**: https://github.com/gu-dsan6000
- Houses all student project websites
- Individual student repositories for assignments and projects

### 3. Teaching Materials Repository
- **URL**: https://github.com/bigdatateaching
- Source materials for labs and assignments
- Template code and starter files

## GitHub Classroom

We use GitHub Classroom for assignment distribution and submission:

- **Classroom URL**: https://classroom.github.com/classrooms/34950344-georgetown-university-dsan6000-big-data-and-cloud-computing
- This classroom is linked to the `gu-dsan6000` organization
- Assignments and labs will be distributed through GitHub Classroom invitations
- Each assignment creates a private repository for individual students or teams

## Getting Started

1. Join the GitHub Classroom using the invitation link provided in class
2. Clone this repository to stay updated with course materials
3. Set up your development environment following the instructions above
4. Check the schedule regularly for updates and assignments

## Instructors

- **Amit Arora** - Wednesdays, 9:30 AM - 12:00 PM, Reiss 262
- **Jeff Jacobs** - Tuesdays, 9:30 AM - 12:00 PM, TBD

## Course Duration

August 27, 2025 - December 20, 2025