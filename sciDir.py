from urllib.parse import urljoin
from random import randint
from time import sleep
from auxiliaryfuncs import make_soup

def get_volumes_scidir(soup):
    list_vols = [i.text for i in soup.findAll("span", attrs={"class": "accordion-title js-accordion-title"})]
    last_vol = list_vols[0].split(' ')[-1]
    if '-' in last_vol:
        last_vol = last_vol.split('-')[1]
    try:
        first_vol = list_vols[len(list_vols)-1].split(' ')[-1].split('-')[0]
    except IndexError:
        first_vol = list_vols[len(list_vols)-1].split(' ')[-1]

    volumes = list(range(int(first_vol),int(last_vol)+1))
    return volumes # returns list with volumes for each journal

def get_paper_scidir(soup):
    start_url = 'https://www.sciencedirect.com/'
    paper_links = []
    for link in soup.findAll('a', attrs={'class':'anchor article-content-title u-margin-xs-top u-margin-s-bottom'}):
        url_joined = urljoin(start_url, link.get('href'))
        paper_links.append(url_joined)
    return paper_links

def get_info_scidir(soup):

    paper = {}

    paper["journal"] = 'SciDir'

    paper['citation'] = []
    try:
        journal = soup.find('div', attrs={'id':'publication'}).text
        title = soup.find('h1', attrs={'id':'screen-reader-main-title'}).text
        authors = ''
        for name in soup.findAll('a', attrs={'class':'author size-m workspace-trigger'}):
            authors += name.text + ' '
        DOI = soup.find('a', attrs={'class':'doi'}).get("href")
        citation = title + '. ' + authors + '. ' + journal + '. ' + DOI
        paper['citation'].append(citation)
    except:
        paper['citation'].append('NA')
        print('cannot get paper info')

    # get info in abstract
    paper['abstract'] = []
    paper['data'] = []
    try:
        abstract = soup.find('div', attrs={'class':'abstract author'}).text
        paper['abstract'].append(abstract)

        maybe_code = "availa"
        if "availa" in abstract:
            end = abstract.split('availa')[1]
            maybe_code += end
            paper['data'].append(maybe_code)

        maybe_code2 = "freely "
        if "freely" in abstract:
            end = abstract.split('freely')[1]
            maybe_code2 += end
            paper['data'].append(maybe_code2)

    except:
        paper['abstract'].append('NA')
        paper['data'].append('NA')
        print('cannot get paper abstract info')


    # get keywords
    paper['keywords'] = []
    try:
        for word in soup.findAll('div', attrs={'class':'keyword'}):
            paper['keywords'].append(word.text)
    except:
        paper['keywords'].append('NA')
        print('cannot get paper keywords')

    return paper

def scrap_scidir(journal,f5,num=10):

    issues = list(range(1,num+1))
    print(issues)

    #get volumes
    issues_url = "https://www.sciencedirect.com/journal/%s/issues"%journal
    print(issues_url)
    issues_soup = make_soup(issues_url)
    sleep(randint(10,20))
    volumes = get_volumes_scidir(issues_soup)

    # get papers links
    url_papers_list = set()
    for volume in volumes:
        for issue in issues:
            volumes_url = "https://www.sciencedirect.com/journal/%s/vol/%s/issue/%s" %(journal, volume, issue)
            print(volumes_url)
            issue_soup = make_soup(volumes_url)
            sleep(randint(10,20))
            paper_links = get_paper_scidir(issue_soup)
            [url_papers_list.add(i) for i in paper_links]

            for paper in url_papers_list:
                print(paper)
                paper_soup = make_soup(paper)
                sleep(randint(10,20))
                paper_dir = get_info_scidir(paper_soup)
                f5.writelines('{}@{}@'.format(k,v) for k, v in paper_dir.items())
                f5.write('\n')
                sleep(randint(10,20))

