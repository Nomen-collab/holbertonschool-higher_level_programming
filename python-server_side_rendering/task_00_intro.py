import logging
import os

# Configure logging to display error messages
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template with placeholders
    and a list of attendees.

    Args:
        template (str): The content of the template with placeholders.
        attendees (list): A list of dictionaries, where each dictionary
                          represents an attendee with their data.
    """

    # 1. Input Type Validation
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Define the expected placeholders
    # The keys here correspond to the dictionary keys of the attendees
    placeholders_mapping = {
        "name": "{name}",
        "event_title": "{event_title}",
        "event_date": "{event_date}",
        "event_location": "{event_location}"
    }

    # 3. Process Each Attendee and Generate Output Files
    for i, attendee in enumerate(attendees):
        output_filename = f"output_{i + 1}.txt"
        processed_template = template

        # Replace each placeholder
        for key, placeholder in placeholders_mapping.items():
            # Use .get() to handle missing keys, with None as default
            value = attendee.get(key)

            # If the value is missing (None) or not provided, use "N/A"
            if value is None:
                value_to_replace = "N/A"
            else:
                value_to_replace = str(value) # Ensure the value is a string

            # Perform the replacement
            processed_template = processed_template.replace(placeholder, value_to_replace)

        # Write the processed content to an output file
        try:
            with open(output_filename, 'w') as f:
                f.write(processed_template)
            print(f"Generated {output_filename}") # Confirmation message for the terminal
        except IOError as e:
            logging.error(f"Error writing file {output_filename}: {e}")
