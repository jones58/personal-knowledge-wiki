import os
import plistlib

def extract_url_from_webloc(file_path):
    """
    Extract the URL from a .webloc file.
    """
    try:
        with open(file_path, 'rb') as file:
            plist = plistlib.load(file)
            return plist.get('URLString', None)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def ingest_webloc_files_to_md(directory, output_md_file, recursive=True):
    """
    Ingest all .webloc files in the specified directory (and optionally subdirectories)
    into a single markdown file as links.
    """
    with open(output_md_file, 'w', encoding='utf-8') as md_file:
        for root, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith('.webloc'):
                    file_path = os.path.join(root, filename)
                    print(f"Processing file: {file_path}")
                    url = extract_url_from_webloc(file_path)
                    if url:
                        link_text = os.path.splitext(filename)[0]
                        md_file.write(f"[{link_text}]({url})\n")
                        print(f"Added link: [{link_text}]({url})")
                    else:
                        print(f"No URL found in {file_path}")
            if not recursive:
                break

if __name__ == "__main__":
    # Use the current working directory as the directory containing .webloc files
    webloc_directory = os.getcwd()
    # Specify the output markdown file
    output_markdown_file = "webloc_links.md"

    # Ingest .webloc files into the markdown file
    ingest_webloc_files_to_md(webloc_directory, output_markdown_file, recursive=True)
