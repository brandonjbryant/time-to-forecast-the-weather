import numpy as np
import pandas as pd

def get_tokyo():
    '''
    This function takes in csv file and returns it as a dataframe.
    '''
    major_city_df = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
    tokyo = major_city_df[major_city_df.City == 'Tokyo']
    return tokyo

def clean_tokyo(df):
    '''
    This fucntion takes in a dataframe and fills all the nulls value with the mean value.
    '''
    df = df.fillna(df.mean())
    return df


def prep_tokyo(df):
    '''
    The function takes in a dataframe and converts dates to datetime,
     and set date as index, and creates the month and year columns, then returns the dataframe
     "
    '''
    df.dt = pd.to_datetime(df.dt)
    df = df.set_index('dt').sort_index()
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    return df

def wrangle_tokyo():
    '''
    This function wrangles the tokyo dataframe utilizing the acquire, prepare, and cleaning fucntions.
    '''
    df = get_tokyo()
    df = clean_tokyo(df)
    df = prepare_tokyo(df)
    return df