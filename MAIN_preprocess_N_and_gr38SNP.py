from tqdm import tqdm
import pandas as pd

import argparse
import os

from easy_entrez import EntrezAPI
from UTIL_append_N_v3 import append_N

if __name__ == '__main__':

    #arguments
    parser = argparse.ArgumentParser(description="append constant N column into EVERY FILE IN THE FOLDER")
    parser.add_argument("--f", type=str, help="name of the folder", default="")
    args = parser.parse_args()

    folder = args.f
    sub_files = os.listdir(folder)

    #filter the files
    sub_files = [i for i in sub_files if i[0] != "."]
    
    print("\nappending sample size to every file in directory:", folder)

    #get the target df (summary statisctics)
    target_df = ""
    for file in tqdm(sub_files, desc = "searching master query index"):
        if "list_gwas_summary_statistics" in file:
            target_df_name = folder + "/" + file
            target_df = pd.read_csv(folder + "/" + file)
        
    #if the query file is not found in the target folder
    if type(target_df) == str and target_df == "":
        print("\nFAILED: gwas summary statistics not found")
        print("terminating")
        exit()
    else:
        print("gwas query found:", target_df_name)

    #if the data is not in the query file
    if "N" not in target_df.columns:
        print("\nFAILED: 'N' column missing in dataframe")
        print("terminating")
        exit()

    print("\n-----------------------------------------------------\n")
    print("starting data preprocessing")

    for gwas_id, N in zip(target_df["Study accession"], target_df["N"]):
        
        #search the subfiles for the target
        for files in sub_files:
            #found!
            if gwas_id in files:
                append_N(root_folder=folder, filename=files, N=N)

    print("\n-----------------------------------------------------\n")
    print("data processing finished")
            

        


    
