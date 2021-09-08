from sciDir import scrap_scidir

# Science direct

sci_dir_10 = [
    "current-opinion-in-systems-biology", "computational-toxicology", "chemical-physics-impact",
    "artificial-intelligence-in-the-life-sciences", 
    "biophysical-reports", "biochemistry-and-biophysics-reports",
    "biotechnology-notes", "chemical-data-collections",  "biotechnology-reports", "biosystems",
    "archives-of-biochemistry-and-biophysics",
    "gene-and-genome-editing", "food-chemistry-molecular-sciences", "data-in-brief",
    "european-journal-of-medicinal-chemistry-reports", "advances-in-cancer-biology-metastasis",
    "advances-in-medical-sciences",
    "computational-and-theoretical-chemistry", "chemical-physics", "biophysical-chemistry",
    "biochimica-et-biophysica-acta-bba-protein-structure-and-molecular-enzymology",
    "medicine-in-drug-discovery","journal-of-structural-biology-x","gene-x", "gene",
    "artificial-intelligence-in-medicine",
    "softwarex", "results-in-chemistry","progress-in-biophysics-and-molecular-biology","gene-reports",
     "human-genetics-and-genomics-advances", "food-chemistry", "european-journal-of-pharmaceutics-and-biopharmaceutics",
    "molecular-phylogenetics-and-evolution","lung-cancer", "journal-of-traditional-chinese-medical-sciences",
    "computational-biology-and-chemistry", "cell-reports-methods", "biocybernetics-and-biomedical-engineering",
    "journal-of-structural-biology", "journal-of-molecular-structure","journal-of-advanced-research",
    "genomics-proteomics-and-bioinformatics", "genomics", "genes-and-diseases", "current-opinion-in-chemical-biology",
    "current-opinion-in-structural-biology",
    "european-journal-of-pharmaceutical-sciences", "european-journal-of-integrative-medicine"]
    
sci_dir_25 = ["gene-expression-patterns","cell-reports-physical-science", "cell-reports-medicine", "cancer-cell",
    "biotechnology-advances",     
    "biochimica-et-biophysica-acta-bba-general-subjects",
    "biochimica-et-biophysica-acta-bba-molecular-basis-of-disease", 
    "biochimica-et-biophysica-acta-bba-proteins-and-proteomics", 
    "bioorganic-and-medicinal-chemistry",
    "bioresource-technology", "biophysical-journal",
    "cell-biology-international-reports", "cell", "cancer-genetics", 
    "computer-physics-communications", "computational-and-structural-biotechnology-journal",
    "european-journal-of-cancer", "current-biology", "chem","cell-reports", 
    "european-journal-of-cell-biology", "drug-discovery-today", "cell-chemical-biology", 
    "journal-of-molecular-graphics-and-modelling", "iscience", "european-journal-of-medicinal-chemistry",
    "journal-of-pharmaceutical-sciences", "journal-of-proteomics",
     "structure", "the-american-journal-of-human-genetics", "trends-in-biotechnology", "trends-in-cancer",
    "trends-in-cell-biology", "trends-in-chemistry","journal-of-molecular-biology"]

sci_dir_30 = ["polyhedron","tetrahedron"]
sci_dir_52 = ["journal-of-biological-chemistry"]

journal_lists = [sci_dir_10,sci_dir_25,sci_dir_30,sci_dir_52]
 
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # science direct
    f5 = open('science_dir.txt','w')
    for _list in journal_lists:
        for journal in _list:
            print(journal)
            if _list is sci_dir_10:
                sci_dir_list_dict = scrap_scidir(journal,f5,num=10)
            elif _list is sci_dir_25:
               sci_dir_list_dict = scrap_scidir(journal,f5,num=25)
            elif _list is sci_dir_30:
               sci_dir_list_dict = scrap_scidir(journal,f5,num=30)
            elif _list is sci_dir_52:
               sci_dir_list_dict = scrap_scidir(journal,f5,num=52)
    f5.close()

