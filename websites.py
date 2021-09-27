import webbrowser
import random
from intention import pre_process
def open_website(q):
    p = False
    nope = ["cannot open the website...please try again","it seems that the website you are asking for is not in our database.Sorry.","please check your spellings and try again"]    
    websites = {"youtube":"https://www.youtube.com/",
      "facebook":"http://www.facebook.com/",
       "Twitter": "http://twitter.com/?lang=en",
       "tumblr":"http://www.tumblr.com/login",
       "Instagram":"http://www.instagram.com/?hl=en",
       "whatsapp":"http://www.whatsapp.com/",
       "Snapchat":"http://www.snapchat.com/",
       "orkut":"http://www.orkut.com/index.html",
       "pinterest":"http://in.pinterest.com/",
       "messenger":"http://www.messenger.com/",
       "skype":"http://itstillworks.com/13579570/skype",
       "gmail":"http://mail.google.com/mail/u/0",
       "wikipedia":"http://www.wikipedia.org/",
       "yahoo":"http://in.yahoo.com/",
       "wynk":"http://www.wynk.in/music",
       "gaana":"http://gaana.com/",
       "google":"http://www.google.com/",
       "zomato":"http://www.zomato.com/hyderabad",
       "swiggy":"http://www.swiggy.com",
       "book my show":"http://in.bookmyshow.com/",
       "trivago":"http://www.trivago.in/",
       "spotify":"http://www.spotify.com/",
        "saavan":"http://www.saavn.com/"}

    keywords = pre_process(q)
    
    for k in keywords:
        if k in websites:
            webbrowser.open(websites[k])
            p = True
    if(p==False):
        print(random.choice(nope))
#open_website("open googl")