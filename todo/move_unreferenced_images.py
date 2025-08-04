#!/usr/bin/env python3

import os
import shutil
from pathlib import Path

# Base directory
base_dir = Path("/home/ubuntu/repos/6000-fall-2025")
todo_dir = base_dir / "todo"
to_be_deleted_dir = todo_dir / "to-be-deleted"

# Read the unreferenced images list
unreferenced_file = todo_dir / "unreferenced_images.md"
unreferenced_images = []

with open(unreferenced_file, 'r') as f:
    for line in f:
        if line.startswith('- '):
            img_path = line.strip('- \n')
            unreferenced_images.append(img_path)

print(f"Found {len(unreferenced_images)} unreferenced images to move")

# Move each image
moved_count = 0
for img_path in unreferenced_images:
    src_path = base_dir / img_path
    dst_path = to_be_deleted_dir / img_path
    
    if src_path.exists():
        # Create destination directory if it doesn't exist
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Move the file
        shutil.move(str(src_path), str(dst_path))
        moved_count += 1
        print(f"Moved: {img_path}")
    else:
        print(f"Warning: Source file not found: {img_path}")

print(f"\nSuccessfully moved {moved_count} images to {to_be_deleted_dir}")

# Update the unreferenced_images.md file with restore command
restore_command = """

## How to Restore Images

To restore all images back to their original locations, run this command from the repository root:

```bash
cd /home/ubuntu/repos/6000-fall-2025
cp -r todo/to-be-deleted/* .
```

Or to restore a specific folder:
```bash
cp -r todo/to-be-deleted/labs/* labs/
cp -r todo/to-be-deleted/slides/* slides/
```
"""

# Append restore instructions to the file
with open(unreferenced_file, 'a') as f:
    f.write(restore_command)