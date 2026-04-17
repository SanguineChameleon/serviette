import os, logging
logger = logging.getLogger("mkdocs")

def on_files(files, config):
    for file in files:
        if file.is_documentation_page():
            name = os.path.basename(file.src_uri).replace(".md", "")
            if name == "index":
                continue
            file.dest_uri = name + "/index.html"
            file.url = name + "/"
    return files