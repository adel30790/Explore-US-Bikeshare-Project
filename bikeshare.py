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
    city = input('which city You want to examine ?: ').casefold() #make case insensitive , from StackOverFlow
    
    
    while city not in CITY_DATA:
        print("No available information for this city !, please try again!")
        city = input('which city You want to examine ?: ').casefold()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    months= ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    month= input("please type which month you want to filter by or type 'all' for no filtering :").casefold()
    
    while month not in months:
        print("no available information for this period !, try again")
        month= input("please type which month you want to filter by or type 'all' for no filtering :").casefold()
        
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday' ,'thursday', 'friday' , 'saturday', 'sunday']
    
    day = input("please choose a day to filter by or type 'all' for no filtering. :").casefold()
    
    while day not in days:
        print("please type a valid day name and try again!.")
        day = input("please choose a day to filter by or type 'all' for no filtering. :").casefold()
        
        


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) #In order to separate data in time stamp. from stackoverflow
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    

    # TO DO: display the most common month
    
    df['month'] = df['Start Time'].dt.month
    
    popular_month = df['month'].mode()[0]
    
    print("the most common month: ", popular_month)
        
    # TO DO: display the most common day of week
    
    df['day'] = df['Start Time'].dt.weekday_name
    
    popular_day = df['day'].mode()[0]
    
    print("the most common day: ", popular_day)


    # TO DO: display the most common start hour
    df['start hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['start hour'].mode()[0]
    
    print("the most common start hour: ", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print("most commonly used start station is: ", popular_start_station)


    # TO DO: display most commonly used end station
    
    popular_end_station = df['End Station'].mode()[0]
    
    print("most commonly used end station is: ", popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df.groupby(["Start Station", "End Station"]).size().nlargest(1) #stackOverflow
    
    print("most common trip is: ", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time'] = pd.to_datetime(df['End Time']) 
    df['end hour'] = df['End Time'].dt.hour
    

    # TO DO: display total travel time
    Total_travel_time= (df['end hour'] - df['start hour']).sum()
    print('Total travel time is:', Total_travel_time) 



    # TO DO: display mean travel time
    Average_travel_time= (df['end hour']-df['start hour']).mean()
    print('Average travel time is:', Average_travel_time) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        Count_of_Genders= df['Gender'].value_counts()
        print('Counts of gender are: \n', Count_of_Genders)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birthyear= int(df['Birth Year'].min())
        print('The earliest year of birth is: ', earliest_birthyear)
        most_recent_birthyear= int(df['Birth Year'].max())
        print('The most recent year of birth is: ', most_recent_birthyear)
        most_common_year= int(df['Birth Year'].mode()[0])
        print('The most common year of birth is: ', most_common_year)
        
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """displays 5 rows of raw data upon user's request"""
    i=0
    while True:
        answer = input('would You like to see 5 rows of data ?\n (yes/no): ').casefold()
        if answer == 'yes':
            print(df.iloc[i:i+5, : ])
            i += 5
        else:
            break
         
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
