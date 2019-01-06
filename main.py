import requests
from bs4 import BeautifulSoup

def  GetNextLink(content):
    for tag in content.find_all('a'):
        if 'Next' in tag.text:
            return tag.attrs['href']
    return None


def downloadChapters(link):
    print(link)
    site = requests.get(link)
    site.raise_for_status()
    soup = BeautifulSoup(site.content)
    content = soup.select('.entry-content')[0]
    [d.extract() for d in content.findAll('div')]
    next_link = GetNextLink(content)
    [d.extract() for d in content.findAll('a')]
    with open('book.txt', 'ab') as file:
        file.write("\n\n".encode('utf8'))
        file.write(soup.select('.entry-title')[0].text.encode('utf8'))
        file.write("\n\n".encode('utf8'))
        file.write(content.getText().encode('utf8'))
    if next_link is not None:
        downloadChapters(next_link)
    else:
        return


if __name__ == "__main__":
    downloadChapters('https://www.parahumans.net/2017/09/11/daybreak-1-1/')