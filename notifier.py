import urllib2
import time


def internet_on():
    try:
        # as of november the third saime is throwing a code 503 to let the user
        # know that the site is down
        urllib2.urlopen('https://tramites.saime.gob.ve', timeout=60)
        return True
    except urllib2.URLError as err:
        return False


timer = 30
while True:
    if(internet_on()):
        print("found url")
        timer = 3600
        # TODO: read a property to find the emails to send the notification
        # TODO: and then call the function that sends the actual email
    else:
        print("error finding the url")
        timer = 30
    time.sleep(timer)
