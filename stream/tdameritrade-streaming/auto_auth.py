import time
import urllib
import requests
from splinter import Browser
from config import password, account_number, client_id, CHROMEDRIVER_PATH




def get_auth_token():
    # --------------------- AUTHENTICATION AUTOMATION --------------------------

    # define the location of the Chrome Driver - CHANGE THIS!!!!!
    executable_path = {'executable_path': config.CHROMEDRIVER_PATH}

    # Create a new instance of the browser, make sure we can see it (Headless = False)
    browser = Browser('chrome', **executable_path, headless=False)

    # define the components to build a URL
    method = 'GET'
    url = 'https://auth.tdameritrade.com/auth?'
    client_code = client_id + '@AMER.OAUTHAP'
    payload = {'response_type':'code', 'redirect_uri':'http://localhost/test', 'client_id':client_code}

    # build the URL and store it in a new variable
    p = requests.Request(method, url, params=payload).prepare()
    myurl = p.url

    # go to the URL
    browser.visit(myurl)

    # define items to fillout form
    payload = {'username': account_number,
               'password': password}

    # fill out each part of the form and click submit
    username = browser.find_by_id("username").first.fill(payload['username'])
    password = browser.find_by_id("password").first.fill(payload['password'])
    submit   = browser.find_by_id("accept").first.click()

    # click the Accept terms button
    browser.find_by_id("accept").first.click() 

    # give it a second, then grab the url
    time.sleep(1)
    new_url = browser.url

    # grab the part we need, and decode it.
    parse_url = urllib.parse.unquote(new_url.split('code=')[1])

    # close the browser
    browser.quit()



    # THE AUTHENTICATION ENDPOINT

    # define the endpoint
    url = r"https://api.tdameritrade.com/v1/oauth2/token"

    # define the headers
    headers = {"Content-Type":"application/x-www-form-urlencoded"}

    # define the payload
    payload = {'grant_type': 'authorization_code', 
               'access_type': 'offline', 
               'code': parse_url, 
               'client_id':client_id, 
               'redirect_uri':'http://localhost/test'}

    # post the data to get the token
    authReply = requests.post(r'https://api.tdameritrade.com/v1/oauth2/token', headers = headers, data=payload)

    # convert it to a dictionary
    decoded_content = authReply.json()                       


    # grab the access_token
    access_token = decoded_content['access_token']
    headers = {'Authorization': "Bearer {}".format(access_token)}