import os
import re

# Function to generate title from filename
def generate_title(filename):
    # Remove the extension
    base = os.path.splitext(filename)[0]
    # Remove numbers
    base = re.sub(r'\d+', '', base)
    # Replace dashes and underscores with spaces
    base = base.replace('-', ' ').replace('_', ' ')
    # Convert to title case
    title = base.title()
    return title.strip()

# Function to add frontmatter to a single file
def add_frontmatter(file_path):
    # Extract the filename
    filename = os.path.basename(file_path)

    # Read the original file content with utf-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check if frontmatter with title already exists
    if content.startswith('---') and 'title:' in content.split('---')[1]:
        print(f"Frontmatter with title already exists in {filename}. Skipping.")
        return

    # Generate the title
    title = generate_title(filename)
    # Create the frontmatter content
    frontmatter = f"---\ntitle: {title}\n---\n\n"





    # Write the frontmatter followed by the original content with utf-8 encoding
    with open(file_path, 'w', encoding='utf-8') as file:

        file.write(frontmatter + content)
# Function to process all markdown and mdx files in the directory and its subdirectories
def process_all_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.md') or filename.endswith('.mdx'):
                file_path = os.path.join(root, filename)
                try:
                    add_frontmatter(file_path)
                    print(f"Frontmatter added to {filename} in {root}")
                except UnicodeDecodeError as e:
                    print(f"Failed to process {filename} in {root} due to encoding error: {e}")

# Process all files in the current directory and its subdirectories
if __name__ == "__main__":
    process_all_files(os.getcwd())
