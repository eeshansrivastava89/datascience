from pyspark.sql import SparkSession
import yaml
from jinja2 import Environment, FileSystemLoader
from utils.sql_renderer import render_sql

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Parametrized SQL Workflows") \
    .getOrCreate()

# Load configurations
with open('../config/metrics.yaml', 'r') as metrics_file:
    metrics_config = yaml.safe_load(metrics_file)

with open('../config/filters.yaml', 'r') as filters_file:
    filters_config = yaml.safe_load(filters_file)

# Set up Jinja2 environment for SQL templates
env = Environment(loader=FileSystemLoader('../sql_templates'))

# Load SQL templates
base_query_template = env.get_template('base_query.sql.j2')
metrics_template = env.get_template('metrics.sql.j2')

# Render SQL queries with parameters
base_query = render_sql(base_query_template, metrics_config, filters_config)
metrics_query = render_sql(metrics_template, metrics_config)

# Execute the rendered SQL queries
base_query_result = spark.sql(base_query)
metrics_query_result = spark.sql(metrics_query)

# Show results
base_query_result.show()
metrics_query_result.show()