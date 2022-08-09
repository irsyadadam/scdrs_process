import pandas as pd
import os
import argparse
from tqdm import tqdm

from easy_entrez import EntrezAPI



if __name__ == '__main__':
    #arguments

    entrez_api = EntrezAPI( 'your-tool-name', 'e@mail.com', return_type='json')
    results = entrez_api.search(dict(chromosome=1, organism='human', position=925941), database='snp', max_results=1)


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

        #skip header
        next(f)

        with open("finished_data/" + filename, "a") as f_out:
            #iterate over the file for the actual data
            for datum in tqdm(f.readlines(), desc = "appending column"):
                datum = datum.strip("\n")
                datum = f'{datum}\t{N}\n'
                f_out.write(datum)

    
    print("finished data file:", "finished_data/" + filename)