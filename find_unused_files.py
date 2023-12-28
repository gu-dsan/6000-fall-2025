import os

"""
Bad code with no regards to reusability, just here because I was too tired and decided to scribble this
any way to delete all unusued files which have been inherited..
"""
import glob
from pathlib import Path

png_files = []
for path in Path('.').rglob('*.PNG'):
    print(str(path.resolve()))
    if "_site" not in str(path.resolve()) and ".ppol" not in str(path.resolve()):
        png_files.append(str(path.resolve()))

mkdn_files = []
for path in Path('.').rglob('*.?md'):
    print(str(path.absolute))
    mkdn_files.append(str(path.resolve()))

unused_png_file = []
    
for png_file in png_files:
    found = False
    for md_file in mkdn_files:
        with open(md_file, encoding='utf-8') as f:
            content = f.read()
            if os.path.basename(png_file) in content:
                found = True
        if found is True:
            break
    if found is False:
        unused_png_file.append(png_file)
print(unused_png_file)
print(f"there are {len(unused_png_file)} png files")
print(f"goinf to delete all unused files")
for unsued_file in unused_png_file:
    print(f"going to delete {unsued_file}")
    file_to_rem = Path(unsued_file)
    file_to_rem.unlink()
print("deleted all unsued files")
