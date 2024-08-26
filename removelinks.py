import os
import re
import argparse

def process_links_files(directory):
    files_processed = 0
    files_modified = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower() == "links.md":
                file_path = os.path.join(root, file)
                modified = process_file(file_path)
                files_processed += 1
                if modified:
                    files_modified += 1

    print(f"\nSummary:")
    print(f"Total files processed: {files_processed}")
    print(f"Files modified: {files_modified}")

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if "# Links:" is present in the content
    if "# Links:" in content:
        # Remove "# Links:" and any whitespace after it
        updated_content = re.sub(r'# Links:\s*', '', content)

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Removed '# Links:' from {file_path}")
        return True
    else:
        print(f"No '# Links:' found in {file_path}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process links.md files and remove '# Links:' occurrences.")
    parser.add_argument("-d", "--directory", default=os.getcwd(), help="The directory to process (default: current directory)")
    args = parser.parse_args()

    print(f"Processing directory: {args.directory}")
    process_links_files(args.directory)
