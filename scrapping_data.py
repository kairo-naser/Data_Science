import requests # [cite: 13, 47]
from bs4 import BeautifulSoup # [cite: 21, 33, 50]
from urllib.request import urlopen # [cite: 32]

# --- 1. SETTING UP THE URL ---
# Specify the URL of the webpage you want to scrape[cite: 47].
# Example 1: Race results [cite: 39]
url_timing = "http://www.hubertiming.com/results/2017GPTR10K" 
# Example 2: Inspirational quotes [cite: 46]
url_quotes = "http://www.values.com/inspirational-quotes" 

# --- 2. ACCESSING CONTENT (USING URLOPEN) ---
# The urllib.request module is used to open URLs[cite: 34].
# Pass the URL to urlopen() to get the raw HTML of the page[cite: 38, 39].
html_raw = urlopen(url_timing)

# --- 3. ACCESSING CONTENT (USING REQUESTS) ---
# Alternatively, use the 'requests' library to send an HTTP request[cite: 13, 48].
# Save the response from the server in a response object called 'r'[cite: 48].
r = requests.get(url_quotes)
# r.content holds the raw HTML content, which is a 'string' type[cite: 49].

# --- 4. PARSING THE HTML ---
# Raw HTML is nested; we need a parser to create a tree structure[cite: 16, 17].
# BeautifulSoup takes raw HTML and breaks it into Python objects[cite: 44, 51].
# 'html5lib' is an advanced parser library used for this task[cite: 18, 54].
soup = BeautifulSoup(r.content, 'html5lib')

# prettify() gives a visual representation of the parse tree[cite: 55].
print(soup.prettify())

# --- 5. EXTRACTING BASIC INFORMATION ---
# The soup object allows you to extract the title of the page[cite: 56, 57].
title = soup.title
print(title)

# get_text() allows you to quickly print out the text of the webpage[cite: 58, 59].
text = soup.get_text()
print(text)

# --- 6. NAVIGATING AND SEARCHING THE TREE ---
# Use find_all() to extract specific HTML tags like 'a' for hyperlinks[cite: 62, 63].
all_links = soup.find_all("a") # [cite: 64]

# Attributes like 'href' provide additional info about elements[cite: 66].
# Use a for loop and get("href") to extract only the actual links[cite: 67, 68].
for link in all_links:
    print(link.get("href"))

# --- 7. SCRAPING TABLE DATA ---
# To print out table rows only, pass 'tr' into soup.find_all()[cite: 70, 71].
rows = soup.find_all('tr')

# Iterate through rows and find 'td' (table cell) tags[cite: 75, 76].
for row in rows:
    row_td = row.find_all('td')
    
    # --- 8. CLEANING DATA ---
    # Rows often have HTML tags embedded; we want to remove them[cite: 77, 78].
    # Pass the cells into BeautifulSoup and use get_text() to clean it[cite: 80, 81].
    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    print(cleantext)