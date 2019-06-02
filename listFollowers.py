from bs4 import BeautifulSoup

# HTML file which you have saved from https://www.instagram.com/<your_username>/followers/
# You must log in, on your browser
curDate = "02-06-2019"

fileName = 'data/Insta-followers-' + curDate

# All your followers list will be saved in ./data/followers-<curData> file
outputFileName = "data/followers-"+curDate

followers_file = open(outputFileName,"w+")

with open(fileName) as fp:
    # Created Beautiful Soup object which parses HTML file
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

# resultSet = <bs4-Object>("<tag-name>", [params..])
resultSet = soup.find_all("a", class_ = className)

# For loop iterates all users who are following you
for x in resultSet:
    # Uncomment following line to debug
    # print(x)
    # x.text contains user name who follows you
    followers_file.write(x.text+'\n')

# All your current followers will be stored in a file.
# after few days you can once again run the script find out missing names in the new file
# which were there earlier.

followers_file.close()