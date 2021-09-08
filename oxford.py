from urllib.parse import urljoin
from random import randint
from time import sleep
from auxiliaryfuncs import make_soup

def get_oxford_volumes_links(soup):
    start_url = 'https://academic.oup.com/'
    all_urls = []
    for name in soup.find_all('div', attrs={'class':'customLink'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls

def get_oxford_paper_links(soup):
    start_url = 'https://academic.oup.com/'
    all_urls = []
    for name in soup.find_all('h5', attrs={'class':'customLink item-title'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls

def get_info_oxford(soup):

    paper = {}

    paper["journal"] = 'Oxford'

    paper['citation'] = []
    try:
        title = soup.find('h1', attrs={'class':'wi-article-title article-title-main'}).text.replace("\n","").replace("\r","")
        authors = [ a.text for a in soup.findAll('a', attrs={'class':'linked-name js-linked-name-trigger'})]
        journal = soup.find('div', attrs={'class':'ww-citation-primary'}).text
        citation = (title + '. ' + ', '.join(authors) + '.' + journal).lstrip()
        paper['citation'].append(citation)
    except:
        paper['citation'].append('NA')
        print('cannot get paper info')

    # get info in abstract
    paper['abstract'] = []
    paper['data'] = []
    try:
        long_abstract_string = soup.find('section', attrs={'class':'abstract'}).text
        list_abstract_availability = long_abstract_string.split("Availability")
        if len(list_abstract_availability) == 1:
            paper['abstract'].append(list_abstract_availability)
            paper['data'].append('NA')
        else:
            paper['abstract'].append(list_abstract_availability[0])
            paper['data'].append(list_abstract_availability[1])
    except:
        paper['abstract'].append('NA')
        paper['data'].append('NA')
        print('cannot get paper abstract info')

    return paper

def scrap_journal_oxford(journal, issue,f4):

    # get volumes
    volume_soup = make_soup("https://academic.oup.com/%s/issue-archive/%s" % (journal, issue))
    print("https://academic.oup.com/%s/issue-archive/%s" % (journal, issue))
    sleep(randint(10,20))
    links = get_oxford_volumes_links(volume_soup)

    if len(links) == 0:
        return print('this issue does not exist')

    # get papers
    for volume in links:
        papers_soup = make_soup(volume)
        sleep(randint(10,20))
        paper_links = get_oxford_paper_links(papers_soup)
        # get info from each paper
        for paper in paper_links:
            print(paper)
            paper_soup = make_soup(paper)
            sleep(randint(10,20))
            paper_info = get_info_oxford(paper_soup)
            f4.writelines('{}@{}@'.format(k,v) for k, v in paper_info.items())
            f4.write('\n')
            sleep(randint(10,20)) 
