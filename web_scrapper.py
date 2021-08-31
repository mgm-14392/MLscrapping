from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
from random import randint
from time import sleep
import requests
import csv

# nature abreviation of journals
nature_journals = [ 'natmachintell', 'aps','biopharmdeal','bcj','bjc','cgt','cddis','celldisc','cmi','commschem','commseng','commsmed',
                  'cdd','cddiscovery','cr','commsbio','commsphys','emm','ejhg','gt','gim','gene','hr','hgv',
                  'ijir','ijosup','ijo','ja','jhg','jhh','leu','labinvest','leusup','modpathol','nature','nataging',
                  'natcancer','natcatal','nchembio','natcomputsci','ng','natbiomedeng','natmetab','nmicrobiol','neuro',
                   'nphys','nrcardio','nrclinonc','nrd','nrendo',
                  'nrg','nrneph','nrn','nrurol','npp','npjparkd','nutd','natafrica','nbt','natcardiovascres',
                   'ncb','nchem','ncomms','natelectron','natfood',
                  'ni','nm','nmeth','nrc','natrevchem','nrdp','nrgastro','nri','nrmp','nrm','nrneurol',
                   'natrevphys','nrrheum','nsmb','natsynth','npjamd','npjbcancer','npjdigitalmed','npjgenmed','npjqi',
                   'npjregenmed','npjscifood','npjsba','npjvaccines','onc','oncsis','tpj','pcan',
                   'sdata','sigtrans'
                  ]

# chemical_information_modeling volumes
jcim = ['d2020.y2021', 'd2020.y2020', 'd2010.y2019', 'd2010.y2018', 'd2010.y2017', 'd2010.y2016', 'd2010.y2015',
        'd2010.y2014', 'd2010.y2013', 'd2010.y2012', 'd2010.y2011', 'd2010.y2010', 'd2000.y2009', 'd2000.y2008',
       'd2000.y2007','d2000.y2006','d2000.y2005','d2000.y2004','d2000.y2003','d2000.y2002','d2000.y2001',
        'd2000.y2000','d1990.y1999','d1990.y1998','d1990.y1997','d1990.y1996','d1990.y1995','d1990.y1994',
        'd1990.y1993','d1990.y1992','d1990.y1991','d1990.y1990','d1980.y1989','d1980.y1988',
       'd1980.y1987','d1980.y1986','d1980.y1985','d1980.y1984','d1980.y1983','d1980.y1982',
        'd1980.y1981','d1980.y1980','d1970.y1979','d1970.y1978','d1970.y1977','d1970.y1976','d1970.y1975',
        'd1970.y1974','d1970.y1973','d1970.y1972','d1970.y1971','d1970.y1970','d1960.y1969',
       'd1960.y1968','d1960.y1967','d1960.y1966','d1960.y1965','d1960.y1964','d1960.y1963','d1960.y1962',
        'd1960.y1961','d1960.y1960']


def make_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

# Nature
def get_last_page_nature(soup):
    pages = soup.findAll('li', attrs={'class':'c-pagination__item'})
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
    paper_keywords = {}
    paper_data_availability = {}
    paper_code_availability = {}
    paper_abstract = {}
    
    try:
        # get paper citation 
        citation = soup.find('p', attrs={'class':'c-bibliographic-information__citation'}).text
    except:
        citation = 'NA'
        print('cannot get paper info')

    # get data availability info
    paper_data_availability[citation] = []   
    try:
        paper_data_availability[citation].append(
            soup.find('section', attrs={'data-title':'Data availability'}).text)
    except:
        paper_data_availability[citation].append('NA')
        print('cannot get data availability into')
    
    # get code availability info
    paper_code_availability[citation] = []
    try:
        paper_code_availability[citation].append(
            soup.find('section', attrs={'data-title':'Code availability'}).text)
    except:
        paper_code_availability[citation].append('NA')
        print('cannot get code availability into')
    
    # get abstract
    paper_abstract[citation] = []
    try: 
        paper_abstract[citation].append(
            soup.find('div', attrs={'class':'c-article-section__content'}).text)
    except:
        paper_abstract[citation].append('NA')
        print('cannot get paper abstract')
    
    # start dict for jeywords
    paper_keywords[citation] = []
    # get subjects
    try:
        for li in soup.findAll('li',  attrs={'class':'c-article-subject-list__subject'}):
            for link in li.find_all('a'):
                #paper_keywords[citation].append(link.get('href'))
                paper_keywords[citation].append(link.text)
    except:
        paper_keywords[citation].append('NA')
        print('cannot get paper keywords')
               
    return paper_keywords, paper_data_availability, paper_code_availability, paper_abstract


