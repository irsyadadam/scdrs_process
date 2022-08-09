#PARAMETERS:
#bash unzip_all.sh [FOLDER]
#    [FOLDER] is the directory to unzip all gz files

folder=$1

for filename in ${folder}/*.gz; do
    gzip -d ${filename}
done
