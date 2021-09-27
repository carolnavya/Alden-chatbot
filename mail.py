import smtplib
import nltk
from intention import pre_process
from details import deets

def extract(q):
    sub = 'sent through Alden'
    keywords = pre_process(q)
    print(keywords)
    if 'gmail.com' in keywords:
        x = keywords.index('gmail.com')
        to = keywords[x-2]+keywords[x-1]+keywords[x]
        print(to)
        '''
    if 'subject' in keywords:
        y = keywords.index('subject')
        if keywords[y-1]==keywords[x]:
            words = nltk.word_tokenize(q)
            y = words.index("subject")
            for word,tag in nltk.pos_tag(keywords[y:]):
                sub = sub+" "+word
                print(sub)
        else:
            while(x!=y-1):
                x+=1
                print("x")
                sub = sub+" "+keywords[x]
           '''
    shabd= nltk.word_tokenize(q)
    print(shabd)
    z = shabd.index('@')
    print(x)
    msg = ''
    for w in shabd[z+2:]:
        msg = msg+" "+w
    print(msg)
    send_email(sub,msg,to)

def send_email(subject, msg,TO_ADDRESS):
    EMAIL_ADDRESS = str(deets.email_id)
    PASSWORD = str(deets.password)
    print("Please wait for few moments")
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, TO_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


#subject = "Test subject"
#msg = "YO!!! We can send emails now!!!!"
#extract("send mail to carolnavya1999@gmail.com with subject call me with the meeting details that states that")