from transformers import pipeline
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf

S3_DATA_INPUT_PATH="s3://[path where 'imdb_top_movie_review.csv' located in S3]" #paste your own path in the brackets
S3_DATA_OUTPUT_PATH_FILTERED="s3://[path for the output in S3]" #paste your own path in the brackets

def main():

    spark = SparkSession.builder.appName('project').getOrCreate()
    df = spark.read.option("header",True).csv(S3_DATA_INPUT_PATH, inferSchema=True)
    print(f'The total number of records in the source data set is {df.count()}')

    clean_df = df.na.drop() # Drop null value

    # Load model & define user function
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarizeUDF = udf(lambda text : summarizer(text, max_length=130, min_length=30, do_sample=False)) 

    # make a "Summary review" column by summary review in a "Review_content" column
    summary_df = clean_df.withColumn('Summary review', testUDF(clean_df['Review_content']))

    # preview data
    summary_df.show(10)
    summary_df.printSchema()
    summary_df.write.mode('overwrite').parquet(S3_DATA_OUTPUT_PATH_FILTERED)

    print('summary data successfully')


if __name__ == '__main__':
    main()
