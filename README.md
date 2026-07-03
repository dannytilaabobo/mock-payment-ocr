# Automated Payment PDF OCR Extractor (Sanitized Core Concept)

## 📌 Context & Operational Mandate
In high-volume global payment operations, processing unstructured documents (like remittance advices or swift receipts) manually is a significant source of operational risk, SLA breach, and human fatigue. 

This repository contains a **sanitized, non-proprietary simulation framework** of an end-to-end data pipeline that I designed in a local python shell. It proves the architectural capability to convert raw, unstructured image/PDF text blocks into production-ready tabular data formats.

## 🛠️ Extracted Target Core Fields
The pipeline utilizes targeted regular expression matching paired with a `pandas` compiler to dynamically extract the following critical operational metadata from raw text:
- **Date:** Isolates processing dates for cutoff enforcement.
- **Sender Bank:** Maps out originating clearing entities.
- **SWIFT 8BIC:** Extracts routing identifiers for automated lookups.
- **Transaction Reference (Tran Ref):** Captures the unique system tracking key.
- **Amount with Currency:** Segregates high-value fund units.
- **Charges Fee:** Captures deduction rules for automated reconciliation.

## 💡 How the Architecture Works
1. **OCR Text Emulation:** Simulates string data fed into the python shell after passing through a `pytesseract` (Tesseract OCR) image extraction tool.
2. **Deterministic Processing:** A regex engine targets specified delimiters and fields without requiring manual intervention.
3. **Data Compilation:** Compiled keys are loaded into a `pandas.DataFrame` architecture and automatically exported into `.csv` / `.xlsx` templates for the clearing and core reconciliation teams.

## 📈 Measurable Business Impact
- **Efficiency:** Drastically reduces manual data extraction and multi-page form encoding time.
- **Risk Mitigation:** Prevents data-entry typos on critical payment identifiers like the Transaction Reference and SWIFT 8BIC.
