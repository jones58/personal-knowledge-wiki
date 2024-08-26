import os
import xml.etree.ElementTree as ET

def extract_url_from_webloc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            root = ET.fromstring(content)
            url = root.find('.//string').text
            return url
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def ingest_webloc_files_to_md(output_md_file):
    with open(output_md_file, 'w', encoding='utf-8') as md_file:
        md_file.write("# Links:\n\n")
        for filename in os.listdir('.'):
            if filename.endswith('.webloc'):
                file_path = os.path.join('.', filename)
                url = extract_url_from_webloc(file_path)
                if url:
                    link_text = os.path.splitext(filename)[0]
                    md_file.write(f"- [{link_text}]({url})\n")
                    print(f"Added link: [{link_text}]({url})")
                    os.remove(file_path)
                    print(f"Deleted file: {filename}")
                else:
                    print(f"No URL found in {filename}")

if __name__ == "__main__":
    output_markdown_file = "links.md"
    ingest_webloc_files_to_md(output_markdown_file)
    print(f"Conversion complete. Output written to {output_markdown_file}")
    print("All .webloc files have been deleted.")
