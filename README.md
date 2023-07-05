# Bike Share Data Analysis with Python

## Project Description
This is a database of bike share data for three U.S. cities: Chicago, Washington, and New York City. The coding prompts the user to select the city they want to look at, the month, and the day of the week and shows them that data.

## Installation Requirements
Python 3, NumPy, and pandas are required to run this program which can be downloaded from the web. A text editor such as Atom or Sublime can be helpful in visualising the code, but is not necessary.

## Usage Instructions
### The Datasets
There are three .csv files for each city discussed above in the database. Each includes the following data from the first six months of 2017:
1. Start Time (year-month-day, time)
2. End Time (year-month-day, time)
3. Trip Duration (in seconds)
4. Start Station
5. End Station
6. User Type (Subscriber or Customer)
The Chicago and New York City files also have a Gender column and a Birth Year column.

### Error Handling
When promting users to input what they want, they may make spelling mistakes or ask for something not among the options. Script was added to respond to any undesired answer to prevent the script from breaking and to inform the user to input a valid option like so:

```python
allowed_cities = ["new york city", "chicago", "washington"]
 city = input("What city do you want to look at? Chicago, New York City, or Washington: ")
 while city.lower() not in allowed_cities:
      print("Sorry, " + city + " is not an allowed city.")
      city = input("What city do you want to look at? Chicago, New York City, or Washington: ")
```
## Credits
The datasets and parts of the code were provided for by Udacity. Udacity's GPT and OpenAI's GPT assisted in fixing bugs and answering my questions. 
