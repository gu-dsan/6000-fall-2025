import pandas as pd
from typing import Dict, List, Any


def create_markdown_table(data: Dict[str, List[Any]]) -> str:
    """
    Creates a markdown table from a dictionary of data.
    Similar to R's tribble() function.
    
    Args:
        data: Dictionary where keys are column names and values are lists of data
        
    Returns:
        String containing the markdown table
    """
    df = pd.DataFrame(data)
    return df.to_markdown(index=False)


def create_comparison_table(
    col1_header: str,
    col2_header: str,
    col3_header: str,
    data: List[tuple]
) -> str:
    """
    Creates a comparison table with three columns.
    
    Args:
        col1_header: Header for first column
        col2_header: Header for second column
        col3_header: Header for third column
        data: List of tuples containing (col1_value, col2_value, col3_value)
        
    Returns:
        String containing the markdown table
    """
    df = pd.DataFrame(data, columns=[col1_header, col2_header, col3_header])
    return df.to_markdown(index=False)


def create_two_column_table(
    col1_header: str,
    col2_header: str,
    data: List[tuple]
) -> str:
    """
    Creates a simple two-column table.
    
    Args:
        col1_header: Header for first column
        col2_header: Header for second column
        data: List of tuples containing (col1_value, col2_value)
        
    Returns:
        String containing the markdown table
    """
    df = pd.DataFrame(data, columns=[col1_header, col2_header])
    return df.to_markdown(index=False)