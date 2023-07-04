# Bike Share Data Analysis with Python

## Project Description
This is a database of bike share data for three U.S. cities: Chicago, Washington, and New York City. The coding prompts the user to select the city they want to look at, the month, and the day of the week and shows them that data.

## Usage Instructions
### Error Handling
When promting users to input what they want, they may make spelling mistakes or ask for something not among the options. If so, code can be added to tell the user to input a valid option like so:
`allowed_cities = ["new york city", "chicago", "washington"]
 city = input("What city do you want to look at? Chicago, New York City, or Washington: ")
 while city.lower() not in allowed_cities:
      print("Sorry, " + city + " is not an allowed city.")
      city = input("What city do you want to look at? Chicago, New York City, or Washington: ")`