def scrap_journal_nature(journal, article_type):
    
    csv_columns = ['Citation','Info']
    csvfile = open("Nature_MLpapers_info.txt", 'w')
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
     
    # get number of pages
    soup_page = make_soup("https://www.nature.com/%s/%s" % (journal, article_type))
    sleep(randint(2,10))
    
    # get links to all papers
    url_list = []
    for page in range(1, get_last_page_nature(soup_page)):
        initial_url = 'https://www.nature.com/%s/research-articles?searchType=journalSearch&sort=PubDate&page=' % journal
        url_page = initial_url + str(page)
        soup_links = make_soup(url_page)
        sleep(randint(2,10))
        links = get_links_nature(soup_links)
        [url_list.append(i) for i in links]
        
    dict_data = []
    # get info of each paper
    for paper in url_list:
        soup_paper = make_soup(paper)
        sleep(randint(2,10))
        paper_keywords, paper_data_availability, paper_code_availability, paper_abstract = get_info_nature(soup_paper)
        dict_data.append(paper_keywords)
        dict_data.append(paper_data_availability)
        dict_data.append(paper_code_availability)
        dict_data.append(paper_abstract)
   
    for data in dict_data:
        writer.writerow(data)

        
# jcim
def get_jcim_issue_links(soup):
    start_url = 'https://pubs.acs.org/'
    all_urls = []
    for name in issue_soup.find_all('div', attrs={'class':'loi__cover col-lg-3 col-md-4 col-sm-3 col-xs-12'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls

def get_jcim_paper_links(soup):
    start_url = 'https://pubs.acs.org/'
    all_urls = []
    for name in issue_soup.find_all('h5', attrs={'class':'issue-item_title'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls 

def get_info_jcim(soup):
    paper_keywords = {}
    paper_data_availability = {}
    paper_abstract = {}
       
    try: 
        # paper info
        title = soup.find('h1', attrs={'class':'article_header-title'}).text
        authors = list(set([ i.text for i in soup.findAll('span', attrs={'class':'hlFld-ContribAuthor'})]))
        journal = soup.find('div', attrs={'class':'article_header-cite-this'}).text
        DOI = soup.find('div', attrs={'class':'article_header-doiurl'}).text
        citation = title + '. ' + ', '.join(authors) + '.' + journal.split('Cite this:')[1] + '. ' + DOI
    except:
        citation = 'NA'
        print('cannot get paper info')
    
    # get data availability info
    paper_data_availability[citation] = []
    try:          
        paper_data_availability[citation].append(
            soup.find('div', attrs={'class':'article_supporting-info'}).text)
    except:
        paper_data_availability[citation].append('NA')
        print('cannot get paper data availability info')
    
    # get abstract
    paper_abstract[citation] = []
    try:
        paper_abstract[citation].append(
            soup.find('div', attrs={'class':'article_abstract'}).text)
    except:
        paper_abstract[citation].append('NA')
        print('cannot get paper abstract')
    
    # get keywords
    paper_keywords[citation] = []
    try:
        for li in soup.find('ul',  attrs={'class':'rlist--inline loa'}).find_all('li'):
            for link in li.find_all('a'):
                paper_keywords[citation].append(link.text)
    except:
        paper_keywords[citation].append('NA')
        print('cannot get paper keywords')
                  
    return paper_keywords, paper_data_availability, paper_abstract

def scrap_journal_jcim(volume):
    
    csv_columns = ['Citation','Info']
    csvfile = open("JCIM_MLpapers_info.txt", 'w')
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    
    url_issue_list = []
    # get issues links on each volume
    volume_soup = make_soup("https://pubs.acs.org/loi/jcisd8/group/%s" % volume)
    sleep(randint(2,10))
    issue_links = get_jcim_issue_links(volume_soup)
    # list with the urls from each issue
    [url_issue_list.append(i) for i in issue_links]
    
    url_paper_list = []
    # get papers links each issue
    for url in url_issue_list:
        volume_soup = make_soup(url)
        sleep(randint(2,10))
        paper_links = get_jcim_paper_links(volume_soup)
        # list with the urls from each paper
        [url_paper_list.append(i) for i in issue_links]
    
    dict_data = []
    #get paper info
    for paper_url in url_paper_list:
        paper_soup = make_soup(paper_url)
        sleep(randint(2,10))
        paper_keywords, paper_data_availability, paper_abstract = get_info_jcim(paper_soup)
        dict_data.append(paper_keywords)
        dict_data.append(paper_data_availability)
        dict_data.append(paper_abstract)
        
    for data in dict_data:
        writer.writerow(data)

# chemoinformatics

def get_last_page_chemoinfo(soup):
    pages = soup.findAll('li', attrs={'class':'c-pagination__item'})
    for i in range(0,len(pages)):
        pages_list = list(pages[i].strings)
        lst = list(map(str.strip, pages_list))
        if 'page' in lst or'…' in lst:
            continue
        if 'Next' not in lst:
            num = int(lst[1])
    return int(num)

def get_links_chemoinfo(soup):
    start_url = 'https://jcheminf.biomedcentral.com/'
    all_urls = []
    for name in soup.find_all('h3', attrs={'class':'c-listing__title'}):
        for link in name.find_all('a'):
            url_joined = urljoin(start_url, link.get('href'))
            all_urls.append(url_joined)
    return all_urls

def get_info_chemoinfo(soup):
    paper_keywords = {}
    paper_data_availability = {}
    paper_abstract = {}
    
    try:
        # get paper citation 
        citation = soup.find('p', attrs={'class':'c-bibliographic-information__citation'}).text
    except:
        citation = 'NA'
        print('cannot get paper info')
        
    # get data and materials availability info
    paper_data_availability[citation] = []
    try:
        paper_data_availability[citation].append(
            soup.find('section', attrs={'data-title':'Availability of data and materials'}).text)
    except:
        paper_data_availability[citation].append('NA')
        print('cannot get code availability into')
    
    # get abstract
    paper_abstract[citation] = []
    try: 
        paper_abstract[citation].append(
            soup.find('div', attrs={'class':'c-article-section__content'}).text)
    except:
        paper_abstract[citation].append('NA')
        print('cannot get paper abstract')
    
    # start dict for jeywords
    paper_keywords[citation] = []
    # get subjects
    try:
        for li in soup.findAll('li',  attrs={'class':'c-article-subject-list__subject'}):
            for link in li.find_all('span'):
                paper_keywords[citation].append(link.text)
    except:
        paper_keywords[citation].append('NA')
        print('cannot get paper keywords')
               
    return paper_keywords, paper_data_availability, paper_abstract

def scrap_journal_chemoinfo():
    
    csv_columns = ['Citation','Info']
    csvfile = open("ChemoInfo_MLpapers_info.txt", 'w')
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    
    #get number of pages
    soup_page = make_soup("https://jcheminf.biomedcentral.com/articles?searchType=journalSearch&sort=PubDate&page=1")
    sleep(randint(2,10))
    
    # get links to all papers
    url_list = []
    for page in range(1, get_last_page_chemoinfo(soup_page)):
        initial_url = 'https://jcheminf.biomedcentral.com/articles?searchType=journalSearch&sort=PubDate&page='
        url_page = initial_url + str(page)
        soup_links = make_soup(url_page)
        sleep(randint(2,10))
        links = get_links_chemoinfo(soup_links)
        [url_list.append(i) for i in links]
    
    dict_data = []
    # extract info from papers
    for paper in url_list:
        paper_soup = make_soup(paper)
        sleep(randint(2,10))
        paper_keywords, paper_data_availability, paper_abstract = get_info_chemoinfo(paper_soup)
        dict_data.append(paper_keywords)
        dict_data.append(paper_data_availability)
        dict_data.append(paper_abstract)   

    for data in dict_data:
        writer.writerow(data)     
        
        
if __name__ == '__main__':
    # scrape nature
    for journal in nature_journals:
        print(journal)
        scrap_journal_nature(journal, "research-articles")
        scrap_journal_nature(journal, "reviews-and-analysis")
        
    # scrap jcim
    for volume in jcim:
        scrap_journal_jcim(volume)
    
    #scrape chemoinfo
    scrap_journal_chemoinfo()