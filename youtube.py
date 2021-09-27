import webbrowser
import urllib.request
import urllib.parse
import re
from intention import pre_process
def extract(q):
    keywords = pre_process(q)
    sent = ' '.join(str(k) for k in keywords)
    return sent

def play(query):
    req = extract(query)
    query_string = urllib.parse.urlencode({"search_query" : req})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])

#play("play bts on youtube")