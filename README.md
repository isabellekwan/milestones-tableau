# Instructions to Merge JSON Files

## Prerequisites

- Python installed on your system ([Download Python](https://www.python.org/downloads/))
- Ensure all JSON files (`allDocuments01.json`, `allDocuments02.json`, etc.) are in the same directory as the Python script.

## Steps to Merge JSON Files

1. **Download the Script**

   Download the `mergeAllJSON.py` script into your working directory.

2. **Run the Script**

   Open a command prompt or terminal:
   
   - Navigate to the directory where `mergeAllJSON.py` is located using the `cd` command.

   - Run the script using Python:
     ```
     python mergeAllJSON.py
     ```

3. **Verify Output**

   - The script will merge all `allDocuments*.json` files into a single JSON file named `combinedAll.json` in the same directory.

   - Check the `combined.json` file to ensure all data attributes are correctly merged and each object contains a `user_id` field.

## Notes

- If you encounter any issues, ensure your JSON files are correctly formatted and contain the expected structure (`'data'` key containing attributes to merge).

- Adjust the script or file paths as necessary based on your specific file naming conventions or directory structure.

- "mergeUserJSON.py" has the same functinoality, but I may edit it in the future

- For troubleshooting or customization, refer to the script comments or consult Python and JSON documentation.
