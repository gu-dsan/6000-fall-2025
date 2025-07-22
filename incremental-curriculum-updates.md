# Incremental Curriculum Updates for 2025
## Data Engineering Course - Week by Week Plan

| Week | Current Topic | Existing Slides | Existing Labs | GitHub Repos | Proposed Changes | Lab Assignment | Homework |
|------|---------------|-----------------|---------------|--------------|------------------|----------------|----------|
| 1 | Course overview, Big Data concepts, The Cloud | [slides/01-slides.qmd](/slides/01-slides.html) | [labs/01-labs.qmd](/labs/01-labs.html) | [fall-2024-lab-01](https://github.com/gu-dsan6000/fall-2024-lab-01), [fall-2024-assignment-01](https://github.com/gu-dsan6000/fall-2024-assignment-01) | **UPDATE**: Add modern data engineering landscape overview, update big data examples with current industry cases | Environment setup (Python 3.12, AWS/Azure accounts, GitHub) | Complete background skills assessment, set up all development tools |
| 2 | Introduction to the cloud | [slides/02-slides.qmd](/slides/02-slides.html) | No dedicated lab | ❌ Missing lab-02 repo | **UPDATE**: Update AWS services to current offerings (Glue, Lake Formation), add multi-cloud concepts, remove outdated examples | AWS account setup, IAM roles, S3 buckets, basic EC2 instances | Deploy simple application on AWS with cost monitoring |
| 3 | Parallelization (multiprocessing, asyncio) | [slides/03-slides.qmd](/slides/03-slides.html) | No dedicated lab | [fall-2024-lab-03](https://github.com/gu-dsan6000/fall-2024-lab-03), [fall-2024-assignment-03](https://github.com/gu-dsan6000/fall-2024-assignment-03) | **KEEP**: Good foundational content, minor updates to Python 3.12 syntax | Multiprocessing vs asyncio performance comparison, Ray basics | Build parallel data processing script comparing different approaches |
| 4 | DuckDB, Polars, and file formats | [slides/04-slides.qmd](/slides/04-slides.html) | No dedicated lab | [fall-2024-lab-04](https://github.com/gu-dsan6000/fall-2024-lab-04), [fall-2024-assignment-04](https://github.com/gu-dsan6000/fall-2024-assignment-04) | **UPDATE**: Expand file formats to include Arrow, add Iceberg introduction, update library versions | DuckDB vs Polars performance benchmarking, file format conversions | Build data transformation pipeline comparing formats and engines |
| 5 | Data Warehouse (Presto, Snowflake, Athena) | No existing slides | No dedicated lab | [fall-2024-lab-05](https://github.com/gu-dsan6000/fall-2024-lab-05) | **UPDATE**: Modernize to include Databricks, BigQuery, add lakehouse concepts | Hands-on with Snowflake/Databricks trial accounts, Athena queries | Design modern data warehouse vs lakehouse comparison |
| 6 | Introduction to Spark, RDDs | [slides/06-slides.qmd](/slides/06-slides.html) | [labs/07-labs.qmd](/labs/07-labs.html) | ❌ Missing lab-06 repo | **MINOR UPDATE**: Streamline RDD content, focus more on DataFrames, update to Spark 3.5 | PySpark installation, basic RDD and DataFrame operations | Build ETL pipeline with PySpark |
| 7 | Spark DataFrames and Spark SQL | No existing slides | No dedicated lab | [fall-2024-lab-07](https://github.com/gu-dsan6000/fall-2024-lab-07) (references fall-2023) | **CONSOLIDATE**: Merge with advanced operations, add performance optimization | Complex Spark SQL queries, Catalyst optimizer exploration | Advanced Spark transformations and optimizations |
| 8 | Spark ML and Streaming | [slides/08-slides.qmd](/slides/08-slides.html) | No dedicated lab | [fall-2024-lab-08](https://github.com/gu-dsan6000/fall-2024-lab-08) | **CONSOLIDATE**: Combine ML and streaming into one session, focus on practical examples | MLlib pipeline + structured streaming lab | End-to-end ML pipeline with real-time inference |
| 9 | **NEW**: Apache Iceberg & Table Formats | **NEW CONTENT** | **NEW LAB** | [fall-2024-lab-09](https://github.com/gu-dsan6000/fall-2024-lab-09) → **REPLACE with Iceberg content** | **ADD**: Deep dive into Iceberg, comparison with Hudi and Delta Lake, hands-on implementation | Set up Iceberg on AWS S3, schema evolution, time travel queries | Migrate existing data warehouse to Iceberg format |
| 10 | **NEW**: Data Pipeline Orchestration | **NEW CONTENT** | **NEW LAB** | [fall-2024-lab-10](https://github.com/gu-dsan6000/fall-2024-lab-10) → **REPLACE with Airflow content** | **ADD**: Apache Airflow fundamentals, DAG design patterns, monitoring and alerting | Install Airflow locally, build multi-stage DAGs, implement data quality checks | Design and implement production data pipeline with error handling |
| 11 | **MODIFIED**: Ray, RAPIDS → Vector Databases & RAG | [slides/13-slides.qmd](/slides/13-slides.html) | No dedicated lab | [fall-2024-lab-11](https://github.com/gu-dsan6000/fall-2024-lab-11), [fall-2024-lab-feature-store-vector-db](https://github.com/gu-dsan6000/fall-2024-lab-feature-store-vector-db) | **REPLACE**: Remove RAPIDS focus, add vector database concepts with Chroma/Weaviate (local deployment) | Set up local Chroma instance, build document ingestion pipeline, implement semantic search | Build RAG system for Reddit data analysis |
| 12 | Data Engineering (general concepts) | No dedicated slides | No dedicated lab | [fall-2024-lab-ray](https://github.com/gu-dsan6000/fall-2024-lab-ray), [fall-2024-lab-dask](https://github.com/gu-dsan6000/fall-2024-lab-dask) → **REFOCUS to modern data stack** | **EXPAND**: Modern data stack overview, data governance, quality monitoring, cost optimization | dbt basics, Great Expectations data quality tests, cost monitoring setup | Implement data governance framework with lineage tracking |
| 13 | Lambda & Docker | [slides/docker/_docker.qmd](/slides/docker/) | [labs/11-labs.qmd](/labs/11-labs.html) | [fall-2024-assignment-06](https://github.com/gu-dsan6000/fall-2024-assignment-06) | **UPDATE**: Add serverless data processing patterns, container orchestration, event-driven architectures | Serverless ETL with AWS Lambda, containerized data apps, Step Functions | Deploy fault-tolerant serverless data processing system |
| 14 | Project presentations | No content needed | No lab needed | [fall-2024-project-team-*](https://github.com/gu-dsan6000?q=fall-2024-project-team) (35+ teams) | **KEEP**: Final project presentations with peer evaluation | Project presentations and demos | Final project submission and documentation |

## Key Changes Summary

### Content Reductions
- **Spark sessions**: Reduced from 5 to 3 sessions (weeks 6-8)
  - Week 6: Spark fundamentals (RDDs + DataFrames)
  - Week 7: Spark SQL + advanced operations 
  - Week 8: Spark ML + Streaming combined
- **RAPIDS removal**: Too specialized and hardware-dependent
- **Excessive MapReduce focus**: Keep concepts, reduce implementation details

### New Content Added
- **Week 9: Apache Iceberg & Table Formats**
  - Hands-on with Iceberg on AWS S3
  - Schema evolution and time travel
  - Comparison with Delta Lake and Hudi
  
- **Week 10: Data Pipeline Orchestration**
  - Apache Airflow fundamentals
  - DAG design patterns
  - Production pipeline monitoring

- **Week 11: Vector Databases & RAG (Limited GenAI Focus)**
  - Local Chroma or Weaviate deployment
  - Document ingestion pipeline
  - Simple RAG implementation for analytics

### Technology Updates
- **Python 3.12** throughout all examples
- **Latest library versions**: Polars 1.x, DuckDB 1.x, PySpark 3.5
- **Modern AWS services**: Glue, Lake Formation, Step Functions
- **Current cloud patterns**: Multi-cloud, serverless, containerization

## Lab Infrastructure Requirements

### Free/Local Options Prioritized
- **Chroma**: Run locally, no API costs
- **Airflow**: Local installation for development
- **Iceberg**: Use with local MinIO or AWS free tier
- **DuckDB**: Completely local, no infrastructure costs

### Cloud Resource Management
- Continued focus on AWS free tier and educational credits
- Cost monitoring labs in multiple sessions
- Shutdown procedures emphasized in every cloud session

## Project Ideas (Simplified)

### Option 1: Reddit Analytics Pipeline
**Scope**: Traditional analytics focused
- Build batch processing pipeline for Reddit data
- Implement data quality monitoring
- Create analytical dashboards
- Focus on scalability and cost optimization

**Technologies**: Airflow, Spark, Iceberg, DuckDB, basic visualization

### Option 2: Reddit Intelligent Search
**Scope**: Limited GenAI integration
- Build semantic search over Reddit discussions
- Implement RAG for question answering
- Include traditional analytics alongside AI features
- Focus on data engineering aspects, not AI research

**Technologies**: Vector database (Chroma), embedding models, Airflow, traditional data pipeline + semantic layer

Both projects use the same Reddit dataset but approach it from different angles - traditional analytics vs intelligent search.