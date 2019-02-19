# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# import the scraperwiki library - which we use to scrape webpages
import scraperwiki
import lxml.html
#
print("hello")
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
print(html)
# created a variable called html which grabs the web address and then prints it
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print(root.cssselect("a"))
print(root.cssselect("body style"))
variablelistofmatches = root.cssselect("a")
for match in variablelistofmatches:
  print(match)
pint(lxml.html.twostring(match))
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
