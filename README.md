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

### Code Structure
The code is structured in the following order:
1. Libraries that help with data handling are imported (time, NumPy, and pandas)
   Note: the time library comes preinstalled with Python
2. The .csv files are loaded
3. The user is asked to type the city they want to look at, then the month, then the day of the week
4. The data is filtered depending on what the user inputs (first, city, then month, then day) and loaded
5. New columns are calculated and loaded (such as most frequent time of travel)
6. The code displays all the results for the user
7. The code asks the user if they would like to see raw data and responds accordingly
8. The user is given the option to restart once all input options have been exhausted

### Error Handling
When promting users to input what they want, they may make spelling mistakes or ask for something not among the options. Script was added to respond to any undesired answer to prevent the script from breaking and to inform the user to input a valid option like so:

```python
allowed_cities = ["new york city", "chicago", "washington"]
 city = input("What city do you want to look at? Chicago, New York City, or Washington: ")
 while city.lower() not in allowed_cities:
      print("Sorry, " + city + " is not an allowed city.")
      city = input("What city do you want to look at? Chicago, New York City, or Washington: ")
```
Since Washington does not have gender or Birth Year data, if/else code was added to prevent the script from attempting to load that which doesn't exist. If the column is present, it loads it. If it doesn't, an else statemnt can be used to display a message to inform the user the data doesn't exist: 
```python
if 'Gender' in df:
            print("Gender Counts:\n", df['Gender'].value_counts())
else:
            print("Gender information is not available for the selected city.")
```

## Credits
The datasets and parts of the code were provided for by Udacity. Udacity's GPT and OpenAI's GPT assisted in fixing bugs and answering my questions. 
