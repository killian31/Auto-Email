from send_mail import send_email
import pandas as pd
import time

def send_all_emails(df, seconds=5):
    f = open('sent_mail.txt', 'w')
    for i in range(df.shape[0]):
        print("Sending to", df.iloc[i]['Mail'] + '...')
        send_email(df.iloc[i]['Surname'], df.iloc[i]['Mail'])
        f.write('Mail sent to: ' + df.iloc[i]['Surname'] + ' ' + df.iloc[i]['Name'] + '\n')
        print(i,'| ' + 'Mail sent to: ' + df.iloc[i]['Surname'] + ' ' + df.iloc[i]['Name'])
        time.sleep(seconds)
    f.close()
data = pd.read_csv('bdd_alumni.csv')
data.drop(['Unnamed: 0'], axis=1, inplace=True)
print(data.head())

a = input('Entrée pour envoyer...')

def main():
    send_all_emails(data, seconds=2)

if __name__=='__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)
