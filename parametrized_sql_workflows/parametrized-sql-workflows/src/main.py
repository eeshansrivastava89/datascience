from jinja2 import Environment, FileSystemLoader
import yaml
import os

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def render_sql(template_name, context):
    env = Environment(loader=FileSystemLoader('src/sql_templates'))
    template = env.get_template(template_name)
    return template.render(context)

def main():
    metrics_config = load_config('src/config/metrics.yaml')
    filters_config = load_config('src/config/filters.yaml')

    # Prepare context for SQL rendering
    context = {
        'metrics': metrics_config,
        'filters': filters_config,
        'tables': {
            'clickstream': 'clickstream_table',
            'customer': 'customer_table',
            'transaction': 'transaction_table'
        }
    }

    # Render the base SQL query
    base_query = render_sql('base_query.sql.j2', context)
    print("Base Query:")
    print(base_query)

    # Render metrics SQL
    metrics_query = render_sql('metrics.sql.j2', context)
    print("Metrics Query:")
    print(metrics_query)

if __name__ == "__main__":
    main()