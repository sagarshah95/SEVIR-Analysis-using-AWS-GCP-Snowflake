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
## @args: [database = "detailsfroms3", table_name = "stormdetails_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "detailsfroms3", table_name = "stormdetails_csv", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("begin_yearmonth", "long", "begin_yearmonth", "int"), ("begin_day", "long", "begin_day", "int"), ("begin_time", "long", "begin_time", "int"), ("end_yearmonth", "long", "end_yearmonth", "int"), ("end_day", "long", "end_day", "int"), ("end_time", "long", "end_time", "int"), ("episode_id", "long", "episode_id", "int"), ("event_id", "long", "event_id", "int"), ("state", "string", "state", "string"), ("state_fips", "long", "state_fips", "int"), ("year", "long", "year", "int"), ("month_name", "string", "month_name", "string"), ("event_type", "string", "event_type", "string"), ("cz_type", "string", "cz_type", "string"), ("cz_fips", "long", "cz_fips", "int"), ("cz_name", "string", "cz_name", "string"), ("wfo", "string", "wfo", "string"), ("begin_date_time", "string", "begin_date_time", "string"), ("cz_timezone", "string", "cz_timezone", "string"), ("end_date_time", "string", "end_date_time", "string"), ("injuries_direct", "long", "injuries_direct", "int"), ("injuries_indirect", "long", "injuries_indirect", "int"), ("deaths_direct", "long", "deaths_direct", "int"), ("deaths_indirect", "long", "deaths_indirect", "int"), ("damage_property", "string", "damage_property", "string"), ("damage_crops", "string", "damage_crops", "string"), ("source", "string", "source", "string"), ("magnitude", "double", "magnitude", "double"), ("magnitude_type", "string", "magnitude_type", "string"), ("flood_cause", "string", "flood_cause", "string"), ("category", "string", "category", "string"), ("tor_f_scale", "string", "tor_f_scale", "string"), ("tor_length", "double", "end_range", "double"), ("tor_width", "long", "tor_width", "int"), ("tor_other_wfo", "string", "tor_other_wfo", "string"), ("tor_other_cz_state", "string", "tor_other_cz_state", "string"), ("tor_other_cz_fips", "string", "tor_other_cz_fips", "string"), ("tor_other_cz_name", "string", "tor_other_cz_name", "string"), ("begin_range", "long", "begin_range", "double"), ("begin_azimuth", "string", "begin_azimuth", "string"), ("begin_location", "string", "begin_location", "string"), ("end_range", "long", "tor_length", "int"), ("end_azimuth", "string", "end_azimuth", "string"), ("end_location", "string", "end_location", "string"), ("begin_lat", "double", "begin_lat", "double"), ("begin_lon", "double", "begin_lon", "double"), ("end_lat", "double", "end_lat", "double"), ("end_lon", "double", "end_lon", "double"), ("episode_narrative", "string", "episode_narrative", "string"), ("event_narrative", "string", "event_narrative", "string"), ("data_source", "string", "data_source", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("begin_yearmonth", "long", "begin_yearmonth", "int"), ("begin_day", "long", "begin_day", "int"), ("begin_time", "long", "begin_time", "int"), ("end_yearmonth", "long", "end_yearmonth", "int"), ("end_day", "long", "end_day", "int"), ("end_time", "long", "end_time", "int"), ("episode_id", "long", "episode_id", "int"), ("event_id", "long", "event_id", "int"), ("state", "string", "state", "string"), ("state_fips", "long", "state_fips", "int"), ("year", "long", "year", "int"), ("month_name", "string", "month_name", "string"), ("event_type", "string", "event_type", "string"), ("cz_type", "string", "cz_type", "string"), ("cz_fips", "long", "cz_fips", "int"), ("cz_name", "string", "cz_name", "string"), ("wfo", "string", "wfo", "string"), ("begin_date_time", "string", "begin_date_time", "string"), ("cz_timezone", "string", "cz_timezone", "string"), ("end_date_time", "string", "end_date_time", "string"), ("injuries_direct", "long", "injuries_direct", "int"), ("injuries_indirect", "long", "injuries_indirect", "int"), ("deaths_direct", "long", "deaths_direct", "int"), ("deaths_indirect", "long", "deaths_indirect", "int"), ("damage_property", "string", "damage_property", "string"), ("damage_crops", "string", "damage_crops", "string"), ("source", "string", "source", "string"), ("magnitude", "double", "magnitude", "double"), ("magnitude_type", "string", "magnitude_type", "string"), ("flood_cause", "string", "flood_cause", "string"), ("category", "string", "category", "string"), ("tor_f_scale", "string", "tor_f_scale", "string"), ("tor_length", "double", "end_range", "double"), ("tor_width", "long", "tor_width", "int"), ("tor_other_wfo", "string", "tor_other_wfo", "string"), ("tor_other_cz_state", "string", "tor_other_cz_state", "string"), ("tor_other_cz_fips", "string", "tor_other_cz_fips", "string"), ("tor_other_cz_name", "string", "tor_other_cz_name", "string"), ("begin_range", "long", "begin_range", "double"), ("begin_azimuth", "string", "begin_azimuth", "string"), ("begin_location", "string", "begin_location", "string"), ("end_range", "long", "tor_length", "int"), ("end_azimuth", "string", "end_azimuth", "string"), ("end_location", "string", "end_location", "string"), ("begin_lat", "double", "begin_lat", "double"), ("begin_lon", "double", "begin_lon", "double"), ("end_lat", "double", "end_lat", "double"), ("end_lon", "double", "end_lon", "double"), ("episode_narrative", "string", "episode_narrative", "string"), ("event_narrative", "string", "event_narrative", "string"), ("data_source", "string", "data_source", "string")], transformation_ctx = "applymapping1")
## @type: SelectFields
## @args: [paths = ["end_day", "month_name", "wfo", "end_lat", "year", "event_narrative", "source", "begin_yearmonth", "deaths_direct", "end_date_time", "episode_id", "event_type", "begin_day", "tor_f_scale", "begin_azimuth", "end_range", "state", "begin_lat", "state_fips", "deaths_indirect", "magnitude_type", "tor_other_cz_state", "tor_other_cz_fips", "tor_other_cz_name", "begin_lon", "begin_location", "cz_type", "damage_property", "data_source", "injuries_indirect", "end_yearmonth", "begin_range", "cz_timezone", "episode_narrative", "end_location", "magnitude", "tor_width", "end_lon", "damage_crops", "end_time", "begin_time", "cz_fips", "begin_date_time", "tor_other_wfo", "end_azimuth", "event_id", "cz_name", "tor_length", "category", "flood_cause", "injuries_direct"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]
selectfields2 = SelectFields.apply(frame = applymapping1, paths = ["end_day", "month_name", "wfo", "end_lat", "year", "event_narrative", "source", "begin_yearmonth", "deaths_direct", "end_date_time", "episode_id", "event_type", "begin_day", "tor_f_scale", "begin_azimuth", "end_range", "state", "begin_lat", "state_fips", "deaths_indirect", "magnitude_type", "tor_other_cz_state", "tor_other_cz_fips", "tor_other_cz_name", "begin_lon", "begin_location", "cz_type", "damage_property", "data_source", "injuries_indirect", "end_yearmonth", "begin_range", "cz_timezone", "episode_narrative", "end_location", "magnitude", "tor_width", "end_lon", "damage_crops", "end_time", "begin_time", "cz_fips", "begin_date_time", "tor_other_wfo", "end_azimuth", "event_id", "cz_name", "tor_length", "category", "flood_cause", "injuries_direct"], transformation_ctx = "selectfields2")
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "detailsfromredshift", table_name = "dev_public_details", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
resolvechoice3 = ResolveChoice.apply(frame = selectfields2, choice = "MATCH_CATALOG", database = "detailsfromredshift", table_name = "dev_public_details", transformation_ctx = "resolvechoice3")
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice4"]
## @return: resolvechoice4
## @inputs: [frame = resolvechoice3]
resolvechoice4 = ResolveChoice.apply(frame = resolvechoice3, choice = "make_cols", transformation_ctx = "resolvechoice4")
## @type: DataSink
## @args: [database = "detailsfromredshift", table_name = "dev_public_details", redshift_tmp_dir = TempDir, transformation_ctx = "datasink5"]
## @return: datasink5
## @inputs: [frame = resolvechoice4]
datasink5 = glueContext.write_dynamic_frame.from_catalog(frame = resolvechoice4, database = "detailsfromredshift", table_name = "dev_public_details", redshift_tmp_dir = args["TempDir"], transformation_ctx = "datasink5")
job.commit()