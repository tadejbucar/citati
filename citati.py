import urllib
from BeautifulSoup import BeautifulSoup

url='http://quotes.yourdictionary.com/theme/marriage/'
u1=urllib.urlopen(url).read()
soup = BeautifulSoup(u1)
citati=soup.findAll('p',attrs={'class': 'quoteContent'})

for x in citati:
    print x.text