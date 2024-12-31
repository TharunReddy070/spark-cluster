from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_list, concat_ws

# Initialize Spark session
spark = SparkSession.builder.appName("MovieLensTags").getOrCreate()

# Load MovieLens data
movies_df = spark.read.csv("/data/movies.csv", header=True, inferSchema=True)
tags_df = spark.read.csv("/data/tags.csv", header=True, inferSchema=True)

# Join movies with tags to get associated tags for each movie
movie_tags = movies_df.join(tags_df, movies_df.movieId == tags_df.movieId).select("title", "tag")

# Perform MapReduce-like operation: Group tags by movie title
movie_tags_grouped = movie_tags.groupBy("title").agg(collect_list("tag").alias("tags"))

# Convert the array of tags into a single string, separated by commas
movie_tags_grouped = movie_tags_grouped.withColumn("tags", concat_ws(",", "tags"))

# Show the results
movie_tags_grouped.show()

# Save result to a file
movie_tags_grouped.write.csv("/data/movie_tags_output")
