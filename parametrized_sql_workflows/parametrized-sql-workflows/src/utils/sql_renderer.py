from jinja2 import Environment, FileSystemLoader
import yaml
import os

class SQLRenderer:
    def __init__(self, template_dir):
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def load_template(self, template_name):
        return self.env.get_template(template_name)

    def render_template(self, template_name, params):
        template = self.load_template(template_name)
        return template.render(params)

    def load_yaml_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def render_sql_from_config(self, base_template, metrics_config, filters_config):
        metrics = self.load_yaml_config(metrics_config)
        filters = self.load_yaml_config(filters_config)

        params = {
            'metrics': metrics,
            'filters': filters
        }

        return self.render_template(base_template, params)

# Example usage:
# renderer = SQLRenderer(template_dir='src/sql_templates')
# sql_query = renderer.render_sql_from_config('base_query.sql.j2', 'src/config/metrics.yaml', 'src/config/filters.yaml')