from futSci import scrap_journal_FS

## Future Science (bio and fmc are not open access, we could only get title and abstract)

future_science_journals = ["bio","fmc", "btn","fdd","fsoa"]
volume_bio = list(range(1,14+1))
issue_bio = list(range(1,25+1))

volume_fmc = list(range(1,14+1))
issue_fmc = list(range(1,24+1))

volume_tbn = list(range(27,72+1))
issue_btn = list(range(1,7+1))

volume_fdd = list(range(1,4+1))
issue_fdd = ['1','1s','2','2s']

volume_fsoa = list(range(1,8+1))
issue_fsoa = list(range(1,11+1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Future Science
    f6 = open('FutureScience_fmc.txt','w')
    for volume in volume_fmc:
        for issue in issue_fmc:
            fsoa_dicts = scrap_journal_FS('fmc',volume,issue,f6)

    #for volume in volume_fdd:
    #    for issue in issue_fdd:
    #        fdd_dicts = scrap_journal_FS('fdd',volume,issue,f6)

    #for volume in volume_tbn:
    #    for issue in issue_btn:
    #        btn_dicts = scrap_journal_FS('btn',volume,issue,f6)
    f6.close()
