# Scraping a website:
# 1. Use API
# 2. HTML web Scrapping using some tool like bs4 (beautifulsoup)


# Requirements
# pip install requests
# pip install bs4
# pip install html5lib
""" 
<form action="result.php" target="_blank" method="post">
<input type="text" name="regno">
<input type="text" name="ucap_text" id="CaptchaInput" class="form-control" required="">
</form>
 """

import requests

from bs4 import BeautifulSoup, Tag

url = "http://gpamravati.ac.in/result"


# Step 1: Get the HTML

r = requests.get(url)

htmlcontent = r.content
# print(htmlcontent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)


# Step 3: HTML tree Traversal
title = soup.title
print(title.string)


# Commonly used type of objects:

# 1. Tag
# 2. Navigable String
# 3. BeautifulString
# 4. Comment


# get all td of the page
paras = soup.find_all('td')


captcha_box = soup.find('td', {"id": "CaptchaDiv"})

print(captcha_box)


# Get Text From ELements:
captcha_text = captcha_box.get_text()

print(captcha_text)
