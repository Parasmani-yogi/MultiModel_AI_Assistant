import os
import uuid

TEMP_DIR = "assets/temp"

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def save_uploaded_file(file):
    ext = file.name.split(".")[-1]
    path = os.path.join(TEMP_DIR, f"{uuid.uuid4()}.{ext}")

    with open(path, "wb") as f:
        f.write(file.getbuffer())

    return path