def generate_invitations(template, attendees):
    with open('template.txt', 'r') as file:
        template = file.read()

    # Check input types and Handle empty inputs
    if not isinstance(template, str):
        raise TypeError('template content must be a string')
    if not isinstance(attendees, list):
        raise TypeError('attendees must be a list')
    if not template:
        raise ValueError("Template is empty, no output files generated.")
    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    # Process each attendee
    for index, attendee in attendees(start=1):
        if not isinstance(attendee, dict):
            raise TypeError("Error: each attendee must be a dictionary")
        missing_value = {key: attendee.get(key, 'N/A') for key in
                        ['name', 'event_title', 'event_date', 'event_location']}
        formatted_content = template.format(**missing_value)

        output_file = f'output_{index}.txt'
        with open('output.txt', 'w') as output:
            output.write(formatted_content)

values = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

generate_invitations('template.txt', values)
