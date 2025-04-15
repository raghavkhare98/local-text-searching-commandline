from pathlib import Path
from config import ENCODING

def read_files(directory, extensions):
    file_contents = {}
    for file in Path(directory).rglob("*"):
        if file.suffix.lower() in extensions:
            content = file.read_text(encoding=ENCODING)
            file_contents[str(file)] = content
    return file_contents

