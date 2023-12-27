import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("./dataset_smart-tv_converted_version.csv")

# Convert the 'date_hour' column to datetime
data['date_hour'] = pd.to_datetime(data['date_hour'])

# Extract the hour from the 'date_hour' column
data['hour'] = data['date_hour'].dt.hour

# Create a figure with 24 subplots
fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(12, 12))

# Iterate over each hour
for hour, ax in zip(range(12), axes.flatten()):
    # Filter the data for the current hour
    hour_data = data[data['hour'] == hour]

    # Create a box plot for the current hour
    ax.boxplot(hour_data['bytes_up'])
    ax.set_title(f'Hora {hour}')
    ax.set_xlabel('Hora')
    ax.set_ylabel('Taxa de Upload (bytes)')

# Adjust the layout of the subplots
plt.tight_layout()

# save the plot
plt.savefig('group_by_hours.png')

# Show the plot
plt.show()


# Create a figure with 24 subplots
fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(12, 12))
# Iterate over each hour
for hour, ax in zip(range(13,22), axes.flatten()):
    # Filter the data for the current hour
    hour_data = data[data['hour'] == hour]

    # Create a box plot for the current hour
    ax.boxplot(hour_data['bytes_up'])
    ax.set_title(f'Hora {hour}')
    ax.set_xlabel('Hora')
    ax.set_ylabel('Taxa de Upload (bytes)')

# Adjust the layout of the subplots
plt.tight_layout()

# Show the plot
plt.show()

# save the plot
#plt.savefig('group_by_hours.png')
