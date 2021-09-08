from urllib.parse import urljoin
from random import randint
from time import sleep
from auxiliaryfuncs import make_soup

def get_papers_PLOS(soup):
    start_url = 'https://journals.plos.org/'
    paper_links = []
    for part in soup.findAll('h3', attrs={'class':'item--article-title'}):
        for a in part.findAll('a'):
            url_joined = urljoin(start_url, a['href'])
            paper_links.append(url_joined)
    return paper_links

def get_paper_info_PLOS(soup):

    paper = {}

    paper["journal"] = 'PlosOne'

    paper['citation'] = []
    try:
        citation = soup.find('div', attrs={'class':'articleinfo'}).text.split('Editor')[0]
        paper['citation'].append(citation)
    except:
        paper['citation'].append('NA')
        print('cannot get paper info')

    paper['abstract'] = []
    try:
        abstract = soup.find('div', attrs={'class':'abstract toc-section abstract-type-'}).text
        paper['abstract'].append(abstract)
    except:
        paper['abstract'].append('NA')
        print('cannot get paper abstract info')

    paper['keywords'] = []
    try:
        keywords = [a.text for a in soup.findAll('a', attrs={'class':"taxo-term"})]
        paper['keywords'].append(keywords)
    except:
        paper['keywords'].append('NA')
        print('cannot get paper keywords')

    paper['data'] = []
    try:
        data = soup.find('div', attrs={'class':'articleinfo'}).text.split('Data Availability:')
        if len(data) > 1 :
            data[1].split('Funding')[0]
            paper['data'].append(data)
        else:
            print('cannot get data info')
            paper['data'].append('NA')
    except:
        paper['data'].append('NA')
        print('cannot get data info')

    paper['code'] = []
    try:
        if "github" in soup.text or "GitHub" in soup.text:
            subs = 'github'
            soup_list = soup.text.split(' ')
            link = [i for i in soup_list if subs in i]
            paper['code'].append(link)
        elif "GitLab" in soup.text or "gitlab" in soup.text:
            subs = 'github'
            soup_list = soup.text.split(' ')
            link = [i for i in soup_list if subs in i]
            paper['code'].append(link)
    except:
        paper['code'].append('NA')
        print('cannot get paper code')

    return paper


def scrap_journal_PLOS(link,f7):
    print(link)
    page_soup = make_soup(link)
    sleep(randint(10,20))

    paper_links = get_papers_PLOS(page_soup)

    if len(paper_links) > 1:

        for paper in paper_links:
            print(paper)
            paper_soup = make_soup(paper)
            sleep(randint(10,20))
            paper_dict = get_paper_info_PLOS(paper_soup)
            f7.writelines('{}@{}@'.format(k,v) for k, v in paper_dict.items())
            f7.write('\n')
            sleep(randint(10,20))
