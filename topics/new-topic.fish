#!/usr/bin/env fish
#
# new-topic.fish - Create a new topic from template
# Run from: topics/ directory (same level as this script)
#
# Usage: fish new-topic.fish <subject> "Topic Name"
#
# Example:
#   fish new-topic.fish Math "Linear Algebra"
#   Creates: Math/LinearAlgebra.html with all placeholders ready to fill
#

if test (count $argv) -lt 2
    echo "Usage: fish new-topic.fish <subject> \"Topic Name\""
    echo ""
    echo "Subjects:"
    echo "  Math, Physics, Chemistry, ComputerScience, ..."
    echo ""
    echo "Example:"
    echo "  fish new-topic.fish Math \"Linear Algebra\""
    echo "  fish new-topic.fish Physics \"Quantum Mechanics\""
    echo ""
    echo "This will create Math/LinearAlgebra.html from the template."
    exit 1
end

set subject $argv[1]
set topic_name $argv[2]

# Verify subject directory exists or create it
if not test -d $subject
    echo "Creating directory: $subject/"
    mkdir -p $subject
end

# Convert to filename (remove spaces, capitalize)
set filename (echo $topic_name | tr ' ' '\n' | sed 's/^./\U&/' | tr -d '\n')
set filename_lower (echo $filename | tr '[A-Z]' '[a-z]')
set url_slug (echo $topic_name | tr ' ' '_')

set output_file "$subject/$filename.html"

# Check if file exists
if test -f $output_file
    echo "Error: $output_file already exists!"
    exit 1
end

# Check if template exists
if not test -f TEMPLATE.html
    echo "Error: TEMPLATE.html not found! (must be in topics/ directory)"
    exit 1
end

echo "Creating $output_file from TEMPLATE.html..."

# Create file with placeholders replaced
sed \
    "s/\[TOPIC_TITLE\]/$topic_name/g" \
    "s/\[TOPIC_NAME\]/$filename_lower/g" \
    "s/\[TOPIC_URL_SLUG\]/$url_slug/g" \
    "s/\[TOPIC_KEYWORD\]/$filename_lower/g" \
    TEMPLATE.html > $output_file

echo ""
echo "✓ Created: $output_file"
echo ""
echo "Next steps:"
echo "1. cd $subject && ls"
echo "2. Open $filename.html in your editor"
echo "3. Replace [SUBTOPIC_NAME] and [SPECIALIZED_TOPIC] placeholders"
echo "4. Add content in each learning level section"
echo "5. Add Wikipedia and arXiv links in Sources section"
echo "6. Add textbook references"
echo "7. Test in browser (all themes and browsers)"
echo "8. Update ../Topics.md if this is the first topic in $subject"
echo ""
echo "See ../COMPONENTS.md for reusable HTML snippets."
echo "See $subject/index.html for landing page pattern."
