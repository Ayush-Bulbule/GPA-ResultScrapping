# Python Automation Script to get Result of all student from college website.
import requests
import sys
from requests.structures import CaseInsensitiveDict

from bs4 import BeautifulSoup


url = 'https://www.gpamravati.ac.in/result/result.php'


# #Step 1: Getting the HTML

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"


# Function to reuse code
def getResult(i):

    # To create RollNo
    if i < 10:
        data = 'regno=19EC50'+str(i)+'&cap_text=1223&ucap_text=1223'
        # print(data)
    else:
        data = 'regno=19EC5'+str(i)+'&cap_text=1223&ucap_text=1223'
        # print(data)

    # Creating request
    r = requests.post(url, headers=headers, data=data)

    result_html = r.content

    # Step 2: Parse the HTML
    soup = BeautifulSoup(result_html, 'html.parser')

    td_tags = soup.find_all('td')
    font_tags = soup.find_all('font')

    if font_tags.__len__() < 100:
        return

    name = td_tags[17].text
    roll_no = font_tags[3].text
    sub1 = font_tags[5].text
    tot_sub1 = int(font_tags[16].text)
    obt_sub1 = int(font_tags[17].text)
    sub2 = font_tags[20].text
    tot_sub2 = int(font_tags[31].text)
    obt_sub2 = int(font_tags[32].text)
    sub3 = font_tags[35].text
    tot_sub3 = int(font_tags[46].text)
    obt_sub3 = int(font_tags[47].text)
    sub4 = font_tags[50].text
    tot_sub4 = int(font_tags[61].text)
    obt_sub4 = int(font_tags[62].text)
    sub5 = font_tags[65].text
    tot_sub5 = int(font_tags[76].text)
    obt_sub5 = int(font_tags[77].text)
    sub6 = font_tags[80].text
    tot_sub6 = int(font_tags[91].text)
    obt_sub6 = int(font_tags[92].text)
    sub7 = font_tags[95].text
    tot_sub7 = int(font_tags[106].text)
    obt_sub7 = int(font_tags[107].text)

    # print(soup)
    # Write to file
    sys.stdout = open('dataentc-shift2.txt', 'a')

    print("Sem VI Result:", roll_no.strip(), ' - ', name.strip())
    print("{:<3}/{:<3} - {}".format(obt_sub1, tot_sub1, str(sub1).strip()))
    print("{:<3}/{:<3} - {}".format(obt_sub2, tot_sub2, str(sub2).strip()))
    print("{:<3}/{:<3} - {}".format(obt_sub3, tot_sub3, str(sub3).strip()))
    print("{:<3}/{:<3} - {}".format(obt_sub4, tot_sub4, str(sub4).strip()))
    print("{:<3}/{:<3} - {}".format(obt_sub5, tot_sub5, str(sub5).strip()))
    print("{:<3}/{:<3} - {}".format(obt_sub6, tot_sub6, str(sub6).strip()))
    print("{:<3}/{:<3} - {}".format(obt_sub7, tot_sub7, str(sub7).strip()))

    obt_total = obt_sub1+obt_sub2+obt_sub3+obt_sub4+obt_sub5+obt_sub6+obt_sub7
    total = tot_sub1+tot_sub2+tot_sub3+tot_sub4+tot_sub5+tot_sub6+tot_sub7

    persentage = (obt_total*100)/total
    persentage = round(persentage, 4)

    print("Total : ", total)
    print("Total Obtained: ", obt_total)
    print("Persentage: ", persentage)
    print("-"*50)
    ('\n\n')


for i in range(1, 69):
    getResult(i)
print("\n\n This is automated data generation from official site: gpamravati.ac.in/result by Ayush Bulbule")
