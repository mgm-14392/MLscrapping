from urllib.parse import urljoin
from random import randint
from time import sleep
from auxiliaryfuncs import make_soup

def get_last_page_nature(soup):
    pages = soup.findAll('li', attrs={'class':'c-pagination__item'})
    if len(pages) == 0:
        return 1
    else:
        for i in range(0,len(pages)):
            pages_list = list(pages[i].strings)
            lst = list(map(str.strip, pages_list))
            if 'Next' in lst:
                continue
            if 'page' in lst and 'Previous' not in lst:
                num_idx = int(lst.index("page")) + 1
                num = lst[num_idx]
        return int(num)

def get_links_nature(soup):
    start_url = 'https://www.nature.com/'
    all_urls = []
    for name in soup.find_all('h3', attrs={'class':'c-card__title'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls

def get_info_nature(soup):
    paper = {}

    paper["journal"] = 'Nature'

    paper["citation"] = []
    try:
        # get paper citation
        citation = soup.find('p', attrs={'class':'c-bibliographic-information__citation'}).text
        paper["citation"].append(citation)
    except:
        paper["citation"].append("NA")
        print('cannot get paper info')

    # get data availability info
    paper["data"] = []
    try:
        paper["data"].append(
            soup.find('section', attrs={'data-title':'Data availability'}).text)
    except:
        paper["data"].append('NA')
        print('cannot get data availability info')

    # get code availability info
    paper["code"] = []
    try:
        paper["code"].append(
            soup.find('section', attrs={'data-title':'Code availability'}).text)
    except:
        paper["code"].append('NA')
        print('cannot get code availability info')

    # get abstract
    paper["abstract"] = []
    try:
        paper["abstract"].append(
            soup.find('div', attrs={'class':'c-article-section__content'}).text)
    except:
        paper["abstract"].append('NA')
        print('cannot get paper abstract')

    # start dict for jeywords
    paper["keywords"] = []
    # get subjects
    try:
        for li in soup.findAll('li',  attrs={'class':'c-article-subject-list__subject'}):
            for link in li.find_all('a'):
                paper["keywords"].append(link.text)
    except:
        paper["keywords"].append('NA')
        print('cannot get paper keywords')

    return paper


def scrap_journal_nature(journal, article_type, f):

    # get number of pages
    soup_page = make_soup("https://www.nature.com/%s/%s" % (journal, article_type))
    sleep(randint(10,20))

    # get links to all papers
    for page in range(1, get_last_page_nature(soup_page)+1):
        initial_url = 'https://www.nature.com/%s/research-articles?searchType=journalSearch&sort=PubDate&page=' % journal
        url_page = initial_url + str(page)
        soup_links = make_soup(url_page)
        sleep(randint(10,20))
        url_list = get_links_nature(soup_links)
        for paper in url_list:
            print(paper)
            soup_paper = make_soup(paper)
            sleep(randint(10,20))
            paper = get_info_nature(soup_paper)
            f.writelines('{}@{}@'.format(k,v) for k, v in paper.items())
            f.write('\n')
            sleep(randint(10,20))
