import time
from brainyquote import pybrainyquote
def randomquote():#Used to return a random quote from BrainyQuotes official website.
    random=(pybrainyquote.get_random_quote())
    print(random)
    string=''.join(str(e) for e in random)
    string=string.replace('<img alt=','').replace('"','')
    word=string.split('.')
    #To return the value to the function.
    return(word[0])
    #To print on Command prompt instead of being pushed a notification
    #print(word[0])

from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Quote for the day",
                   randomquote(),
                   icon_path=None,
                   duration=10)

























