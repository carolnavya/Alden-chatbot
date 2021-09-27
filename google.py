import webbrowser

def extract(q,k):
    print(k)
    stop_words = ['for','weather']
    keywords = q.split(" ")
    print(keywords)
    pos = keywords.index(k)
    x = keywords[pos+1]
    if x in stop_words:
        keywords.remove(x)
    sent = ' '.join(str(k) for k in keywords[pos+1:])
    return sent
        
def search(query,key):
    wts = extract(query,key)
    print(wts)
    url = "https://www.google.com/?#q="
    webbrowser.open_new(url+wts)


#search("can you google how to get Substring in python")