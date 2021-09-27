import nltk


def pre_process(query):
    words = nltk.word_tokenize(query)
    tags = nltk.pos_tag(words)
    par = nltk.RegexpParser('CHUNK: {<JJ|JJS|RBS>*<NN|NNS|NNP|NNPS>*}')
    chunk = par.parse(tags)

    tree_q = nltk.tree2conlltags(chunk)
    langlist = []
 
#    print(tree_q)
#    print(chunk)
    for tup in tree_q:
        st = ""
        if tup[1] == 'VB':
            st = tup[0]
        elif tup[2] == "B-CHUNK" or tup[2] == "I-CHUNK":
            st += tup[0]
        else:
            continue
        langlist.append(st)
    return langlist

    
def intent(query):
    langlist = pre_process(query)
#    print(langlist)
    if ("mail" in langlist)|("email" in langlist):
        return 'mail'
    elif ("search" in langlist):
        return 'searchs'
    elif ("google" in langlist):
        return 'searchg'
    elif ("play" in langlist):
        return 'play'  
    elif ("tweet" in langlist):
        return 'tweet'
    elif ("weather" in langlist):  
        return 'weather'
    elif ("open" in langlist):
        return 'open'
    else :
        return 'no'

#intent("HEY there! Can you send mail to pratyushac98@gmail.com saying can  you book tickets from Kashmir to Hyderabad ?Carol wants to know the cost too")