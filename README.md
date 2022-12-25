# contact-tracing

data.json file contains a list of locations which contains a list of persons and what date they attended particular locations.

The program solves 3 problems, with 3 functions:
1. find_persons: Find every PERSON that has visited a particular LOCATION on a particular date.
2. find_locations: Find every LOCATION that a particular PERSON has visited on a particular date.
3. find_close_contacts: Given a specific PERSON and date, identify their CLOSE CONTACTS on that date. 

Instructions:
- Tools such as 'postman' can be used to invoke the API
- Use GET method 
- The payload goes inside 'Body' in json format

Non-optional arguments in payload:
1. Date
2. Method

Make sure to type the correct method name
Make sure to type the date in correct format, exactly same as in data.json
