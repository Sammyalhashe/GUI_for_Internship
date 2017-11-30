from mechanize import Browser
from mechanize import CookieJar

"""Constants

[Necessary items to log-on such as Email, password, workspace name]
"""
url = "https://slack.com/signin"
workspace = "personalcodeupdates"
email = "sammyalhashemi1@gmail.com"
password = "Rfin1ihe"

channel = raw_input("channel name")

"""Configuring the Browser using mechanize

[
    1) Instantiate browser class
    2) Configure it to not handle robot questions
    3) Intiantiate a CookieJar class
    4) Set the Browser's CookieJar to be the class just instantiated
]
"""
browser = Browser(history=None, request_class=None,
                  content_parser=None, allow_xhtml=False)
browser.set_handle_robots(False)
cookie = CookieJar(policy=None)
browser.set_cookiejar(cookie)
browser.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

"""Opening the website and browser

[
    1) Get reponse from inputting workspace url
    2) Get reponse from inputting email and password
]
"""

# workspace url
browser.open(url)
browser.select_form(nr=0)
browser.form['domain'] = workspace

response_workspace = browser.submit()
print(response_workspace.read())

## email and password
browser.select_form(nr=1)
browser.form['email'] = email
browser.form['password'] = password

response_login = browser.submit()
print(response_login.read())


"""Choose Channel to add to

[Ie. twittercode_snippets]
"""

browser.click_link(text=channel)
