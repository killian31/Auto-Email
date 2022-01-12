from send_mail import send_email
import pandas as pd
import time

def send_all_emails(df, seconds=5):
    # write down every user you sent an e-mail to 
    f = open('sent_mail.txt', 'w')
    for i in range(df.shape[0]):
        print("Sending to", df.iloc[i]['Mail'] + '...')
        send_email(df.iloc[i]['Surname'], df.iloc[i]['Mail'])
        f.write('Mail sent to: ' + df.iloc[i]['Surname'] + ' ' + df.iloc[i]['Name'] + '\n')
        print(i,'| ' + 'Mail sent to: ' + df.iloc[i]['Surname'] + ' ' + df.iloc[i]['Name'])
        # wait between each email to avoid problems
        time.sleep(seconds)
    f.close()

def main():
    send_all_emails(data, seconds=2)
    
data = pd.read_csv('db_emails.csv')
print(data.head())

a = input('Hit Enter to begin...')

if __name__=='__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)
