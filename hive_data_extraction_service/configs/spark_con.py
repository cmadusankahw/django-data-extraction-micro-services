from pyspark.sql import SparkSession, SQLContext
from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql import Row
import json
import pandas

spark = SparkSession.builder\
    .appName("interfacing spark sql to hive metastore without configuration file")\
    .config("hive.metastore.uris", "thrift://10.101.16.82:9083")\
    .enableHiveSupport() \
    .getOrCreate()


# Queries are expressed in HiveQL
resultset = spark.sql("SELECT * FROM ibrac_propensity_db.clickstream limit 10").toPandas()

# resultset = spark.sql("SELECT * FROM ibrac_propensity_db.clickstream limit 10").toJSON().collect()
# parsed = json.dumps(resultset)

result = json.loads(resultset.to_json(orient="records"))

spark.close()

print(result)