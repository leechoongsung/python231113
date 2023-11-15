import re

def is_valid_email(email):
    # Define the regular expression pattern for a simple email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use the search() function to check if the email matches the pattern
    match = re.search(pattern, email)

    # If a match is found, the email is valid
    return match is not None

# Test the function with 10 sample email addresses
sample_emails = [
    'user@example.com',
    'john.doe@company.org',
    'invalid-email',
    'missing_at_symbol@example',
    'user@.com',
    'user@com',
    'user@domain-without-dash.com',
    'user@domain_with_underscore.com',
    'user@123.45.67.89',
    'user@subdomain.example.com',
]

for email in sample_emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
