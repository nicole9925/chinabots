import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates

def create_dfs():
    """
    Returns 2 dataframes, users then tweets
    """
    # load in users and tweet dfs
    users1 = pd.read_csv("data/users1.csv")
    users2 = pd.read_csv("data/users2.csv")
    users3 = pd.read_csv("data/users3.csv")
    users = pd.concat([users1, users2, users3])
    
    tweets1 = pd.read_csv("data/tweets1.csv", low_memory=False)
    tweets2 = pd.read_csv("data/tweets2.csv", low_memory=False)
    tweets3 = pd.read_csv("data/tweets3_1.csv", low_memory=False)
    tweets4 = pd.read_csv("data/tweets3_2.csv", low_memory=False)
    tweets5 = pd.read_csv("data/tweets3_3.csv", low_memory=False)
    tweets = pd.concat([tweets1, tweets2, tweets3, tweets4, tweets5])
    
    return users, tweets

def account_creation(users):
    """
    Displays account creation by year
    """
    users_copy = users.copy()
    
    #convert to datetime, and then date
    users_dt = pd.to_datetime(users_copy.account_creation_date).apply(lambda x: x.date())
    users_copy.loc[:,'account_creation_date'] = users_dt.values
    
    # groupby creation date to get counts
    account_creation_counts = users_copy.groupby('account_creation_date').count().reset_index()[['account_creation_date', 'userid']]
    
    # create x (dates) and y (account_counts) values for graph
    dates = matplotlib.dates.date2num(account_creation_counts.account_creation_date)
    account_counts = account_creation_counts.userid.values
    
    # create graph
    plt.plot_date(dates, account_counts)
    
    return None

def account_creation_2(users):
    """
    Displays account creation by year, binned at each year
    """
    users_dt = pd.to_datetime(users.account_creation_date)
    users.loc[:,'account_creation_date'] = users_dt.values
    
    (
    users['account_creation_date']
    .groupby([users["account_creation_date"].dt.year])
    .count()
    .plot(title='Account Creation by Year', figsize=(15,10),kind="bar")
    )
    
def tweet_language(tweets):
    """
    displays top 10 most tweeted in languages by suspended accounts
    """
    return tweets['tweet_language'].groupby(tweets['tweet_language']).count().nlargest(10)

def tweet_language_in(tweets):
    """
    displays top 10 userids of those who tweeted in indonesian
    """
    tweet_lang_user = tweets[['userid','tweet_language']][tweets['tweet_language'] == 'in']['userid']
    return tweet_lang_user.groupby(tweet_lang_user).count().nlargest(10)

def tweet_time(tweets):
    """
    displays concentration of tweets by time, in UTC
    """
    tweets.loc[:, 'tweet_time'] = pd.to_datetime(tweets.tweet_time).values
    tweet_time_groupby = tweets['tweet_time'].groupby(tweets['tweet_time'].dt.hour).count()
    
    tweet_time_groupby.plot(title='Tweet Times')