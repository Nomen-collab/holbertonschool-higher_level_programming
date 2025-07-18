# main_test.py
from task_00_intro import generate_invitations
import os # For cleaning up output files if necessary

# --- Ensure template.txt exists for this test ---
# You should have created it manually or you can create it programmatically for tests
template_content_for_test = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
"""
with open('template.txt', 'w') as file:
    file.write(template_content_for_test)
# --------------------------------------------------------

# Read the template from a file
try:
    with open('template.txt', 'r') as file:
        template_content = file.read()
except FileNotFoundError:
    print("Error: template.txt not found. Please create the template file.")
    template_content = "" # To avoid an error if the file doesn't exist

# List of attendees
attendees_data = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"} # Test for missing data
]

print("--- Test 1: Normal execution ---")
generate_invitations(template_content, attendees_data)

print("\n--- Test 2: Empty template ---")
generate_invitations("", attendees_data)

print("\n--- Test 3: Empty attendees list ---")
generate_invitations(template_content, [])

print("\n--- Test 4: Invalid template type (not a string) ---")
generate_invitations(123, attendees_data)

print("\n--- Test 5: Invalid attendees list type (not a list) ---")
generate_invitations(template_content, "not a list")

print("\n--- Test 6: Invalid attendees list type (list but not dictionaries) ---")
generate_invitations(template_content, [1, "two", {"name": "Test"}])

# Clean up generated files for tests
print("\n--- Cleaning up generated files ---")
for i in range(1, len(attendees_data) + 1):
    filename = f"output_{i}.txt"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed {filename}")
if os.path.exists('template.txt'):
    os.remove('template.txt')
    print("Removed template.txt")
