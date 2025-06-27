import pandas as pd

# Standalone script for quick suspicious user check
def detect_suspicious_logins():
    logins = pd.read_csv('data/logins.csv')
    logins['login_time'] = pd.to_datetime(logins['login_time'])
    logins.sort_values(by=['user_id', 'login_time'], inplace=True)
    suspicious_users = set()

    for user_id, group in logins.groupby('user_id'):
        group = group.sort_values('login_time').reset_index(drop=True)
        for i in range(1, len(group)):
            delta = (group.loc[i, 'login_time'] - group.loc[i - 1, 'login_time']).total_seconds()
            if delta < 300 and group.loc[i, 'ip_address'] != group.loc[i - 1, 'ip_address']:
                suspicious_users.add(user_id)

    return suspicious_users

if __name__ == "__main__":
    print("Suspicious Users:", detect_suspicious_logins())