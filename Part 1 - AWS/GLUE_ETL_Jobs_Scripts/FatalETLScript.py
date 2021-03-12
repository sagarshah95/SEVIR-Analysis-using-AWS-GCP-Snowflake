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
## @args: [database = "fatalfroms31", table_name = "stormfatal_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "fatalfroms31", table_name = "stormfatal_csv", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("fat_yearmonth", "long", "fat_yearmonth", "int"), ("fat_day", "long", "fat_day", "int"), ("fat_time", "long", "fat_time", "int"), ("fatality_id", "long", "fatality_id", "int"), ("event_id", "long", "event_id", "int"), ("fatality_type", "string", "fatality_type", "string"), ("fatality_date", "string", "fatality_date", "timestamp"), ("fatality_age", "long", "fatality_age", "int"), ("fatality_sex", "string", "fatality_sex", "string"), ("fatality_location", "string", "fatality_location", "string"), ("event_yearmonth", "long", "event_yearmonth", "int")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("fat_yearmonth", "long", "fat_yearmonth", "int"), ("fat_day", "long", "fat_day", "int"), ("fat_time", "long", "fat_time", "int"), ("fatality_id", "long", "fatality_id", "int"), ("event_id", "long", "event_id", "int"), ("fatality_type", "string", "fatality_type", "string"), ("fatality_date", "string", "fatality_date", "timestamp"), ("fatality_age", "long", "fatality_age", "int"), ("fatality_sex", "string", "fatality_sex", "string"), ("fatality_location", "string", "fatality_location", "string"), ("event_yearmonth", "long", "event_yearmonth", "int")], transformation_ctx = "applymapping1")
## @type: SelectFields
## @args: [paths = ["fatality_id", "fatality_age", "fatality_location", "event_yearmonth", "fat_yearmonth", "event_id", "fat_time", "fat_day", "fatality_date", "fatality_sex", "fatality_type"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]
selectfields2 = SelectFields.apply(frame = applymapping1, paths = ["fatality_id", "fatality_age", "fatality_location", "event_yearmonth", "fat_yearmonth", "event_id", "fat_time", "fat_day", "fatality_date", "fatality_sex", "fatality_type"], transformation_ctx = "selectfields2")
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "fatalfromredshift", table_name = "dev_public_fatality", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
resolvechoice3 = ResolveChoice.apply(frame = selectfields2, choice = "MATCH_CATALOG", database = "fatalfromredshift", table_name = "dev_public_fatality", transformation_ctx = "resolvechoice3")
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice4"]
## @return: resolvechoice4
## @inputs: [frame = resolvechoice3]
resolvechoice4 = ResolveChoice.apply(frame = resolvechoice3, choice = "make_cols", transformation_ctx = "resolvechoice4")
## @type: DataSink
## @args: [database = "fatalfromredshift", table_name = "dev_public_fatality", redshift_tmp_dir = TempDir, transformation_ctx = "datasink5"]
## @return: datasink5
## @inputs: [frame = resolvechoice4]
datasink5 = glueContext.write_dynamic_frame.from_catalog(frame = resolvechoice4, database = "fatalfromredshift", table_name = "dev_public_fatality", redshift_tmp_dir = args["TempDir"], transformation_ctx = "datasink5")
job.commit()