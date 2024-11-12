import argparse
import logging
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

logging.basicConfig(level=logging.INFO)

# Parse Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--input_object_store_base_url")
parser.add_argument("--input_path")
parser.add_argument("--output_object_store_base_url")
parser.add_argument("--output_path")
parser.add_argument("--subreddits")
args = parser.parse_args()

logging.info(args.input_object_store_base_url)
logging.info(args.input_path)
logging.info(args.output_object_store_base_url)
logging.info(args.output_path)
logging.info(args.subreddits)

input_complete_path = f"{args.input_object_store_base_url}{args.input_path}"
output_complete_path = f"{args.output_object_store_base_url}{args.output_path}"

logging.info(input_complete_path)
logging.info(output_complete_path)

spark = SparkSession.builder.appName("PySparkApp").getOrCreate()
logging.info(f"spark version = {spark.version}")

# Read data from object store
logging.info(f"going to read {input_complete_path}")
df_in = spark.read.parquet(input_complete_path)
df_in_ct = df_in.count()
logging.info(f"finished reading files...")

# filter the dataframe to only keep the subreddits of interest
subreddits = [s.strip().lower() for s in args.subreddits.split(",")]
filtered = df_in.where(lower(col("subreddit")).isin(subreddits))
filtered_ct = filtered.count()

# save the filtered dataframes so that these files can now be used for future analysis
logging.info(f"going to write {output_complete_path}")

logging.info(f"Read in {df_in_ct} records, wrote out {filtered_ct} records.")
filtered.write.mode("overwrite").parquet(output_complete_path, compression="zstd")

spark.stop()
