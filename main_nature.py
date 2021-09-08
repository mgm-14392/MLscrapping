from nature import scrap_journal_nature

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Nature
    f = open('nature.txt','w')
    for journal in nature_journals:
        nature_dicts = scrap_journal_nature(journal, "research-articles", f)
    f.close()

