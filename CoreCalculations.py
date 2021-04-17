import pandas as pd

def load_data(chicago, NY, washington):
    '''chicago is boolean,
        NY is boolean,
        washington is boolean,
        the function returns the data frame from the required cities'''
    flag = False
    if chicago:
        data = pd.read_csv('chicago.csv')
        flag = True
    if NY:
        if(flag):
            data = data.append(pd.read_csv('new_york_city.csv'))
        else:
            data = pd.read_csv('new_york_city.csv')
        flag = True
    if washington:
        if(flag):
            data = data.append(pd.read_csv('washington.csv'))
        else:
            data = pd.read_csv('new_york_city.csv')
        flag = True
    if(not flag):
        #print("Select at least one city")
        return None
    else:
        return data
#################################################################
def max_month(data): #max month in the whole 6 months or in filtered sent data
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    return data['Start Time'].dt.month_name().mode()[0] #if you want to return the month number: data['Start Time'].dt.month.mode()[0]

def max_day_week(data):
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    return data['Start Time'].dt.day_name().mode()[0]

def max_hour_day(data):
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    return data['Start Time'].dt.hour.mode()[0]

def max_date(data):
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    return data['Start Time'].dt.date.mode()[0]
# ##############################################################
def max_start_station(data):
    return data['Start Station'].mode()[0]

def max_end_station(data):
    return data['End Station'].mode()[0]

def common_trip(data):
    #max(Start Station and End Station)
    #merge the 2 columns into 1 column
    data['Trip'] = data['Start Station']+" to "+data['End Station']
    return data['Trip'].mode()[0]
###############################################################
def total_travel_time(data):
    return data[['Trip Duration']].sum()[0]

def average_travel_time(data):
    return data[['Trip Duration']].mean()[0]

def min_travel_time_trip(data): #should it return all information about the rows of minimum travel time trip?
    return data[['Trip Duration']].min()[0]

def max_travel_time_trip(data):
    return data[['Trip Duration']].max()[0]

def standard_deviation_of_travel_time(data):
    return data[['Trip Duration']].std()[0]

# ###########################################################
def compare_female_males(data):
    #Already cheched there is Gender column in the GUI in BikeShare.py
    return data['Gender'].value_counts()

def compare_subscribers_customers(data):
    return data['User Type'].value_counts()

def youngest_users(data):
    #there is NaN
    #data.fillna(0)
    youngest_birth_date = data[['Birth Year']].max()[0]
    youngest_age = 2017-youngest_birth_date
    return youngest_age

def oldest_users(data):
    return 2017-data[['Birth Year']].min()[0]

def mode_age(data):
    #most common age
    return 2017-data[['Birth Year']].mode()['Birth Year'][0]


def average_age(data):
    return 2017-data[['Birth Year']].mean()[0]

def median_age(data):
    return 2017-data[['Birth Year']].median()[0]

##########################################################
def filter_by_months(data, *months):
    '''
    :param data:
    :param months: should range from 1 to 6 corresponding to months from January to June
    :return:
    '''
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    filtered_data = pd.DataFrame()
    for month in months:
        # dt.month_name() if you want to make it by month name not month number
        filtered_data = filtered_data.append(data[data['Start Time'].dt.month == month])
    return filtered_data

def filter_by_days_in_month(data, *input_day_numbers):
    #handle all and none options: already handled in the GUI  in BikeShare.py
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    filtered_data = pd.DataFrame()
    for day in input_day_numbers:
        filtered_data = filtered_data.append(data[data['Start Time'].dt.day == day])
    return filtered_data

def filter_by_days_in_week(data, *input_days):
    '''

    :param data:
    :param input_days: The first letter should be capital and the rest are small like: Thursday; use method str.title() to enter the parameter correctly
    :return:
    '''

    data['Start Time'] = pd.to_datetime(data['Start Time'])
    filtered_data = pd.DataFrame()
    for day in input_days:
        filtered_data = filtered_data.append(data[data['Start Time'].dt.day_name() == day])
    return filtered_data

def filter_by_hour(data, *input_hours):
    '''

    :param data:
    :param hours: should be integers from 0 to 23
    :return:
    '''
    data['Start Time'] = pd.to_datetime(data['Start Time'])

    filtered_data = pd.DataFrame()
    for hour in input_hours:
        filtered_data = filtered_data.append(data[data['Start Time'].dt.hour == hour])
    return filtered_data
#############################################################
