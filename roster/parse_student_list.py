#!/usr/bin/env python3
"""
Parse student roster from roster.txt file.

The roster.txt file is created by copy-pasting the contents 
from the Photo Roster page on Canvas into a text file.

Each group of 3 lines contains:
- Line 1: Name
- Line 2: Numbered name (duplicate)
- Line 3: Email
"""

import logging
from typing import List, Tuple


# Configure logging with basicConfig
logging.basicConfig(
    level=logging.INFO,  # Set the log level to INFO
    # Define log message format
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)


def _read_file(
    file_path: str,
) -> List[str]:
    """Read file and return lines."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        raise


def _parse_student_groups(
    lines: List[str],
) -> List[Tuple[str, str]]:
    """Parse lines into groups of (name, email)."""
    students = []
    
    # Process in groups of 3
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            name = lines[i]
            # Skip the numbered duplicate name at lines[i+1]
            email = lines[i + 2]
            
            if name and email:  # Ensure both fields are non-empty
                students.append((name, email))
                logging.debug(f"Parsed student: {name} - {email}")
        else:
            logging.warning(f"Incomplete group at line {i+1}")
    
    return students


def _write_csv(
    students: List[Tuple[str, str]],
    output_file: str,
) -> None:
    """Write student data to CSV file."""
    import csv
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Email'])  # Header
            writer.writerows(students)
        logging.info(f"Successfully wrote {len(students)} students to {output_file}")
    except Exception as e:
        logging.error(f"Error writing CSV: {e}")
        raise


def _write_names_csv(
    students: List[Tuple[str, str]],
    output_file: str,
) -> None:
    """Write only student names to CSV file."""
    import csv
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Name'])  # Header
            for name, _ in students:
                writer.writerow([name])
        logging.info(f"Successfully wrote {len(students)} names to {output_file}")
    except Exception as e:
        logging.error(f"Error writing names CSV: {e}")
        raise


def main() -> None:
    """Main function to parse student list."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Parse student roster from Canvas Photo Roster export to CSV",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
How to create roster.txt:
    1. Go to Canvas course page
    2. Navigate to People > Photo Roster
    3. Select all text on the page (Ctrl+A / Cmd+A)
    4. Copy the text (Ctrl+C / Cmd+C)
    5. Paste into a text file and save as roster.txt

Example usage:
    # Basic usage (creates students.csv and names.csv)
    uv run python parse_student_list.py
    
    # With custom input/output files
    uv run python parse_student_list.py --input roster.txt --output students.csv --names-output names.csv
    
    # With debug logging
    uv run python parse_student_list.py --debug
"""
    )
    
    parser.add_argument(
        "--input",
        type=str,
        default="roster.txt",
        help="Input file path from Canvas Photo Roster (default: roster.txt)",
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default="students.csv",
        help="Output CSV file path (default: students.csv)",
    )
    
    parser.add_argument(
        "--names-output",
        type=str,
        default="names.csv",
        help="Output CSV file path for names only (default: names.csv)",
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Read and parse the file
    logging.info(f"Reading from {args.input}")
    lines = _read_file(args.input)
    
    logging.info(f"Total lines read: {len(lines)}")
    
    # Parse student groups
    students = _parse_student_groups(lines)
    logging.info(f"Parsed {len(students)} students")
    
    # Write to CSV files
    _write_csv(students, args.output)
    _write_names_csv(students, args.names_output)
    
    # Display first few entries
    if students:
        print(f"\nFirst 5 students:")
        for i, (name, email) in enumerate(students[:5], 1):
            print(f"{i}. {name} - {email}")
        
        if len(students) > 5:
            print(f"... and {len(students) - 5} more")
        
        print(f"\nFiles created:")
        print(f"  - {args.output} (names and emails)")
        print(f"  - {args.names_output} (names only)")


if __name__ == "__main__":
    main()