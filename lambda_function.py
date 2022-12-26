import json
from datetime import datetime

        
def find_persons_at_location(locations, location_name, date):
    """Find every PERSON that has visited a particular LOCATION on a particular date."""
    persons_at_location = []
    for location in locations:
        if location_name.lower() == location['location'].lower():
            for person in location['persons']:
                if date in person['dates']:
                    persons_at_location.append(person['person'])

    if len(persons_at_location) > 0:
        return f"The following persons visited {location_name} on {date}: {persons_at_location}"
    else:
        return f"No one visited {location_name} on {date}"
    

def find_locations_visited(locations, person_name, date):
    """Find every LOCATION that a particular PERSON has visited on a particular date."""
    locations_visited = []
    for location in locations:
        for person in location["persons"]:
            if person_name.lower() == person['person'].lower() and date in person['dates']:
                locations_visited.append(location['location'])

    if len(locations_visited) > 0:
        return f"{person_name} visited the following locations on {date}: {locations_visited}"
    else:
        return f"{person_name} visited no locations on {date}"
    

def find_close_contacts(locations, person_name, date):
    """Given a specific PERSON and date, identify their CLOSE CONTACTS on that date."""
    close_contacts = []
    for location in locations:
        person_present_at_location = False
        
        for person in location["persons"]:
            if person['person'].lower() == person_name.lower() and date in person['dates']:
                    person_present_at_location = True
                    break

        if person_present_at_location:
            for person in location["persons"]:
                if person['person'].lower() != person_name.lower() and date in person['dates']:
                        close_contacts.append(person['person'])

    if len(close_contacts) > 0:
        return f"{person_name}'s close contacts on {date}: {close_contacts}"
    else:
        return f"{person_name} had no close contacts on {date}"


def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f%z')
        return True
    except ValueError:
        return False
    
    
def lambda_handler(event, context):
    # Open the file
    try:
        with open('data.json', 'r') as f:
            # Load the contents of the file as a JSON object
            data = json.load(f)
    except FileNotFoundError:
        return {
            'statusCode': 500,
            'body': "Error: data.json file not found" 
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': "Error: Invalid JSON format in data.json file"
        }
    
    if not data:
        return {
            'statusCode': 500,
            'body': "Error: data.json file is empty"
        }
    
    locations = []
    
    # Get the location and persons data from the JSON object
    for data_entry in data:
        locations.append(data_entry)
        
    if event['body'] is not None:
        try:
            body = json.loads(event['body'])
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': "Error: Invalid JSON format in input"
            }
        
    else:
        return {
            'statusCode': 422,
            'body': "Error: No arguments provided."
        }
    person_name = body.get('person')
    
    date = body.get('date')
    if not is_valid_date(date):
        # Handle invalid date input
        return {
                'statusCode': 422,
                'body': "Error: date format is invalid"
            }
    
    location_name = body.get('location')
    method = body.get('method')
    
    if not method:
        return {
            'statusCode': 422,
            'body': "Error: method argument is required"
        }

    if method not in ["find_locations", "find_persons", "find_close_contacts"]:
        return {
            'statusCode': 422,
            'body': "Error: Invalid value for method argument"
        } 
        
    if not date:
        return {
            'statusCode': 422,
            'body': "Error: date argument is required"
        }
    

    if not person_name and not location_name:
        return {
            'statusCode': 422,
            'body': "Error: Either person or location argument is required"
        }

    if location_name and date and method == "find_persons":
        # If a location name and date are provided, find the persons at the location
        result = find_persons_at_location(locations, location_name, date)
    
    elif person_name and date and method == "find_locations":
        # If a person name and date are provided, find the locations they visited.
        result = find_locations_visited(locations, person_name, date)
    
    elif person_name and date and method == "find_close_contacts":
        # If a person name and date are provided, find the close contacts
        result = find_close_contacts(locations, person_name, date)
    
    else:
        # If no input is provided, print an error message
        result = "Check input and retry."
   
    if result:
        return {
            'statusCode': 200,
            'body': result
        }
    else:
        return {
            'statusCode': 200,
            'body': "No data found for the specified input"
        }
