# Contact-tracing
The program solves 3 problems, with 3 methods:
1. find_persons: Find every PERSON that has visited a particular LOCATION on a particular date.
3. find_locations: Find every LOCATION that a particular PERSON has visited on a particular date
4. find_close_contacts: Given a specific PERSON and date, identify their CLOSE CONTACTS on that date

data.json file contains a list of locations which contains a list of persons and what date they attended particular locations.

## Instructions:
- Tools such as 'Postman' can be used to invoke the API
- Link to the API: https://5ipr59i4m8.execute-api.us-east-1.amazonaws.com/default/contact_tracing_function
- Use GET method 
- The payload goes inside 'Body' parameter of 'Event' parameter in json format
- The key value pairs go inside curly braces {}
- Example of valid input data:
{
  "person": "brandon \"bran\" stark",
  "date": "2021-02-04T00:00:00.000Z",
  "method": "find_close_contacts"
}
- Make sure to type the correct method name, listed in the beginning of this file.

Input Arguments for payload: 
- 'person' argument is the person's name for 'find_locations' and 'find_close_contacts' functions.
- 'date' argument is the date in ISO String. (Non-optional, all functions need this argument.)
- 'method' argument points to the appropriate functions inside the program. (Non-optional, all functions need this argument.)
- 'location' argument is the location's name for 'find_persons' function.

## Architectural design:
The program is running on AWS Lambda as the scale of this service is small and can be sufficed using AWS Lambda.
It has been hosted as a REST service and exposed via a public URL using AWS API Gateway with a GET request.


