import pandas as pd
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def month_filter():
    """
        Asks user to specify a month to analyze.

        Returns:
            (str) month - name of the month to filter by, or empty string for no filter
    """
    month = ''
    while True:
        month = input("Which month? January, February, March, April, May or June\n")
        if month.lower() in ["january", "february", "march", "april", "may", "june"]:
            break
        else:
            print("'{}' is not a valid input!!Please try again\n".format(month))
    return month

def day_filter():
    """
        Asks user to specify a day to analyze.

        Returns:
            (str) day - order of the day to filter by, or 0 for no filter
    """
    day = 0
    while True:
        try:
            day = input("Which day? Please enter your response as an integer (e.g 1=sunday)\n")
            if int(day) in [1, 2, 3, 4, 5, 6, 7]:
                break
            else:
                print("A valid number is between 1 and 7 !Please try again\n")

        except ValueError:
            print("'{}' is not a valid input!!Please try again\n".format(day))
    return int(day)

def get_filters():
    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or empty string to apply no month filter
            (str) day - name of the day of week to filter by, or 0 to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!')
    city, month, day = "", "", 0

    # Asking the user to specify a city
    while True:
        city = input("Would you like to see data for chicago, new york city or washington?\n")
        if city.lower() in ["chicago", "new york city", "washington"]:
            break
        else:
            print("'{}' is not a valid input!!Please try again\n".format(city))
    # Asking the user to specify a month and a day
    while True:
        timing = input("Would you like to filter data by month, day or both? type \'none\' for no time filter\n")
        if timing.lower() == 'month':
            month = month_filter()
            break
        elif timing.lower() == 'day':
            day = day_filter()
            break
        elif timing.lower() == 'both':
            month = month_filter()
            day = day_filter()
            break
        elif timing.lower() == 'none':
            break
        else:
            print("'{}' is not a valid input!!Please try again\n".format(timing))
    print('-'*70)
    return city.lower(), month.title(), day

def load_data(city, month, day):
    """
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or empty string to apply no month filter
            (str) day - name of the day of week to filter by, or 0 to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """
    # Reading the csv file for the filtered city
    df = pd.read_csv(CITY_DATA[city])

    # Convert the start and end table to datatime object instead on strings
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != '':
        # use the index of the months list to get the corresponding int
        df = df[df['month'] == month]

    # filter by day if applicable
    if day != 0:
        days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
        df = df[df['day_of_week'] == days[day]]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    #days = {3: 'Sunday', 4: 'Monday', 5: 'Tuesday', 6: 'Wednesday', 7: 'Thursday', 1: 'Friday', 2: 'Saturday'}
    #months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print("Most popular month is --> {} ".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("Most popular day of the week is --> {}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("Most popular start hour is --> {}".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print("Most commonly used start station is --> {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("Most commonly used end station is --> {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent combination of start station and end station trip are --> {}".format((df['Start Station']+" [To] "+ df['End Station']).mode()[0]))


    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = (df['End Time']-df['Start Time']).sum()
    print("the total travel time is --> {}".format(total.round('1s')))

    # TO DO: display mean travel time
    average = (df['End Time']-df['Start Time']).mean()
    print("the average travel time is --> {}".format(average.round('1s')))


    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if 'Gender' in df.columns:
        # TO DO: Display counts of user types
        print("The user count is -->\n{}\n".format(df['User Type'].value_counts()))

        # TO DO: Display counts of gender
        print("The gender count is --> \n{}\n".format(df['Gender'].value_counts()))

        # TO DO: Display earliest, most recent, and most common year of birth
        early = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode())
        print("The earliest, most recent, and most common year of birth are --> {}, {}, {}".format(early, recent, common))
    else:
        print("The user gender is not available")

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def main():
    while True:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input("Would you like to see a sample of the data? Enter yes or no.\n").lower()
        i = 0

        while True:
            if raw_data == 'yes':
                df = df.reset_index(drop=True)
                print(df.loc[i:i+4])
                raw_data = input('\nWould you like to see another 5 rows? Enter yes or no.\n').lower()
                i = i+5
                if i > df.shape[0]:
                    break
            elif raw_data == 'no':
                break
            else:
                raw_data = input("\nYour input is invalid? Enter yes or no.\n'")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
