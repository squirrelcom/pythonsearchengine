from bs4 import BeautifulSoup

def main():

    #open file
    fh = open("1.html", "r")


    #get title and text
    contents = fh.read()
    soup = BeautifulSoup(contents, 'html.parser')

    text = soup.find_all('p')

    
    #text = list(text)

    #print(type(text))

    i = 0

    for i in range(len(text)):
        text[i] = text[i].get_text()

    
    text = text.replace(u'\xa0', u'').split(" ")
    

    print(text)

    #change symbols to spaces

    

    #put data in index

    

    
