from ploOne import scrap_journal_PLOS

## PLOSONE

# extract by volume and issue
plosone_journals = ["plosntds", "plosbiology","ploscompbiol","plosgenetics","plosmedicine"]
plosone_journal_abrev = ["pntd","pbio","pcbi","pgen","pmed"]
PLOS_volumes = list(range(1,20))
PLOS_issues = list(range(1,13))

# extract papers by page
plosone_bio_med = ["https://journals.plos.org/plosone/browse/biology_and_life_sciences?resultView=list&page=",
                   "https://journals.plos.org/plosone/browse/medicine_and_health_sciences?resultView=list&page="]
plosone_comp_fis = ["https://journals.plos.org/plosone/browse/computer_and_information_sciences?resultView=list&page=",
                    "https://journals.plos.org/plosone/browse/physical_sciences?resultView=list&page="]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # plos journals
    f7 = open('PlosOne.txt','w')
    for journal, abrev in zip(plosone_journals, plosone_journal_abrev):
        for volume in PLOS_volumes:
            for issue in PLOS_issues:
                if volume < 10 and issue < 10:
                    link = "https://journals.plos.org/%s/issue?id=10.1371/issue.%s.v0%s.i0%s#Research_Article" %(journal,abrev,volume,issue)
                elif volume < 10 and issue >= 10:
                    link = "https://journals.plos.org/%s/issue?id=10.1371/issue.%s.v0%s.i%s#Research_Article" %(journal,abrev,volume,issue)
                elif volume >= 10 and issue < 10:
                    link = "https://journals.plos.org/%s/issue?id=10.1371/issue.%s.v%s.i0%s#Research_Article" %(journal,abrev,volume,issue)
                elif volume >= 10 and issue >= 10:
                    link = "https://journals.plos.org/%s/issue?id=10.1371/issue.%s.v%s.i%s#Research_Article" %(journal,abrev,volume,issue)

                plos_listdict = scrap_journal_PLOS(link,f7)

    # plosOne

    for journal in plosone_bio_med:
        for page in biol_med:
            url = journal+ page
            print(url)
            plosOne_listdict = scrap_journal_PLOS(url,f7)


    for journal in plosone_comp_fis:
        for page in comp_fis:
            url = journal+ page
            print(url)
            plosOne_listdict = scrap_journal_PLOS(url,f7)

    f7.close()
