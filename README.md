# scDRS Big Data Preprocessing Pipeline

The following are steps to process data using the python scrips in the current directory

#

## 1: GWAS Catalog API Wrapper (use home computer):
First download the GWAS Catalog Summary Statistics and drop the folder into this external hard drive.

The folder should contain the following:
- list_gwas_summary_statistics_DATE.csv (GWAS Query)
- [FOLDER].log (log file from downloading)
- all of the GWAS summary statistics *.gz

#

## 2: Unzipping all files in the Folder (use lab computer to uzip):
Use the following command to unzip the files using <code>unzip_gs_in_folder.sh</code>. Note that [FOLDER] has no "/".

    bash unzip_gs_in_folder.sh [FOLDER]

#
## 3: Renaming all of the files in the folder (use the either lab or home computer):
Here, use <codes>rename_files_to_include_traits.py</codes> to rename all the files in the folder so that they are easily identifiable by phenotype.

    python3 rename_files_to_include_traits.py --f [FOLDER WITHOUT "/"]

#
## 4: Add N (use excel to add column, run with lab computer): 
Now go through the <code>list_gwas_summary_statistics.csv</code> in each folder, and add a new column that says N for the sample size of the study.

Here, the <code>add_N.py</code> file will take in a folder, find the corresponding <code>list_gwas_summary_statistics.csv</code> with the new N column, and append that constant to each respective *.tsv in the folder.

    python3 add_N.py --f [FOLDER WITHOUT THE "/"]

## NOW EACH OF THE *.tsv FILES IN FOLDERS WILL BE READY FOR MAGMA