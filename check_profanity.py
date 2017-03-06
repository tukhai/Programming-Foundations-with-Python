import urllib
import urllib.request
import urllib.error

def read_text():
    quotes = open(r"D:\5GraduationWEBSITES-UDACITY\PREPARATION COURSES\1.Programming Foundations with Python\zzzshit.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    link = 'http://www.wdylike.appspot.com/?q='+str(text_to_check)
    connection = urllib.request.urlopen(link)
    output = connection.read()
    print(connection.read())
    connection.close()
    
read_text()
#check_profanity("shit")
