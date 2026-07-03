import re
import pandas as pd

# 1. SIMULATED TESSERACT OCR OUTPUT
# This raw string simulates the unstructured text extracted by Tesseract OCR from a payment PDF image.
MOCK_OCR_TEXT = """
============================================================
INTERNATIONAL TELEGRAPHIC TRANSFER RECEIPT (DUMMY REPORT)
============================================================
DATE OF TRANSFER: 2026-07-03
SENDER BANK NAME: GLOBAL CLEARING BANK MANILA
SWIFT 8BIC ROUTING: GCBMYKLXXXX
TRANSACTION REFERENCE NO: TRN-99482-XYZ103

TRANSACTION DETAILS:
------------------------------------------------------------
TOTAL PRINCIPAL AMOUNT: USD 145000.00
APPLICABLE CHARGES FEE: USD 25.00
BENEFICIARY CREDIT: TELEGRAPHIC TRANSFER SUCCESSFUL
============================================================
"""

def extract_payment_metadata(raw_text):
    """
    Uses regular expressions to isolate and capture specific banking data fields 
    from unstructured OCR string outputs, matching operational compliance needs.
    """
    print("🚀 Initializing Regex Extraction Pipeline from OCR Raw Text...")
    
    # Custom regex patterns matching the specific banking infrastructure fields
    patterns = {
        'Date': r"DATE OF TRANSFER:\s*(.*)",
        'Sender_Bank': r"SENDER BANK NAME:\s*(.*)",
        'SWIFT_8BIC': r"SWIFT 8BIC ROUTING:\s*(.*)",
        'Transaction_Ref': r"TRANSACTION REFERENCE NO:\s*(.*)",
        'Amount_With_Currency': r"TOTAL PRINCIPAL AMOUNT:\s*(.*)",
        'Charges_Fee': r"APPLICABLE CHARGES FEE:\s*(.*)"
    }
    
    extracted_data = {}
    
    # Loop through patterns and extract information dynamically
    for field, pattern in patterns.items():
        match = re.search(pattern, raw_text)
        if match:
            extracted_data[field] = match.group(1).strip()
        else:
            extracted_data[field] = "NOT_FOUND"
            
    return extracted_data

def convert_to_structured_file(data_dict):
    """
    Converts the isolated data dictionary into a clean pandas DataFrame 
    and simulates exporting directly into automated CSV/Excel reports.
    """
    print("📈 Converting extracted metadata fields into a structured DataFrame...")
    
    # Wrap in a list to construct the DataFrame row
    df = pd.DataFrame([data_dict])
    
    # Simulate saving directly to operational paths
    output_filename = "sanitized_payment_output.csv"
    df.to_csv(output_filename, index=False)
    print(f"✅ Success! Data automatically structured and written to: {output_filename}")
    return df

if __name__ == "__main__":
    # Execute the end-to-end simulation pipeline
    extracted_fields = extract_payment_metadata(MOCK_OCR_TEXT)
    
    print("\n📦 Extracted Target Fields:")
    for k, v in extracted_fields.items():
        print(f" - {k}: {v}")
        
    print("\n")
    final_df = convert_to_structured_file(extracted_fields)
    print("\n🖥️ Final Excel/CSV Data Preview:")
    print(final_df.to_string())
