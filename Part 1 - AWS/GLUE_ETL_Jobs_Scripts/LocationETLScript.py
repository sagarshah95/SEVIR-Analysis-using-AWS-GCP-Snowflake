import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [TempDir, JOB_NAME]
args = getResolvedOptions(sys.argv, ['TempDir','JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "locationfroms3", table_name = "stormlocation_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "locationfroms3", table_name = "stormlocation_csv", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("yearmonth", "long", "yearmonth", "int"), ("episode_id", "long", "episode_id", "int"), ("event_id", "long", "event_id", "int"), ("location_index", "long", "location_index", "int"), ("range", "double", "range", "double"), ("azimuth", "string", "azimuth", "string"), ("location", "string", "location", "string"), ("latitude", "double", "latitude", "double"), ("longitude", "double", "longitude", "double"), ("lat2", "long", "lat2", "int"), ("lon2", "long", "lon2", "int")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("yearmonth", "long", "yearmonth", "int"), ("episode_id", "long", "episode_id", "int"), ("event_id", "long", "event_id", "int"), ("location_index", "long", "location_index", "int"), ("range", "double", "range", "double"), ("azimuth", "string", "azimuth", "string"), ("location", "string", "location", "string"), ("latitude", "double", "latitude", "double"), ("longitude", "double", "longitude", "double"), ("lat2", "long", "lat2", "int"), ("lon2", "long", "lon2", "int")], transformation_ctx = "applymapping1")
## @type: SelectFields
## @args: [paths = ["lat2", "episode_id", "event_id", "location_index", "lon2", "latitude", "range", "azimuth", "location", "yearmonth", "longitude"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]
selectfields2 = SelectFields.apply(frame = applymapping1, paths = ["lat2", "episode_id", "event_id", "location_index", "lon2", "latitude", "range", "azimuth", "location", "yearmonth", "longitude"], transformation_ctx = "selectfields2")
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "locationfromredshift", table_name = "dev_public_location", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
resolvechoice3 = ResolveChoice.apply(frame = selectfields2, choice = "MATCH_CATALOG", database = "locationfromredshift", table_name = "dev_public_location", transformation_ctx = "resolvechoice3")
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice4"]
## @return: resolvechoice4
## @inputs: [frame = resolvechoice3]
resolvechoice4 = ResolveChoice.apply(frame = resolvechoice3, choice = "make_cols", transformation_ctx = "resolvechoice4")
## @type: DataSink
## @args: [database = "locationfromredshift", table_name = "dev_public_location", redshift_tmp_dir = TempDir, transformation_ctx = "datasink5"]
## @return: datasink5
## @inputs: [frame = resolvechoice4]
datasink5 = glueContext.write_dynamic_frame.from_catalog(frame = resolvechoice4, database = "locationfromredshift", table_name = "dev_public_location", redshift_tmp_dir = args["TempDir"], transformation_ctx = "datasink5")
job.commit()