##### Use http://collemc.people.si.umich.edu/data/bshw3StarterFile.html  as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
#

import requests
import re
from bs4 import BeautifulSoup

print ("\n working...... \n")

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

###### 1 ######

findword_student = soup.find_all(text = re.compile('student'))
for word in findword_student:
    amazingstudent = str(word).replace('student', 'AMAZING student')
    word.replace_with(amazingstudent)

###### 2 ######

for imglink in soup.findAll('iframe'):
	imglink['src'] = "/Users/jamesroeser/Desktop/206/PROJECT-3/HW3-StudentCopy/jp/JP.png"

###### 3 ######

for imglink in soup.findAll('img'):
	imglink['src'] = "/Users/jamesroeser/Desktop/206/PROJECT-3/HW3-StudentCopy/media/logo.png"

txtfile = open("HW3_bSoup_html.html", "w")


print(' creating html file...... ')
print('    (look for html file in project folder)')
txtfile.write(str(soup))
txtfile.close()
print('\nDONE\n')
