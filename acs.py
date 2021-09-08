from urllib.parse import urljoin
from random import randint
from time import sleep
from auxiliaryfuncs import make_soup


def get_ACS_issue_links(soup):
    start_url = 'https://pubs.acs.org/'
    all_urls = []
    for name in soup.find_all('div', attrs={'class':'loi__cover col-lg-3 col-md-4 col-sm-3 col-xs-12'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls

def get_ACS_paper_links(soup):
    start_url = 'https://pubs.acs.org/'
    all_urls = []
    for name in soup.find_all('h5', attrs={'class':'issue-item_title'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls

def get_info_ACS(soup):

    paper = {}

    paper["journal"] = 'ACS'

    paper['citation'] =[]
    try:
        # paper info
        title = soup.find('h1', attrs={'class':'article_header-title'}).text
        authors = list(set([ i.text for i in soup.findAll('span', attrs={'class':'hlFld-ContribAuthor'})]))
        journal = soup.find('div', attrs={'class':'article_header-cite-this'}).text
        DOI = soup.find('div', attrs={'class':'article_header-doiurl'}).text
        citation = title + '. ' + ', '.join(authors) + '.' + journal.split('Cite this:')[1] + '. ' + DOI
        paper['citation'].append(citation)
    except:
        paper['citation'].append("NA")
        print('cannot get paper info')

    # get data availability info
    paper["data"] = []
    try:
        paper["data"].append(
            soup.find('div', attrs={'class':'article_supporting-info'}).text)
    except:
        paper["data"].append('NA')
        print('cannot get paper data availability info')

    # get abstract
    paper["abstract"] = []
    try:
        paper["abstract"].append(
            soup.find('div', attrs={'class':'article_abstract'}).text)
    except:
        paper["abstract"].append('NA')
        print('cannot get paper abstract')

    # get keywords
    paper["keywords"] = []
    try:
        for li in soup.find('ul',  attrs={'class':'rlist--inline loa'}).find_all('li'):
            for link in li.find_all('a'):
                paper["keywords"].append(link.text)
    except:
        paper["keywords"].append('NA')
        print('cannot get paper keywords')

    return paper

def scrap_journal_ACS(journal, issue, f2):

    print("https://pubs.acs.org/loi/%s/group/%s" % (journal, issue))

    # get issues links on each volume
    volume_soup = make_soup("https://pubs.acs.org/loi/%s/group/%s" % (journal, issue))
    sleep(randint(20,50))
    url_issue_list = get_ACS_issue_links(volume_soup)
    # get papers links each issue
    for url in url_issue_list:
        volume_soup = make_soup(url)
        sleep(randint(20,50))
        url_paper_list = get_ACS_paper_links(volume_soup)
        #get paper info
        for paper_url in url_paper_list:
            print(paper_url)
            paper_soup = make_soup(paper_url)
            sleep(randint(20,50))
            paper = get_info_ACS(paper_soup)
            f2.writelines('{}@{}@'.format(k,v) for k, v in paper.items())
            f2.write('\n')
            sleep(randint(20,50))
