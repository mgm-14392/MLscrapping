from urllib.parse import urljoin
from random import randint
from time import sleep
from auxiliaryfuncs import make_soup
import re

def get_last_page_BMC(soup):
    pages = soup.findAll('li', attrs={'class':'c-pagination__item'})
    for i in range(0,len(pages)):
        pages_list = list(pages[i].strings)
        lst = list(map(str.strip, pages_list))
        if 'page' in lst or'…' in lst:
            continue
        if 'Next' not in lst:
            num = int(lst[1])
    return int(num)

def get_links_BMC(soup, journal):
    start_url = 'https://%s/' % journal
    all_urls = []
    for name in soup.find_all('h3', attrs={'class':'c-listing__title'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls

def get_info_BMC(soup):

    paper = {}

    paper["journal"] = 'BMC'

    paper['citation'] = []
    try:
        # get paper citation
        citation = soup.find('p', attrs={'class':'c-bibliographic-information__citation'}).text
        paper['citation'].append(citation)
    except:
        paper['citation'].append('NA')
        print('cannot get paper info')

    # get data and materials availability info
    paper['data'] = []
    try:
        paper['data'].append(
            soup.find('section', attrs={'data-title':'Availability of data and materials'}).text)
    except AttributeError:
        try:
            pattern = re.compile(r'Availability of data and materials')
            for i in soup.findAll('h3', text=pattern):
                for sib in i.next_siblings:
                    if sib.name == 'p':
                        paper['data'].append(sib.text)
                    else:
                        paper['data'].append('NA')
                        print('cannot get code availability into')  
        except:
            paper['data'].append('NA')
            print('cannot get code availability into')

    # get abstract
    paper['abstract'] = []
    try:
        paper['abstract'].append(
            soup.find('div', attrs={'class':'c-article-section__content'}).text)
    except:
        paper['abstract'].append('NA')
        print('cannot get paper abstract')

    # start dict for jeywords
    paper['keywords'] = []
    # get subjects
    try:
        for li in soup.findAll('li',  attrs={'class':'c-article-subject-list__subject'}):
            for link in li.find_all('span'):
                paper['keywords'].append(link.text)
    except:
        paper['keywords'].append('NA')
        print('cannot get paper keywords')

    return paper

def scrap_journal_BMC(journal,f3):

    #get number of pages
    soup_page = make_soup("https://%s/articles?searchType=journalSearch&sort=PubDate&page=1" % journal)
    sleep(randint(10,20))
    print(get_last_page_BMC(soup_page))

    # get links to all papers
    for page in range(1, get_last_page_BMC(soup_page)+1):
        initial_url = 'https://%s/articles?searchType=journalSearch&sort=PubDate&page=%d' % (journal, page)
        print(initial_url)
        url_page = initial_url + str(page)
        soup_links = make_soup(url_page)
        sleep(randint(10,20))
        url_list = get_links_BMC(soup_links, journal)
        # extract info from papers
        for paper in url_list:
            print(paper)
            paper_soup = make_soup(paper)
            sleep(randint(10,20))
            paper = get_info_BMC(paper_soup)
            f3.writelines('{}@{}@'.format(k,v) for k, v in paper.items())
            f3.write('\n')
            sleep(randint(10,20))
