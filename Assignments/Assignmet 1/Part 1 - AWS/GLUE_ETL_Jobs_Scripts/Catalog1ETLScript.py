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
## @args: [database = "catalog1froms3", table_name = "catalog1_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "catalog1froms3", table_name = "catalog1_csv", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("id", "string", "id", "string"), ("file_name", "string", "file_name", "string"), ("file_index", "long", "file_index", "int"), ("img_type", "string", "img_type", "string"), ("time_utc", "string", "time_utc", "timestamp"), ("minute_offsets", "string", "minute_offsets", "string"), ("episode_id", "string", "episode_id", "int"), ("event_id", "string", "event_id", "int"), ("event_type", "string", "event_type", "string"), ("llcrnrlat", "double", "llcrnrlat", "double"), ("llcrnrlon", "double", "llcrnrlon", "double"), ("urcrnrlat", "double", "urcrnrlat", "double"), ("urcrnrlon", "double", "urcrnrlon", "double"), ("proj", "string", "proj", "string"), ("size_x", "long", "size_x", "int"), ("size_y", "long", "size_y", "int"), ("height_m", "long", "height_m", "int"), ("width_m", "long", "width_m", "int"), ("data_min", "double", "data_min", "double"), ("data_max", "double", "data_max", "double"), ("pct_missing", "long", "pct_missing", "double")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("id", "string", "id", "string"), ("file_name", "string", "file_name", "string"), ("file_index", "long", "file_index", "int"), ("img_type", "string", "img_type", "string"), ("time_utc", "string", "time_utc", "timestamp"), ("minute_offsets", "string", "minute_offsets", "string"), ("episode_id", "string", "episode_id", "int"), ("event_id", "string", "event_id", "int"), ("event_type", "string", "event_type", "string"), ("llcrnrlat", "double", "llcrnrlat", "double"), ("llcrnrlon", "double", "llcrnrlon", "double"), ("urcrnrlat", "double", "urcrnrlat", "double"), ("urcrnrlon", "double", "urcrnrlon", "double"), ("proj", "string", "proj", "string"), ("size_x", "long", "size_x", "int"), ("size_y", "long", "size_y", "int"), ("height_m", "long", "height_m", "int"), ("width_m", "long", "width_m", "int"), ("data_min", "double", "data_min", "double"), ("data_max", "double", "data_max", "double"), ("pct_missing", "long", "pct_missing", "double")], transformation_ctx = "applymapping1")
## @type: SelectFields
## @args: [paths = ["img_type", "time_utc", "file_name", "minute_offsets", "size_y", "size_x", "data_max", "proj", "llcrnrlon", "height_m", "pct_missing", "urcrnrlat", "file_index", "episode_id", "event_id", "event_type", "urcrnrlon", "data_min", "id", "width_m", "llcrnrlat"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]
selectfields2 = SelectFields.apply(frame = applymapping1, paths = ["img_type", "time_utc", "file_name", "minute_offsets", "size_y", "size_x", "data_max", "proj", "llcrnrlon", "height_m", "pct_missing", "urcrnrlat", "file_index", "episode_id", "event_id", "event_type", "urcrnrlon", "data_min", "id", "width_m", "llcrnrlat"], transformation_ctx = "selectfields2")
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "redshiftdatafortable1", table_name = "dev_public_catalog", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
resolvechoice3 = ResolveChoice.apply(frame = selectfields2, choice = "MATCH_CATALOG", database = "redshiftdatafortable1", table_name = "dev_public_catalog", transformation_ctx = "resolvechoice3")
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice4"]
## @return: resolvechoice4
## @inputs: [frame = resolvechoice3]
resolvechoice4 = ResolveChoice.apply(frame = resolvechoice3, choice = "make_cols", transformation_ctx = "resolvechoice4")
## @type: DataSink
## @args: [database = "redshiftdatafortable1", table_name = "dev_public_catalog", redshift_tmp_dir = TempDir, transformation_ctx = "datasink5"]
## @return: datasink5
## @inputs: [frame = resolvechoice4]
datasink5 = glueContext.write_dynamic_frame.from_catalog(frame = resolvechoice4, database = "redshiftdatafortable1", table_name = "dev_public_catalog", redshift_tmp_dir = args["TempDir"], transformation_ctx = "datasink5")
job.commit()