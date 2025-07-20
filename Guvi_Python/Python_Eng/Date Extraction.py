# You are required to create a Python function to extract all occurrences of a specific pattern (e.g., dates in the format MM/DD/YYYY) from a given text using regular expressions and quantifiers.

import re

text = "Today is 03/26/2024 and tomorrow is 03/27/2024."

def extract_dates(text, date_format= r'\d{2}/\d{2}/\d{4}'):
    match = re.findall(date_format,text)
    return match
extracted_match = extract_dates(text)
print(", ".join(extracted_match))