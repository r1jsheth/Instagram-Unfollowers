## **Instagram Unfollowers***

This is one of the easiest way to find your **unfollowers** and **new followers**! I have created a simple web-scraper using [BeautifulSoup](<https://pypi.org/project/beautifulsoup4/>).

Don't worry this app **doesn't require** you to sign in to any 3rd party where you need to sign in. Simple follow my instructions and you will be ready to go.

**Dependencies**

Install BeautifulSoup (bs4)

`sudo pip3 install beautifulsoup4 `

Or else you can simple follow instructions [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup).

**Instructions**

1. Install bs4. The script solely run on bs4 or BeautifulSoup, so you must have it installed on your python3.

2. Clone this repository using following command.

   `git clone https://github.com/rhetoricalraj/Instagram-Unfollowers`

3. Log in to Instagram using your PC and go to [your account](https://www.instagram.com/'your_username'/followers/) page. You can see all your followers, scroll down until all your followers are loaded.

4. Save this page in `.html` format using `CTRL` `+` `S` to the directory where this repository is cloned.

5. Now go again to the same followers web-page and **right-click** on any random your follower's username and go to **inspect element**.

6. This is the most important step. Copy the class name for the tag `<a class='className' href='link here'>`. This class name is going to be useful in next step.

7. Open `listFollowers.py`  and find `className` variable in the python code. Paste the name which you copied earlier from page. Also change value of `curDate` accordingly. So that you can identify later.

8. That's it. Run your python file using  following command.

   `python3 listFollowers.py`
   
   This script will create a file in `data` directory named `followers` + `curDate`. Which will store your all current followers as of today.
   
9. Now come back after few days and run this `listFollowers.py` once again. You can run `unfollowers.sh` which will identify the difference between **previous followers list** file and **current followers list** file. Ouput file will be generated.