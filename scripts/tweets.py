import pandas as pd 

def find_random_user(users, tweets):
    df = None
    while df is None or df.shape[0] == 0:
        user = users.sample(1)
        user_name = user["user_display_name"].item()
        df = tweets.loc[tweets["user_display_name"] == user_name]
    df["tweet_time"] = pd.to_datetime(df["tweet_time"], errors="coerce")
    return df.reset_index(drop=True).copy(), user.reset_index(drop=True).copy()