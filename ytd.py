import pafy
import urllib
import urllib2

from bs4 import BeautifulSoup

print "Welcome to the YTD Search and Download Engine.."
query = raw_input("Please enter the search query here : ")
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser")
no = 0
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    v = pafy.new(str(vid['href'][9:20]))
    no = no + 1
    print "#" + str(no)
    print "ID : " + vid['href'][9:20]
    print "Title : " + v.title
    print "Uploader : " + v.author
    print "#################"
x = raw_input("You can paste the ID here : ")
v = pafy.new(str(x))
s = v.getbestaudio()
s.download()
print v.title + " is downloaded.."
