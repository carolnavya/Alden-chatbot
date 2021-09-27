import random

def introduce():
    print("""Greetings!I'm Alden,your personal assistant.\nYou can ask me to do the following:\n
          $open websites(Just use the word 'open'!)\n
          $send gmail\n
          $play videos on youtube(Use the keyword 'play'!)\n
          $tweet your thoughts (^_~)\n(The keyword you gotta use is 'tweet')\n
          $To let me sleep say 'bye'""")
    
def inputs():
    greet = ["hey there!","hi!","hello!","ALOHA!","ANYASEYO!","YO!","BONJOUR!","Heyya!"]
    helper =["How can I help you?","What can I do for you?","What do you want me to do?","Can I be of any assistance?"]
    return (random.choice(greet)+" "+random.choice(helper)+" :")

def input2():
    helper2 = ["How else can I help you?","What else can I do for you?","Is there anything else?"]
    return(random.choice(helper2))
    
what_up_ques = ["supp","what up","what's up","whats up","what are you up to","watcha duin?","What are you doing?","whats going on?"]
what_up_ans = ["nuthin much","well...nuthin of importance","nuthing u neeed to know :D","waiting for your instructions"]
rest = {"what are you?":"I am ur personal assistant",
            "who are you?":"I am ur personal assistant",
            "what is your name?":"I am Alden.Your personal assistant! ^_^",
            "what all can you do?":"""I can do the following:
            $open websites(Just use the word 'open'!)\n
            $send gmail\n
            $play videos on youtube(Use the keyword 'play'!)\n
            $tweet your thoughts (^_~)\n(The keyword you gotta use is 'tweet'
            $To let me sleep say 'bye')"""
            }

def dont_understand():
    no = ["sorry!I dont understand","What you are trying to say is beyond my capabiity of understanding...can you please try again","can you please repeat yourself?"]
    return (random.choice(no)+"\n")

