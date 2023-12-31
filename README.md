# Movie reviews summary from IMDB data

## This project scarbing movie reviews from IMDB and keep it into S3. Then use PySpark to summarise reviews before perform to AWS Athena.

[picture of aws dirgram]

## File
* web scarb
* pyspark process file

## Data flow
* web scrabing all reviews in first page of "review page" from top 50 movies by using selenium and BeautifulSoup
* sent data into S3
* summarise reviews with "bart-large-cnn" (https://huggingface.co/facebook/bart-large-cnn) in AWS EMR
* sent data into S3
* use Athena to EDA

## How to use
1. clone this project first
2. [optional] edits and run "IMDB_webscrabping.ipynb" file in case of wanting to pull more reviews or movies
3. access to primary node following AWS guild in EMR
4. create file in primary node by using ```vi summary.py``` and copy code in file "summary.py" and paste into it
5. save file and run ```pyspark-summit summary.py```
6. EDA it on athena
