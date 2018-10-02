# Lab 3

This lab is going to cover web scraping for static websites.


# Lab

For this lab, you will be using the NBA statistics website:

https://stats.nba.com/players/

Starting at the above link, extract the top 5 players under Three Pointers Made
and navigate to their profile page, and from there to their traditional splits page.
Then, extract their overall statistics from 2017-2018.

Save all of this data into a `pandas` DataFrame such that each record is a one of the five
players and columns correspond to the columns from the overall statistics tables.

**Note:** You will need to do some investigating into how the website works and how
to construct resource links that will get you what you want.

# Things to Know

A static website is a website that uses `http` to execute website transformations.
Consequently resource requests are made for everything and new pages/resources tend
to be represnted by links in anchor tags (`<a></a>`).

When scraping static websites, you essentially need to be able to do two
things:

1. Request a resource (such as someones facebook profile)
2. Explore and extract the data in that resource (profile name, brithday,
links to posts, etc.)


# Tools

One notable tool for scraping websites is the BeautifulSoup library.

Feel free to install this with 

    pip install beautifulsoup4

and import it with

    from bs4 import BeautifulSoup

BeautifulSoup is an html/xml exploration library that lets you easily parse
HTML documents. A great place to get HTML docs is the internet.

The following program requests and HTML page, then extracts all of its links.

```Python
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
html = requests.get(
    "https://en.wikipedia.org/wiki/Tor_(anonymity_network)",
    headers=headers
).text

soup = BeautifulSoup(html)

# Pretty print the HTML to see what it looks like
print(soup.prettify())

# Print the title of the page
print(soup.title.string)

# Find all anchor tags (links)
print(soup.find_all('a'))

```

Use the [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
to learn more.


# Masquerade

Notice in the above script that the request is equipped with a dictionary of headers that
notably includes a "User-Agent" header. This effectively tells the server that we are pinging
that we are a browser and not a script. Some servers know to reject requests that don't come from
browsers to avoid being scraped. We just add another line of code to trump that.

