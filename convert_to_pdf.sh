#!/bin/bash

# This script converts markdown files to PDF using pandoc.

# Define source and destination directories
SOURCE_DIR="Sheet4_Deep_Analysis"
COMP_REPORT="Comprehensive_Sheet4_Analysis_Report.md"
DEST_DIR="Sheet4_PDF_Reports"

# Exit immediately if a command exits with a non-zero status.
set -e

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null
then
    echo "Error: pandoc could not be found."
    echo "Please install pandoc to run this script."
    exit 1
fi

echo "--- Starting Markdown to PDF Conversion (using pdflatex engine) ---"

# Convert the individual deep-dive reports
echo "Processing individual reports in $SOURCE_DIR..."
for md_file in "$SOURCE_DIR"/*.md; do
    if [ -f "$md_file" ]; then
        base_name=$(basename "$md_file" .md)
        pdf_file="$DEST_DIR/${base_name}.pdf"
        echo "Converting: $md_file"
        # Use the default pdflatex engine
        pandoc "$md_file" -o "$pdf_file"
    fi
done
echo "Individual reports converted."

# Convert the comprehensive summary report
if [ -f "$COMP_REPORT" ]; then
    echo "Processing comprehensive report: $COMP_REPORT..."
    comp_base_name=$(basename "$COMP_REPORT" .md)
    comp_pdf_file="$DEST_DIR/${comp_base_name}.pdf"
    echo "Converting: $COMP_REPORT"
    # Use the default pdflatex engine
    pandoc "$COMP_REPORT" -o "$comp_pdf_file"
    echo "Comprehensive report converted."
else
    echo "Warning: Comprehensive report not found at $COMP_REPORT"
fi

echo "--- Conversion Complete ---"
echo "All PDF files have been saved to the '$DEST_DIR' directory."
