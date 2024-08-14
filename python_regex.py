
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

#Extract all email address
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
# Filter out email address from exclude.com
filtered_emails = [email for email in emails if not re.search(r"@exclude\.com", email)]
print(filtered_emails)
