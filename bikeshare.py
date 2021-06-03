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
    while True:
        city=input("Which city do you want(chicago, new york city, washington)?").lower()
        if city not in CITY_DATA:
            print("Sorry, I didnot understand that.")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Which month do you want(all, january, february, ... , june)?").lower()
        if month!='january' and month!='february' and  month!='march' and month!='april'and month!='may' and month!='june' and month!='all':
            print("Sorry, I didnot understand that.")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Which day do you want(all, monday, tuesday, ... sunday)?").lower()
        if day!='monday'and day!='tuesday'and month!='wednesday'and day!='thursday'and day!='friday'and day!='Saturday'and day!='sunday'and day!='all':
            print("Sorry, I didnot understand that.")
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('\nMost Frequent month:', popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Frequent day of week :', popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Frequent Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Frequent Start Station:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Frequent End Station:', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_start_and_end_station= ('from ' + df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('\nMost Frequent combination of start station and end station trip:', popular_start_and_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nThe Total Travel Time: ",total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe Mean Travel Time: ",mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df , city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe counts of user types:\n",user_types)
    if city == 'chicago' or city == 'new york city':
        # TO DO: Display counts of gender
        genders_counts = df['Gender'].value_counts()
        print("\nThe counts of Gender:\n",genders_counts)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year Of Birth :', earliest_year)
        most_recent = df['Birth Year'].max()
        print('\nMost Recent Year Of Birth :', most_recent)
        popular_yearofbirth = df['Birth Year'].mode()[0]
        print('\nMost popular Year Of Birth :', most_recent)
    else:
        print("\nThere's no info about gender in this city")
        print("\nThere's no info about year of birth in this city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_data(df):
    print(df.head())
    i = 0
    while True:
        answer = input("'\Do you want to view anthor five row (yes or no)?").lower()
        if answer != 'yes':
            return
        i += 5
        print(df.iloc[i:i+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            answer = input(" Do you want to view first five row (yes or no)?").lower()
            if answer != 'yes':
                break
            get_data(df)
            break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
