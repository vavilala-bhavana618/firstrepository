import os
import yaml
from prettytable import PrettyTable

# Create a PrettyTable
table = PrettyTable()
table.field_names = ["Environment", "Component Name", "Version"]
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Define the path to the current script

# Define the path to the 'env' folder based on the script's location
env_folder = os.path.join(script_dir, "env")  # Construct the path to the 'env' folder

# List all subdirectories (e.g., 'dev', 'prod-pilot', 'prod') in the 'env' folder
subdirectories = [d for d in os.listdir(env_folder) if os.path.isdir(os.path.join(env_folder, d))]


# Loop through subdirectories in 'env' (e.g., 'dev', 'prod-pilot', 'prod')

for environment in os.listdir(env_folder):
  environment_path = os.path.join(env_folder, environment)
  
  if os.path.isdir(environment_path):
    chart_yaml_path = os.path.join(environment_path, "helm", "Chart.yaml")
    # Modify the path to include the "helm" subdirectory

    if os.path.isfile(chart_yaml_path):
      with open(chart_yaml_path, "r") as chart_file:
        chart_data = yaml.safe_load(chart_file)
        
    if os.path.isfile(chart_yaml_path):
        with open(chart_yaml_path, "r") as chart_file:
            chart_data = yaml.safe_load(chart_file)
        
        # Extract component and version information
        components = chart_data.get("dependencies", [])
        
        for component in components:
            component_name = component.get("name", "N/A")
            component_version = component.get("version", "N/A")
            #component_repository = component.get("repository", "N/A")
            
          #  table.add_row([environment, component_name, component_version, component_repository])
            table.add_row([environment, component_name, component_version])

# Display the table
print(table)
