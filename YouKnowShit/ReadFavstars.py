import bs4

favstarsFile = 'C:\\Users\\JIANG\\Downloads\\favstars-mjyang-1461674723.html'
favstarsList = []
htmlfile = open(favstarsFile, 'r', encoding='UTF-8')
htmltext = htmlfile.read()
soup = bs4.BeautifulSoup(htmltext, "html.parser")
for actName in soup.select('span'):
    favstarsList.append(actName.string)