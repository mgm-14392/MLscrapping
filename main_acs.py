from acs import scrap_journal_ACS

# ACS issues dates
ACS_issues = ['d2020.y2021', 'd2020.y2020', 'd2010.y2019', 'd2010.y2018', 'd2010.y2017', 'd2010.y2016', 'd2010.y2015',
         'd2010.y2014', 'd2010.y2013', 'd2010.y2012', 'd2010.y2011', 'd2010.y2010', 'd2000.y2009', 'd2000.y2008',
         'd2000.y2007','d2000.y2006','d2000.y2005','d2000.y2004','d2000.y2003','d2000.y2002','d2000.y2001',
         'd2000.y2000','d1990.y1999','d1990.y1998','d1990.y1997','d1990.y1996','d1990.y1995','d1990.y1994',
         'd1990.y1993','d1990.y1992','d1990.y1991','d1990.y1990','d1980.y1989','d1980.y1988',
         'd1980.y1987','d1980.y1986','d1980.y1985','d1980.y1984','d1980.y1983','d1980.y1982',
         'd1980.y1981','d1980.y1980','d1970.y1979','d1970.y1978','d1970.y1977','d1970.y1976','d1970.y1975',
         'd1970.y1974','d1970.y1973','d1970.y1972','d1970.y1971','d1970.y1970','d1960.y1969',
         'd1960.y1968','d1960.y1967','d1960.y1966','d1960.y1965','d1960.y1964','d1960.y1963','d1960.y1962',
         'd1960.y1961','d1960.y1960']

#ACS journals does  include chemical_information_modeling issues
ACS_journals = list(
    {"jcisd8", "mpohbp", "jprobs", "jmcmar", "joceah", "jpccck", "jpcbfk", "jpcafh", "jnprdf", "jctcce", "iepra6",
     "jafcau", "ceaax", "acscii", "acbcct", "achsc5", "acncdm", "aidcbc", "amclct", "acsodf", "aptsfn", "bichaw",
     "bomaf6", "bcches", "jceaax"})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # ACS
    f2 = open('ACS.txt','w')
    for journal in ACS_journals:
        print(journal)
        for issue in ACS_issues:
            ACS_list_dicts = scrap_journal_ACS(journal,issue,f2)
    f2.close()

