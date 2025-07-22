# GitHub Repository Analysis - gu-dsan6000 Organization

## Repository Structure Summary

Based on the GitHub CLI analysis of the `gu-dsan6000` organization, here's what I found:

### **Template Repositories (Base/Starter Code)**

These are the main template repositories that students fork from:

#### **Numbered Labs (Traditional Structure)**
- `fall-2024-lab-01` → Basic lab (references fall-2023 content)
- `fall-2024-lab-03` → Lab 3 content  
- `fall-2024-lab-04` → Lab 4 content
- `fall-2024-lab-05` → Lab 5 content  
- `fall-2024-lab-07` → Lab 7 (references fall-2023 lab-07)
- `fall-2024-lab-08` → Lab 8 content
- `fall-2024-lab-09` → Lab 9 content
- `fall-2024-lab-10` → Lab 10 ("fall-2024-lab10")
- `fall-2024-lab-11` → Spark Streaming lab

#### **Named/Specialized Labs**
- `fall-2024-lab-dask` → Dask lab
- `fall-2024-lab-ray` → Ray lab  
- `fall-2024-lab-feature-store-vector-db` → Vector databases & feature store lab
- `lab-vector-db-feature-store` → Base vector DB lab

#### **Assignments**
- `fall-2024-assignment-01` (references fall-2023 content)
- `fall-2024-assignment-03`
- `fall-2024-assignment-04` 
- `fall-2024-assignment-06`

#### **Final Projects**
- Multiple team project repos: `fall-2024-project-team-##`
- Reddit-based big data projects
- 35+ student teams for Fall 2024

### **Key Observations**

#### **Missing Labs/Gaps**
- **Lab 02**: No dedicated lab-02 repository found
- **Lab 06**: No dedicated lab-06 repository found  
- **Lab 12**: No lab-12 repository found
- **Assignment gaps**: Missing assignments 02, 05

#### **Inconsistent Naming Patterns**
- Mix of numbered (lab-01, lab-03) and descriptive names (lab-dask, lab-ray)
- Some labs reference fall-2023 content in fall-2024 repos
- Different naming conventions for GitHub Classroom generated names

#### **Content Areas Covered (Based on Repository Names)**
1. **Basic Setup/Cloud** (lab-01, lab-03, lab-04)
2. **Data Processing** (lab-05, lab-07, lab-08, lab-09)
3. **Distributed Computing** (lab-dask, lab-ray, lab-10, lab-11)
4. **Modern Topics** (lab-feature-store-vector-db)
5. **Final Projects** (Reddit-based analytics)

#### **Detailed Lab Content Analysis**
- **Lab 05 - Data Warehouse**: Based on the syllabus, this lab covers modern data warehousing technologies including:
  - **Amazon Athena**: Serverless interactive query service for S3 data
  - **Presto/Trino**: Distributed SQL query engine
  - **Snowflake**: Cloud-based data warehouse platform
  - Hands-on experience with SQL queries on large datasets
  - Cost optimization and performance tuning techniques

### **Mapping to Course Structure**

Based on our curriculum analysis, here's how the existing repositories likely map:

| Week | Topic | Existing Repository | Status |
|------|-------|-------------------|---------|
| 1 | Course Overview | `fall-2024-lab-01` | ✅ Exists |
| 2 | Cloud Computing | Missing lab-02 | ❌ Gap |
| 3 | Parallelization | `fall-2024-lab-03` | ✅ Exists |
| 4 | DuckDB/Polars | `fall-2024-lab-04` | ✅ Exists |
| 5 | Data Warehouse (Presto, Snowflake, Athena) | `fall-2024-lab-05` | ✅ Exists |
| 6 | Spark Intro | Missing lab-06 | ❌ Gap |
| 7 | Spark DataFrames | `fall-2024-lab-07` | ✅ Exists |
| 8 | Spark ML | `fall-2024-lab-08` | ✅ Exists |
| 9 | Spark NLP | `fall-2024-lab-09` | ✅ Exists |
| 10 | Spark Streaming | `fall-2024-lab-10` | ✅ Exists |
| 11 | Streaming cont. | `fall-2024-lab-11` | ✅ Exists |
| 12 | Ray/RAPIDS | `fall-2024-lab-ray` + `fall-2024-lab-dask` | ✅ Exists |
| 13 | Vector DB | `fall-2024-lab-feature-store-vector-db` | ✅ Exists |

### **Recommendations for 2025 Updates**

#### **Repository Cleanup Needed**
1. **Fill Missing Labs**:
   - Create `fall-2025-lab-02` (Cloud Computing basics)
   - Create `fall-2025-lab-06` (Spark Introduction)

2. **Consolidate/Rename Based on New Curriculum**:
   - `fall-2025-lab-09` → **Apache Iceberg & Table Formats** (NEW)
   - `fall-2025-lab-10` → **Data Pipeline Orchestration (Airflow)** (NEW)
   - `fall-2025-lab-11` → **Vector Databases & Data Ingestion** (UPDATED)
   - Consolidate multiple Spark labs (reduce from 5 to 3)

3. **Standardize Naming Convention**:
   - Use consistent `fall-2025-lab-##` format
   - Descriptive names for specialized content
   - Clear versioning (avoid referencing old years)

#### **New Repositories Needed for 2025**
1. **`fall-2025-lab-iceberg`** - Apache Iceberg hands-on
2. **`fall-2025-lab-airflow`** - Data pipeline orchestration  
3. **`fall-2025-assignment-iceberg`** - Table format migration project
4. **`fall-2025-assignment-pipeline`** - End-to-end data pipeline

#### **Repository Migration Strategy**
1. **Keep Working Content**: Don't break existing labs that work well
2. **Gradual Updates**: Update 2-3 labs per semester
3. **Version Control**: Use clear fall-2025 prefixes
4. **Template Cleanup**: Remove outdated references to fall-2023

### **Student Engagement Analysis**

#### **High Activity Labs** (Many student forks):
- `fall-2024-lab-09` (50+ student submissions) 
- `fall-2024-lab-10` (40+ student submissions)
- `fall-2024-lab-11` (25+ student submissions)
- Vector DB lab (20+ submissions)

#### **Athena/Data Warehouse Lab Activity**:
- `fall-2024-lab-05` shows active student engagement with recent submissions
- Students working with Amazon Athena, Presto, and Snowflake hands-on labs
- Template repository: `dsan-6000-fall-2024-fall-2024-lab-05-fall-2024-lab-05`
- Evidence of ongoing student work through December 2024

#### **Lower Activity Labs**:
- Early numbered labs have fewer submissions
- Suggests either timing issues or content problems

### **Final Project Structure**
- **Current**: Reddit-based big data projects
- **Scale**: 35+ teams in Fall 2024
- **Pattern**: Team-based collaborative projects
- **Technology Stack**: Reddit data, distributed processing

This aligns well with our proposed project options (Reddit Analytics + Reddit Intelligent Search).

## Conclusion

The existing repository structure shows a mature course with comprehensive lab coverage, but there are opportunities for:

1. **Filling gaps** (missing labs 2, 6)
2. **Modernizing content** (Iceberg, Airflow)  
3. **Standardizing naming** (consistent fall-2025 format)
4. **Optimizing structure** (consolidate overlapping Spark content)

The high student engagement (200+ active repositories) indicates a successful course structure that should be evolved incrementally rather than revolutionized.