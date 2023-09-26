import os


def write_file_to_readme(readme, file_path, file_name):
    with open(file_path, "r") as f:
        content = f.read()
        readme.write(f"<details><summary>{file_name}</summary>\n\n")
        readme.write("```py\n")
        readme.write(content)
        readme.write("\n```\n")
        readme.write("</details>\n\n")


directory = "./src"
readme_file = "./README.md"

with open(readme_file, "w") as readme:
    with open("./readme/prefix.md", "r") as prefix:
        readme.write(prefix.read())

    for dirpath, dirnames, filenames in os.walk(directory):
        if "pycache" in dirpath:
            continue
        # If we're not in the root directory, write the directory name
        if dirpath != directory:
            dirname = os.path.basename(dirpath)
            readme.write(f"### {dirname}\n")

        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                write_file_to_readme(readme, file_path, filename)
