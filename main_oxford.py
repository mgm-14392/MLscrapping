from oxford import scrap_journal_oxford

# Oxford
oxford_issues = [ '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
                  '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                  '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021' ]

oxford_journals = [
    'abbs', 'bioscience','ajcp', 'ajhp', 'ajh', 'bioinformatics', 'bioinformaticsadvances', 'bioscience',
    'bbb', 'biostatistics', 'bib', 'cardiovascres', 'chemse', 'clinchem', 'comjnl', 'database', 'dnaresearch', 'endo',
    'ehjcimaging', 'ehjcvp', 'ehjdh', 'g3journal', 'genetics', 'insilicoplants', 'ib', 'iob', 'icb', 'iwc', 'ijpp', 'jacamr',
    'jamiaopen', 'jamia', 'jb', 'jbi', 'jid', 'jmcb', 'jpp', 'imammb', 'narcancer', 'nargab', 'nar', 'synbio', 'sysbio']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Oxford
    f4 = open('Oxford.txt','w')
    for journal in oxford_journals:
        print(journal)
        for issue in oxford_issues:
            oxford_list_dicts = scrap_journal_oxford(journal,issue,f4)
    f4.close()

