import pandas as pd

def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:
    df = logins.drop_duplicates(["id", "login_date"])
    df = df.sort_values(["id", "login_date"])
    
    active_ids = []
    for user_id, group in df.groupby("id"):
        streak = 1
        dates = group["login_date"].tolist()
        for i in range(1, len(dates)):
            if dates[i] - dates[i - 1] == pd.Timedelta(days=1):
                streak += 1
            else:
                streak = 1

            if streak >= 5:
                active_ids.append(user_id)
                break
    return (
        accounts[accounts["id"].isin(active_ids)]
        [["id", "name"]]
        .sort_values("id")
    )
