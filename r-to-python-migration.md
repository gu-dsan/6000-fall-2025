# R to Python Migration Report

## Summary

This repository uses R in specific areas, primarily for:
1. Creating formatted tables in slides using kableExtra
2. Setup chunks in labs for R environment configuration
3. Inline R expressions for dynamic content (timestamps)
4. Example code comparisons between R, Pandas, and PySpark

## R Usage Analysis

### 1. Table Formatting in Slides (High Priority)

**Files affected:**
- `/slides/01-slides.qmd` - Lines 401, 428
- `/slides/02-slides.qmd` - Lines 36, 151  
- `/slides/03-slides.qmd` - Line 45
- `/slides/parallelization-python/spark/_spark.qmd` - Lines 178, 262, 277, 411, 498
- `/slides/06-slides.qmd` - Lines 20, 235, 315
- `/slides/08-slides.qmd` - Line 20
- `/slides/09-slides.qmd` - Line 21
- `/slides/10-slides.qmd` - Line 21

**Current usage:**
R is being executed to create formatted tables using the `kableExtra` package with features like:
- HTML table formatting
- Column specifications (bold, borders)
- Full width control
- Table styling

**Migration approach:**
Replace with Markdown tables or Python-based table generation using:
- Pure Markdown tables for simple cases
- Python with pandas DataFrame.to_markdown() for more complex tables
- Python with tabulate or prettytable libraries for advanced formatting

### 2. Lab Setup Chunks (Low Priority)

**Files affected:**
- `/labs/01-labs.qmd` - Line 10
- `/labs/07-labs.qmd` - Line 17
- `/labs/11-labs.qmd` - Line 9

**Current usage:**
R setup chunks that configure knitr options and load the reticulate package for Python integration.

**Migration approach:**
These can be removed if labs are fully converted to Python. The reticulate package is only needed for R-Python interoperability.

### 3. Example Code for Comparison (No Action Needed)

**Files affected:**
- `/labs/07-labs.qmd` - Lines 113, 130, 150, 183, 203, 220

**Current usage:**
R code blocks with `eval = FALSE` showing R equivalents of Pandas/PySpark operations for educational comparison.

**Migration approach:**
No action needed - these are display-only examples for teaching purposes and are not executed.

### 4. Inline R Expression (High Priority)

**Files affected:**
- `/syllabus.qmd` - Line 34

**Current usage:**
```r
`r strftime(Sys.time(), "%A,  %B %d, %Y at %I:%M %p", tz = "America/New_York")`
```

**Migration approach:**
Replace with Python inline code or use Quarto's built-in date functionality:
```python
from datetime import datetime
import pytz

eastern = pytz.timezone('America/New_York')
current_time = datetime.now(eastern).strftime("%A, %B %d, %Y at %I:%M %p")
```

## Recommended Migration Strategy

### Phase 1: High Priority Items
1. **Convert table generation from R to Markdown/Python**
   - Start with simple tables that can be pure Markdown
   - For complex tables, create a Python utility function that generates Markdown tables
   - Consider using pandas with custom formatting functions

2. **Replace inline R timestamp**
   - Use Python datetime formatting or Quarto's built-in date features

### Phase 2: Low Priority Items
1. **Remove R setup chunks from labs**
   - Only if labs no longer need R-Python interoperability
   - Verify that removing reticulate doesn't break any functionality

### Phase 3: No Action Items
1. **Keep R example code blocks**
   - These serve an educational purpose showing R equivalents
   - They are not executed (eval = FALSE)

## Implementation Notes

### For Table Conversion

Example Python function to replace R table generation:

```python
import pandas as pd

def create_comparison_table(data_dict):
    """
    Creates a markdown table from a dictionary of data
    Similar to R's tribble() function
    """
    df = pd.DataFrame(data_dict)
    return df.to_markdown(index=False)

# Example usage replacing R tribble
data = {
    "": ["Goals", "Location", "Structure/Contents"],
    "Small Data is usually...": [
        "gathered for a specific goal",
        "in one place, and often in a single computer file",
        "highly structured like an Excel spreadsheet"
    ],
    "On the other hand, Big Data...": [
        "may have a goal in mind when it's first started",
        "can be in multiple files in multiple servers",
        "can be unstructured, it can have many formats"
    ]
}
```

### For Inline Date Replacement

In Quarto, you can use:
```yaml
date: today
date-format: "dddd, MMMM D, YYYY 'at' h:mm A"
```

Or use Python inline code with proper Quarto syntax.

## Conclusion

The R usage in this repository is primarily for table formatting and display purposes. Most R code can be easily replaced with Markdown tables or Python equivalents. The educational R examples should be retained as they serve a teaching purpose.