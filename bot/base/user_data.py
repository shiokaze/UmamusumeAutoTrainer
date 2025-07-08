import os

base_path = "userdata"
if not os.path.exists(base_path):
    os.makedirs(base_path)

def write_file(filename, content):
    filepath = os.path.dirname(base_path + filename)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open(base_path + filename, 'w', encoding='utf-8') as f:
        f.write(content)
