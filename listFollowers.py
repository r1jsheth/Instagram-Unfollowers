from bs4 import BeautifulSoup

fileName = 'Insta-followers-25-05-2019.html'

curDate = "25-05-2019"
outputFileName = "data/followers-"+curDate

followers_file = open(outputFileName,"w+")

with open(fileName) as fp:
    soup = BeautifulSoup(fp)

# Check the class name by clicking on inspect element.
# I am not sure if this name is static, as of today 25-05-2019 the name is mentioned below.
# You can find this by going to following link and right click on any of your follower's name and click
# "inspect element" option. Now you can see the class name.
# Simply copy it below and run the script.
# Webpage: https://www.instagram.com/<your_username>/followers/
# You must sign in on your PC

className = "FPmhX notranslate _0imsa "
# Here we are searching of all <a> elements with class name as className
# bs4 can do this beautifully and it stores in resultSet

resultSet = soup.find_all("a", class_ = className)

for x in resultSet:
    followers_file.write(x.text+'\n')

# all your current followers will be stored in a file.
# after few days you can once again run the script find out missing names in the new file
# which were there earlier.

followers_file.close()