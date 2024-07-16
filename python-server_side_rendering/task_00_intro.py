import os


def generate_invitations(template, attendees):
    with open(template, 'r') as file:
        template = file.read()

    # Check input types and Handle empty inputs
    if not isinstance(template, str):
        raise TypeError('template content must be a string')
    if not template.strip():
        return
    if not isinstance(attendees, list):
        raise TypeError('attendees must be a list')
    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            raise TypeError("Error: each attendee must be a dictionary")
        missing_value = {key: (attendee.get(key) if attendee.get(key)
                               is not None else 'N/A') for key in
                         ['name', 'event_title', 'event_date',
                         'event_location']}

        formatted_content = template.format(**missing_value)

        output_file = f'output_{index}.txt'
        with open(output_file, 'w') as output:
            output.write(formatted_content)


attendees = [
        {
            "name": "Alice",
            "event_title": "Python Conference",
            "event_date": "2023-07-15",
            "event_location": "New York"
        },
        {
            "name": "Bob",
            "event_title": "Data Science Workshop",
            "event_date": "2023-08-20",
            "event_location": "San Francisco"
        },
        {
            "name": "Charlie",
            "event_title": "AI Summit",
            "event_date": None,
            "event_location": "Boston"
        },
        {}
    ]


generate_invitations("template.txt", attendees)

for i in range(1, len(attendees) + 1):
    output_file = f'output_{i}.txt'
    assert os.path.exists(output_file), f"{output_file} does not exist"
    with open(output_file, 'r') as file:
        content = file.read()
        print(content)


print("all tests passed")
