#!/usr/bin/env python3
"""
new-topic.py - Create a new topic from template

Usage:
    python3 new-topic.py <subject> "Topic Name"

Examples:
    python3 new-topic.py Math "Linear Algebra"
    python3 new-topic.py Physics "Quantum Mechanics"

This creates: Math/LinearAlgebra.html with all placeholders ready to fill
"""

import sys
import os
import re
from pathlib import Path


def validate_args():
    """Validate command line arguments."""
    if len(sys.argv) < 3:
        print("Usage: python3 new-topic.py <subject> \"Topic Name\"")
        print()
        print("Subjects: Math, Physics, Chemistry, ComputerScience, ...")
        print()
        print("Examples:")
        print("  python3 new-topic.py Math \"Linear Algebra\"")
        print("  python3 new-topic.py Physics \"Quantum Mechanics\"")
        sys.exit(1)

    subject = sys.argv[1]
    topic_name = " ".join(sys.argv[2:])

    return subject, topic_name


def create_filename(topic_name):
    """Convert topic name to filename and variants."""
    # Convert to CamelCase
    words = topic_name.split()
    filename = "".join(word.capitalize() for word in words)

    # Convert to lowercase
    filename_lower = filename.lower()

    # Convert to URL slug
    url_slug = "_".join(words)

    return filename, filename_lower, url_slug


def check_template_exists():
    """Check if TEMPLATE.html exists in current directory."""
    template_path = Path("TEMPLATE.html")
    if not template_path.exists():
        print("Error: TEMPLATE.html not found!")
        print("  Make sure you're running this from the topics/ directory")
        sys.exit(1)
    return template_path


def create_subject_dir(subject):
    """Create subject directory if it doesn't exist."""
    subject_path = Path(subject)
    if not subject_path.exists():
        print(f"Creating directory: {subject}/")
        subject_path.mkdir(parents=True, exist_ok=True)
    return subject_path


def check_file_exists(output_path):
    """Check if output file already exists."""
    if output_path.exists():
        print(f"Error: {output_path} already exists!")
        sys.exit(1)


def replace_placeholders(content, topic_name, filename_lower, url_slug):
    """Replace all placeholders in template content."""
    replacements = {
        "[TOPIC_TITLE]": topic_name,
        "[TOPIC_NAME]": filename_lower,
        "[TOPIC_URL_SLUG]": url_slug,
        "[TOPIC_KEYWORD]": filename_lower,
    }

    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)

    return content


def create_topic_file(template_path, output_path, content):
    """Create the new topic file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def print_next_steps(output_path, subject, filename):
    """Print instructions for next steps."""
    print()
    print(f"✓ Created: {output_path}")
    print()
    print("Next steps:")
    print(f"1. cd {subject}")
    print(f"2. Open {filename}.html in your editor")
    print("3. Replace [SUBTOPIC_NAME] and [SPECIALIZED_TOPIC] placeholders")
    print("4. Add content in each learning level section")
    print("5. Add Wikipedia and arXiv links in Sources section")
    print("6. Add textbook references")
    print("7. Test in browser (all themes and browsers)")
    print("8. Update ../Topics.md if this is the first topic in this subject")
    print()
    print("See ../COMPONENTS.md for reusable HTML snippets.")
    print(f"See {subject}/index.html for landing page pattern.")


def main():
    """Main function."""
    # Validate arguments
    subject, topic_name = validate_args()

    # Create filename variants
    filename, filename_lower, url_slug = create_filename(topic_name)

    # Check template exists
    template_path = check_template_exists()

    # Create subject directory
    subject_path = create_subject_dir(subject)

    # Define output file path
    output_path = subject_path / f"{filename}.html"

    # Check output file doesn't exist
    check_file_exists(output_path)

    # Read template
    print(f"Creating {output_path} from TEMPLATE.html...")

    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace placeholders
    content = replace_placeholders(content, topic_name, filename_lower, url_slug)

    # Create new topic file
    create_topic_file(template_path, output_path, content)

    # Print success message and next steps
    print_next_steps(output_path, subject, filename)


if __name__ == "__main__":
    main()
