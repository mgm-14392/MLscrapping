from urllib.parse import urljoin
from random import randint
from time import sleep
from auxiliaryfuncs import make_soup

def get_papers_FS(soup):
    start_url = 'https://www.future-science.com/'
    paper_links = []
    for link in soup.findAll('h5', attrs={'class':'issue-item__title'}):
        for a in link.findAll('a'):
            url_joined = urljoin(start_url, a['href'])
            paper_links.append(url_joined)
    return paper_links

def get_papers_info_FS(soup):
    paper = {}

    paper["journal"] = 'FutureScience'

    paper['citation'] = []
    try:
        journal = soup.find('div', attrs={'class':'citation__top'}).text.split("\n")[1]
        title = soup.find('h1', attrs={'class':'citation__title'}).text
        names = ''
        for a in soup.findAll('a', attrs={'class':'author-name accordion-tabbed__control visible-x'}):
            names += a.text + ", "
        text = ''
        for a in soup.findAll('span', attrs={'class':'epub-section__item'}):
            text += a.text + ". "
        citation = names + ". " + title + ". " + journal + ". " + text
        paper['citation'].append(citation)
    except:
        paper['citation'].append('NA')
        print('cannot get paper info')

    paper['abstract'] = []
    try:
        abstract = soup.find('div', attrs={'class':'abstractSection abstractInFull'}).text
        paper['abstract'].append(abstract)
    except:
        paper['abstract'].append('NA')
        print('cannot get paper abstract info')

    paper['keywords'] = []
    try:
        keywords = []
        for all_t in soup.findAll('div', attrs={'id':'keywords'}):
            for a in all_t.findAll('a'):
                keywords.append(a.text)
        paper['keywords'].append(keywords)
    except:
        paper['keywords'].append('NA')
        print('cannot get paper keywords')

    paper['data'] = []
    try:
        if 'GitHub' in soup.text:
            paper['data'].append('GitHub repository mentioned, check paper')
        else:
            paper['data'].append('NA')
            print('cannot get paper data')
    except:
        paper['data'].append('NA')
        print('cannot get paper data')

    return paper

def scrap_journal_FS(journal,volume,issue,f6):
    # get papers
    initial_url = "https://www.future-science.com/toc/%s/%s/%s" %(journal,volume,issue)
    print(initial_url)
    papers_soup = make_soup(initial_url)
    sleep(randint(10,20))
    url_papers_list = get_papers_FS(papers_soup)

    for paper in url_papers_list:
        print(paper)
        paperi_soup = make_soup(paper)
        sleep(randint(10,20))
        paper_dir = get_papers_info_FS(paperi_soup)
        f6.writelines('{}@{}@'.format(k,v) for k, v in paper_dir.items())
        f6.write('\n')
        sleep(randint(10,20))
