import os
import argparse
from re import sub
import pandas as pd
from tqdm import tqdm

from numpy import require
from regex import R

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="takes a folder, renames the GWAS IDS in that folder with corresponding traits")
    parser.add_argument("--f", type = str, default = "", help = "path to folder WITHOUT THE /", required = True)
    args = parser.parse_args()

    folder = args.f
    sub_files = os.listdir(folder)

    #filter the files
    sub_files = [i for i in sub_files if i[0] != "."]

    #get the target df (summary statisctics)
    target_df = ""
    for file in tqdm(sub_files, desc = "searching master query index"):
        if "list_gwas_summary_statistics" in file:
            print("gwas query found:", file)
            target_df = pd.read_csv(folder + "/" + file)
        
    if type(target_df) == str and target_df == "":
        print("gwas summary statistics not found")
        print("terminating")
        exit()
        
    #now if the program runs past this point, then there is indeed a df with gwas summary statistics
    # df index: ['First Author', 'PubMed ID', 'Study accession', 'Publication date', 'Journal', 'Title', 'Trait(s)', 'Reported trait', 'Data access']

    print("renaming ...")
    for gwas_id, trait in zip(target_df["Study accession"], target_df["Reported trait"]):

        #process the df["reported trait"] string
        trait = trait.replace(":", "")
        trait = trait.replace(".", "")
        trait = trait.replace(",", "")
        trait = trait.replace("(", "")
        trait = trait.replace(")", "")
        trait = trait.replace("-", "_")
        trait = trait.replace("/", "_")

        trait = trait.split(" ")
        trait = "_".join(trait)

        #if the gwas is downloaded properly
        for file in sub_files:
            if gwas_id in file:
                os.rename(folder + "/" + file, folder + "/" + trait + "_" + file)
        
    print("renaming finished")






