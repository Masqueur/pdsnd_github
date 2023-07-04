import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    allowed_cities = ["new york city", "chicago", "washington"]
    city = input("What city do you want to look at? Chicago, New York City, or Washington: ")

    while city.lower() not in allowed_cities:
        print("Sorry, " + city + " is not an allowed city.")
        city = input("What city do you want to look at? Chicago, New York City, or Washington: ")

    response = input("You want to look at " + city.title() + ". Is that correct? (yes/no) ")

    if response.lower() == "yes":
        print("Great! Let's look at " + city.title() + ".")
    elif response.lower() == "no":
        print("Sorry about that. Let's start over.")
    else:
        print("I'm sorry, I didn't understand your response.")
    

    # TO DO: get user input for month (all, january, february, ... , june)
    allowed_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    month = input("What month do you want to look at? Please spell out the whole month:")

    while month.lower() not in allowed_months:
        print("Sorry, " + month + " is not an allowed month.")
        month = input("What month do you want to look at? Please spell out the whole month: ")

    response = input("You want to look at " + month.title() + ". Is that correct? (yes/no) ")

    if response.lower() == "yes":
        print("Great! Let's look at " + month.title() + ".")
    elif response.lower() == "no":
        print("Sorry about that. Let's start over.")
    else:
        print("I'm sorry, I didn't understand your response.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    allowed_days = ["monday", "tuesday", "wednsday", "thursday", "friday", "saturday", "sunday"]
    day = input("What day of the week do you want to look at? Please spell out the whole word:")

    while day.lower() not in allowed_days:
        print("Sorry, " + day + " is not an allowed month.")
        day = input("What day of the week do you want to look at? Please spell out the whole word: ")

    response = input("You want to look at " + day.title() + ". Is that correct? (yes/no) ")

    if response.lower() == "yes":
        print("Great! Let's look at " + day.title() + ".")
    elif response.lower() == "no":
        print("Sorry about that. Let's start over.")
    else:
        print("I'm sorry, I didn't understand your response.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    if city.lower() == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city.lower() == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    elif city.lower() == 'washington':
        df = pd.read_csv('washington.csv')
    else:
        print('Invalid city name. Please choose either chicago, new york city, or washington.')
    return df

    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'January']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        if day != 'all':
            days = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            day = days.index(day) + 1

            # filter by month to create the new dataframe
            df = df[df['day'] == day]
        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if df is not None:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        most_common_month = df['month'].mode()[0]
        print('The most common month is:', most_common_month)

    # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.week
    most_common_week = df['week'].mode()[0]
    print('The most common week is:', most_common_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    station_counts = df.groupby(['Start Station', 'End Station']).size()
    most_frequent_combination = station_counts.idxmax()

    print('The most frequent combination of start station and end station trip is:', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time, 'seconds')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('User Type Counts:', user_type_counts)

    # TO DO: Display counts of gender
    def gender_counts(df):
        if 'Gender' in df:
            print("Gender Counts:\n", df['Gender'].value_counts())
        else:
            print("Gender information is not available for the selected city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        df.dropna(subset=['Birth Year'], inplace=True)
        df['Birth Year'] = df['Birth Year'].astype(int)
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print('The earliest birth year is:', earliest_birth_year)
        print('The most recent birth year is:', most_recent_birth_year)
        print('The most common birth year is:', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    def display_data(df):
        i = 0
        show_data = input('Would you like to see the first 5 rows of data? Enter yes or no\n')
        if show_data == 'yes':
            print(df.head())
            show_more = input('Would you like to see the next 5 rows of data? Enter yes or no.\n').lower()
            while show_more == 'yes':
                i +=5
                print(df[i:i+5])
                show_more = input('Would you like to see the next 5 rows of data? Enter yes or no.\n').lower()

        print('Thank you for using the data display feature.')
    display_data(df)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
