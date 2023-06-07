import datetime
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
    
    print("woul you like to see data for chicago, New york city, or washington?")
    
    while True:
        city = input("Enter the city:  chicago new york city or washington?    ")
        city = city.lower()
        state = list(CITY_DATA.keys())
        if city not in state:
            print("Enter a valid city")
        else:
            break
            
        
    # get user input for month (all, january, february, ... , june)
    
    while True:
        print("would you like to filter the data by month, day, both ?")
        option = input("  ")
        option = option.lower()
        filta = ["month","day","both"]
        if option not in filta:
            print("Enter a valid filter")
            
        else:
            break
            
    while True:
        month = input("Which month?  jan, feb, march, april, may, june  ")
        month =  month.lower()
        months = ["jan","feb","march","april","may","june"]
        if month not in months:
            print("Enter a valid month")
        else:
            break
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = eval(input("Which day?  Please Enter your response as integer(eg., 1=Sunday)   "))
        days = [1,2,3,4,5,6,7]
        if day not in days:
            print("Enter a valid day")
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
    
    for i in np.arange(0,len(df),5):
        
        option = input("Do you want to see the next 5 lines of raw data?  Please Enter your response as Yes or No   " )
        option = option.lower()
        if option =="yes":
            a = i
            b = a+5
            print(df.iloc[a:b])
        else:
            break
        
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day
    
    if month !="None":
        months = ["jan","feb","march","april","may","june"]
        month = months.index(month)+1
        
        df = df[df["month"]==month]
        
        
    if day !="None":
        
        df = df[df["day_of_week"]==day]
        
        

    return df

        

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    # display the most common month
    
    start_time = datetime.datetime.now()
    
    df["month"]= df["Start Time"].dt.month
    
    most_common_month = df["month"].mode()[0]
    
    month = ["Jan","Feb","march","April","may","june"]
    
    most_common_month = month[most_common_month-1]
    
    print('\nCalculating The First Statistics...\n Most common month is:',most_common_month)
    
    end_time = datetime.datetime.now()
    
    print("\nThis took .",  (end_time - start_time), "seconds")
    
    # display the most common day of week
        
    start_time2 = datetime.datetime.now()
    df["day"] = df["Start Time"].dt.day
    
    most_common_week = df["day"].mode()[0]
    
    week = ["Statuday","Sunday","Monday","Tuesday","Wenesday","Thursday","Friday"]
    most_common_week= week[ most_common_week-1]
    
    print('\nCalculating The next Statistics...\n Most common week:', most_common_week)
   
    end_time2 = datetime.datetime.now()
    
    print("\nThis took .",  (end_time2 - start_time2), "seconds")
        
    # display the most common start hour
    
    start_time = datetime.datetime.now()
    df["hour"]= df["Start Time"].dt.hour
    popular_hour=df["hour"].mode()[0]

    print('\nCalculating The next Statistics...\n Most popular hour:',popular_hour)
    
    end_time = datetime.datetime.now()
    
    print("\nThis took .",  (end_time - start_time), "seconds")
    
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    # display most commonly used start station

    start_time = datetime.datetime.now()
    popular_start_station = df["Start Station"].mode()[0]
    print('\nCalculating The next Statistics...\nCalculating The Most Popular start Stations:\n',popular_start_station)
    end_time = datetime.datetime.now()
    print("\nThis took .",  (end_time - start_time), "seconds")
    start_time = datetime.datetime.now()
    
     # display most commonly used end station
        
    popular_end_station = df["End Station"].mode()[0]    
    print('\nCalculating The next Statistics...\nCalculating The Most Popular end Stations:\n',popular_end_station)
    end_time = datetime.datetime.now()
    print("\nThis took .",  (end_time - start_time), "seconds")
    
    
    # display most frequent combination of start station and end station trip
    
    start_time = datetime.datetime.now()
    
    df["combine_trip"] = df["Start Station"]+"   "+"to"+"   "+df["End Station"].mode()[0]
    
    popular_combine_trip = df["combine_trip"].mode()[0]
    
    print('\nCalculating The next Statistics...\nCalculating The Most frequently combination trip:\n', popular_combine_trip)
    
    end_time = datetime.datetime.now()
    
    print("\nThis took .",  (end_time - start_time), "seconds")
    
     # Display most popular trip
    
    start_time = datetime.datetime.now()
    
    popular_trip = df.groupby(["Start Station","End Station"]).size().nlargest(1)
    
    print('\nCalculating The next Statistics...\nCalculating The Most Popular Trip:\n',popular_trip)
    
    end_time = datetime.datetime.now()
    
    print("\nThis took .",  (end_time - start_time), "seconds")
    

    print('-'*40)


    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    # display total travel time
    
    start_time = datetime.datetime.now()

    total_travel_time = round(df["Trip Duration"].sum(),2)
    
    print('\nCalculating The next Statistics...\nCalculating The total travel time:\n', total_travel_time,
          "Second","or",  round(total_travel_time/3600,2), "Hour")
    
    end_time = datetime.datetime.now()
    
    print("\nThis took .",  (end_time - start_time), "seconds")
    
   
     # display  travel mean time
    
    start_time = datetime.datetime.now()

    avg_time = round(df["Trip Duration"].mean(),2)
    
    print('\nCalculating The next Statistics...\nCalculating The average travel time:\n', avg_time,
          "Second", "or",  round(avg_time/3600,2), "Hour")
    
    end_time = datetime.datetime.now()
    
    print("\nThis took .",  (end_time - start_time), "seconds")
    

    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""


    # Display counts of user types
    
    start_time = datetime.datetime.now()

    user_type = df["User Type"].value_counts()
    
    print('\nCalculating The next Statistics...\nDisplay counts of user types:\n', user_type)
    
    # Display counts of gender
    if "Gender" in df:
        
        accounts_of_gender = df["Gender"].value_counts()
        print("\n counts of Gender:\n",  accounts_of_gender)
        
    
    end_time = datetime.datetime.now()
    
    print("\nThis took .",  (end_time - start_time), "seconds")


    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        
    
        start_time = datetime.datetime.now()
    
        earliest_year = int(df["Birth Year"].min())
    
        recent_year = int(df["Birth Year"].max())
    
        common_year = int(df["Birth Year"].mode()[0])
    
        print('\nCalculating The next Statistics...\nDisplay earliest year of birth:\n', earliest_year,
         "\nDisplay recent year of birth:",recent_year, 
          "\nDisplay common year of birth:", common_year )
    
        end_time = datetime.datetime.now()
        print("\nThis took .",  (end_time - start_time), "seconds")
    

    print('-'*40)


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

