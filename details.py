import webbrowser

def deets():
    print("Let me ask you a few questions before we start")
    deets.email_id = input('Enter you gmail id:')
    deets.password = input('Enter your gmail password:')
    decision = input("Do you have Twitter Access keys?Say yes or no:")
    if decision == 'no':
        print("Please create a new app to generate access tokens")
        webbrowser.open("https://apps.twitter.com/")
    else:
        deets.consumer_key = input("Enter the consumer key:")       
        deets.consumer_secret = input("Enter the consumer secret key:")
        deets.access_token = input("Enter the access token:")
        deets.access_token_secret = input("Enter the access token secret:")
