# Parametrized SQL Workflows

This project provides a framework for building parametrized SQL workflows to manage automated data pipelines for experimentation workflows, such as A/B testing. By utilizing templating engines and configuration files, the project allows for easy updates and modifications to SQL queries without the need to directly alter large SQL files.

## Project Structure

- **src/**: Contains the main application code.
  - **main.py**: Entry point for the application, orchestrating the execution of SQL workflows.
  - **sql_templates/**: Directory for SQL query templates.
    - **base_query.sql.j2**: Base SQL query template with placeholders for parameters.
    - **metrics.sql.j2**: SQL template for defining metrics dynamically.
  - **config/**: Configuration files for metrics and filters.
    - **metrics.yaml**: Defines various metrics used in SQL queries.
    - **filters.yaml**: Specifies filters to be applied in SQL queries.
  - **utils/**: Utility functions for rendering SQL templates.
    - **sql_renderer.py**: Functions to load templates and generate final SQL queries.

- **notebooks/**: Contains Jupyter notebooks for demonstration and usage examples.
  - **workflow_notebook.py**: Demonstrates how to use the parametrized SQL workflows.

- **requirements.txt**: Lists the dependencies required for the project.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the SQL workflows, execute the `main.py` file. This will initialize the workflow, load the necessary configurations, and execute the parametrized SQL queries based on the defined templates.

You can modify the metrics and filters by updating the `metrics.yaml` and `filters.yaml` files, respectively. This allows for flexible experimentation without the need to change the SQL templates directly.

## Contribution

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.