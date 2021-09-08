from BMC import scrap_journal_BMC

#BiomedCentral
BMCjournals = [
    "alzres.biomedcentral.com","bmccancer.biomedcentral.com",
    "bmcmedgenet.biomedcentral.com","bmcmedgenomics.biomedcentral.com",
    "bmcneurosci.biomedcentral.com","bmcpharmacoltoxicol.biomedcentral.com",
    "breast-cancer-research.biomedcentral.com",
    "cancerandmetabolism.biomedcentral.com","cancerci.biomedcentral.com",
    "clinicalepigeneticsjournal.biomedcentral.com",
    "genesandnutrition.biomedcentral.com",
    "genomemedicine.biomedcentral.com",
    "humgenomics.biomedcentral.com",
    "jbiomedsci.biomedcentral.com",
    "jphcs.biomedcentral.com",
    "translational-medicine.biomedcentral.com",
    "molmed.biomedcentral.com",
    "tbiomed.biomedcentral.com",
    "bmcbiotechnol.biomedcentral.com",
    "bmcchem.biomedcentral.com",
    "jcheminf.biomedcentral.com",
    "bdataanalytics.biomedcentral.com",
    "jbioleng.biomedcentral.com",
    "almob.biomedcentral.com",
    "biodatamining.biomedcentral.com",
    "biolres.biomedcentral.com",
    "biologydirect.biomedcentral.com",
    "bmcbioinformatics.biomedcentral.com",
    "bmcbiol.biomedcentral.com",
    "bmcgenomdata.biomedcentral.com",
    "bmcgenomics.biomedcentral.com",
    "bmcmolcellbiol.biomedcentral.com",
    "cellandbioscience.biomedcentral.com",
    "genomebiology.biomedcentral.com",
    "bmcmedimaging.biomedcentral.com",
    "bmcmedinformdecismak.biomedcentral.com",
    "bmcmedicine.biomedcentral.com",
    "cancerimagingjournal.biomedcentral.com",
    "cmjournal.biomedcentral.com",
    "eurjmedres.biomedcentral.com",
    "ojrd.biomedcentral.com",
    "transmedcomms.biomedcentral.com"]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # BMC
    f3 = open('BMC.txt','w')
    for journal in BMCjournals:
        BMC_dict_list = scrap_journal_BMC(journal,f3)
    f3.close()

