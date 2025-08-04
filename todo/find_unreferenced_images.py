#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Base directory
base_dir = Path("/home/ubuntu/repos/6000-fall-2025")

# Find all image files
image_files = []
for folder in ['labs', 'slides']:
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']:
        image_files.extend(base_dir.glob(f"{folder}/**/{ext}"))

# Find all qmd and md files
doc_files = list(base_dir.glob("**/*.qmd")) + list(base_dir.glob("**/*.md"))

# Extract image references from documents
referenced_images = set()
patterns = [
    r'!\[.*?\]\(([^)]+\.(?:png|jpg|jpeg))\)',  # Markdown image syntax
    r'<img[^>]+src="([^"]+\.(?:png|jpg|jpeg))"',  # HTML img tags
    r'<img[^>]+src=\'([^\']+\.(?:png|jpg|jpeg))\'',  # HTML img tags with single quotes
    r'(?:labs|slides)/(?:img/)?[^"\'\s]+\.(?:png|jpg|jpeg)',  # Direct references
]

for doc_file in doc_files:
    try:
        content = doc_file.read_text(encoding='utf-8')
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                # Normalize the path
                if match.startswith(('labs/', 'slides/')):
                    referenced_images.add(match)
                elif '/labs/' in match or '/slides/' in match:
                    # Extract the relative path from labs/ or slides/
                    if '/labs/' in match:
                        ref = 'labs/' + match.split('/labs/')[-1]
                    else:
                        ref = 'slides/' + match.split('/slides/')[-1]
                    referenced_images.add(ref)
                elif 'img/' in match:
                    # Handle relative img/ references
                    if str(doc_file).count('/labs/') > 0:
                        referenced_images.add(f"labs/{match}")
                    elif str(doc_file).count('/slides/') > 0:
                        referenced_images.add(f"slides/{match}")
    except Exception as e:
        print(f"Error reading {doc_file}: {e}")

# Convert image files to relative paths
image_paths = []
for img in image_files:
    rel_path = str(img.relative_to(base_dir))
    image_paths.append(rel_path)

# Find unreferenced images
unreferenced = []
for img_path in sorted(image_paths):
    found = False
    # Check if this image is referenced
    img_name = os.path.basename(img_path)
    for ref in referenced_images:
        if img_path in ref or img_name in ref:
            found = True
            break
    if not found:
        unreferenced.append(img_path)

# Write results
with open(base_dir / "todo" / "unreferenced_images.md", "w") as f:
    f.write("# Unreferenced Images\n\n")
    f.write(f"Total images found: {len(image_paths)}\n")
    f.write(f"Referenced images: {len(image_paths) - len(unreferenced)}\n")
    f.write(f"Unreferenced images: {len(unreferenced)}\n\n")
    
    if unreferenced:
        f.write("## List of Unreferenced Images\n\n")
        for img in sorted(unreferenced):
            f.write(f"- {img}\n")
    else:
        f.write("All images appear to be referenced!\n")

print(f"Found {len(unreferenced)} unreferenced images out of {len(image_paths)} total")