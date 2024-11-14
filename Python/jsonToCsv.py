import json
import csv
from datetime import datetime

# Load JSON data from file
with open('test.json', 'r') as file:
    data = json.load(file)

# Prepare a list to hold all rows for the CSV
rows = []

# Iterate over each series (pod)
for series in data['series']:
    pod_name = series['name']
    fields = series['fields']

    # Find the indices for 'Time' and 'Value'
    time_index = next(i for i, field in enumerate(fields) if field['name'] == 'Time')
    value_index = next(i for i, field in enumerate(fields) if field['name'] == 'Value' and field['type'] == 'number')

    # Extract timestamps and cpu values
    timestamps = fields[time_index]['values']
    cpu_values = fields[value_index]['values']

    # Convert Unix timestamps to human-readable timestamps
    readable_timestamps = [datetime.utcfromtimestamp(ts / 1000).strftime('%Y-%m-%d %H:%M:%S') for ts in timestamps]

    # Combine timestamps and cpu values and sort by cpu values in descending order
    combined = sorted(zip(readable_timestamps, cpu_values), key=lambda x: x[1], reverse=True)

    # Take the top 5 maximum vCPU values
    top_5 = combined[:5]

    # Add rows to the list
    for timestamp, cpu in top_5:
        rows.append({'pod-name': pod_name, 'timestamp': timestamp, 'cpu': cpu})

# Write to CSV file
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['pod-name', 'timestamp', 'cpu']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print("CSV file has been created successfully.")