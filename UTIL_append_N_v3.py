import argparse
from tqdm import tqdm
import csv
import os


def append_N(root_folder, filename, N:str) -> None:
    #ex, parameters are cvd, and is iteration SHAH is passed in
    read_file = root_folder + "/" + filename
    print("\nreading %s" % read_file)

    #make new folder to put all data in
    if not os.path.exists(root_folder + "/%s_gwas_finished_data" % root_folder):
        os.mkdir(root_folder + "/%s_gwas_finished_data" % root_folder)

    #get length of file
    with open(read_file, "r") as f:
        count = 0
        for i in f.readlines():
            count += 1
        print("length of file:", count)
    
    ## NOTEE: THERE IS A NEW LINE CHARACTER AT THE END OF THE LAST ELEMENT OF THE LIST
    ##['SNP', 'CHR', 'BP', 'A1', 'A2', 'freq', 'b', 'se', 'p', 'N\n']

    with open(read_file, "r") as f:

        #write header
        header = next(f)

        #if header does not contain an "N" column yet
        N_list = ["N", "N\n", "n", "n\n"]
        if any(x in N_list for x in header.split("\t")) == False:
            header = header.strip("\n")
            header = f'{header}\tN\n'

            with open(root_folder + "/%s_gwas_finished_data/" % root_folder + filename, "a") as f_out:
                #write header first
                f_out.write(header)

                #iterate over the file for the actual data
                for datum in tqdm(f.readlines(), desc = "processing %s" % filename):
                    datum = datum.strip("\n")
                    datum = f'{datum}\t{N}\n'
                    f_out.write(datum)

        else:
            print("WARNING: file contains N")
            print("process skipped")
    
    print("finished data file:", root_folder + "/%s_gwas_finished_data/" % root_folder + filename)








########################################################################################################






if __name__ == "__main__":
    #arguments
    parser = argparse.ArgumentParser(description="append constant N column into either a .tsv or .csv file")
    parser.add_argument("--f", type=str, help="name of the file", default="")
    parser.add_argument("--N", type=int, help="sample size to append in a new column", default="")
    args = parser.parse_args()

    N = args.N
    filename = args.f

    if not os.path.exists("finished_data"):
        os.mkdir("finished_data")

    #get length of file
    with open(filename, "r") as f:
        count = 0
        for i in f.readlines():
            count += 1
        print("length of file:", count)
    

##NOTEE: THERE IS A NEW LINE CHARACTER AT THE END OF THE LAST ELEMENT OF THE LIST
##['SNP', 'CHR', 'BP', 'A1', 'A2', 'freq', 'b', 'se', 'p', 'N\n']


    with open(filename, "r") as f:
        print("starting iterations")

        #write header
        header = next(f)
        header = header.strip("\n")
        header = f'{header}\tN\n'

        with open("finished_data/" + filename, "a") as f_out:
            #write header first
            f_out.write(header)

            #iterate over the file for the actual data
            for datum in tqdm(f.readlines(), desc = "appending column"):
                datum = datum.strip("\n")
                datum = f'{datum}\t{N}\n'
                f_out.write(datum)
    
    print("finished data file:", "finished_data/" + filename)
