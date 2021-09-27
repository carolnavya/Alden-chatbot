from greetings import introduce,inputs,input2,dont_understand,what_up_ques,what_up_ans,rest
from intention import intent
from google import search
from youtube import play
from websites import open_website
from mail import extract
from tweet import tweet
from weather import extractw
import random
from details import deets
fin = True   

def input_query(query):
    if query in what_up_ques:
        print(random.choice(what_up_ans))
    elif query in rest:
        print(rest[query.lower()])
    else:
        task = intent(query)
        if task == 'searchs':
             search(query,'search')
        elif task == 'searchg':
             search(query,'google')
        elif task == 'mail':
             extract(query)
        elif task == 'tweet':
             tweet(query)             
        elif task == 'weather':
             extractw(query)
        elif task == 'open':
             open_website(query)
        elif task == 'play':
             play(query)
        elif task == 'no':
                print(dont_understand())

fin = True
y = 1

if __name__=='__main__':
    introduce()
    x = 1
    if y == 1:
        deets()
        y +=1        
    while fin ==True:
        if x == 1:
            print(inputs())
            x +=1
        else:
            print(input2())
        query = input()
        if query =='bye':
            print("\nGOODBYE!")
            fin = False
        else:
            input_query(query)
    