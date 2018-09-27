# Lab 4

Lab 4 addresses scraping dynamic websites.

# Lab



# Things to Know

## Dynamic Websites

Most modern websites are dynamic. This means that they use client side
Javascript to execute transformations over the website. They occasionally
make API requests to a server to `GET` or `POST` data.

With libraries such as BeautifulSoup, we can only make resource requests, but we
cannot perform actions on a webpage, such as clicking a button or any other element.

To do this, instead of just downloading resources into our program, we will spawn a
browser and use it as a proxy for performing actions. Browsers can host the HTML and
execute Javascript on our behalf, and they can usually run "headless," which means
that they run without an interface (nothing shows up on the screen.)

Consider this NBA leaderboard:

https://stats.nba.com/leaders/?Season=2017-18&SeasonType=Regular%20Season

Notice that when you scroll to the bottom of the page and click on the next page
button for the table, nothing in the URL changed. The data in the table clearly changed,
but the URL in the browser didn't change. So if a new resource wasn't accessed, what
happened?

Open up this page in Google Chrome. Right click on the next page button for the table and
select "Inspect".  The developer tools will show up and you may notice that the button
contains an attribute called `ng-click`.  The `ng` tells us that they are using `Angular.js`
as a framework and the `click` tells us that some JS is being executed on click. We can
assume that something happens when we click the button.  As it happens


## Selenium

The most popular way of bending a browser to our will is a library called Selenium.
Selenium is an open source automation framework that is widely used for Quality
Assurance and less widely, but equally as successfully used for data scraping.

Selenium ships with a number of browsers than can be used including Chrome and Firefox,
but we want to use Tor.

Check out this [reference](https://seleniumhq.github.io/selenium/docs/api/py/api.html)
and this [tutorial](https://realpython.com/modern-web-automation-with-python-and-selenium/).


## Tor

