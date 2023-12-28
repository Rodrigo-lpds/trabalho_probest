import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
chromecast_data = pd.read_csv("./converted_datasets/dataset_chromecast_converted_version.csv")
smart_tv_data = pd.read_csv("./converted_datasets/dataset_smart-tv_converted_version.csv")

def transform_data(data):
    # Convert the 'date_hour' column to datetime
    data['date_hour'] = pd.to_datetime(data['date_hour'])

    # Extract the hour from the 'date_hour' column
    data['hour'] = data['date_hour'].dt.hour
    
    return data

def data_by_hour(data, hour):
    data = transform_data(data)
    """Returns the data filtered by hour"""
    return data[data['hour'] == hour]

def plot_download_mean_by_hour(data, title):
    """Plots the mean of the data by hour"""
    data = transform_data(data)
    # Calculate the mean by hour
    mean_by_hour = data.groupby('hour')['bytes_up'].mean()
    # Calculate the standard deviation by hour and add to chart
    std_by_hour = data.groupby('hour')['bytes_up'].std()

    # Create a point plot
    plt.errorbar(mean_by_hour.index, mean_by_hour.values, yerr=std_by_hour.values, fmt='o', capsize=6)
    plt.title(title)
    plt.xlabel('Hora')
    plt.ylabel('Média de Upload (bytes)')

    plt.savefig("mean_by_hour/" + title.replace(" ", "") + '.png')

    # Show the plot
    plt.show()

def plot_upload_mean_by_hour(data, title):
    """Plots the mean of the data by hour"""
    data = transform_data(data)
    # Calculate the mean by hour
    mean_by_hour = data.groupby('hour')['bytes_down'].mean()
    # Calculate the standard deviation by hour and add to chart
    std_by_hour = data.groupby('hour')['bytes_down'].std()
    
    # Create a point plot
    plt.errorbar(mean_by_hour.index, mean_by_hour.values, yerr=std_by_hour.values, fmt='o', capsize=6)
    plt.title(title)
    plt.xlabel('Hora')
    plt.ylabel('Média de Upload (bytes)')

    plt.savefig("mean_by_hour/" + title.replace(" ", "") + '.png')

    # Show the plot
    plt.show()


def create_24_subplots(data):
    """Creates 24 subplots"""
    # Create a figure with 24 subplots
    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(12, 12))

    # Iterate over each hour
    for hour, ax in zip(range(12), axes.flatten()):
        # Filter the data for the current hour
        hour_data = data[data['hour'] == hour]

        # Create a box plot for the current hour
        ax.boxplot(hour_data['bytes_up'])
        ax.set_title(f'{hour}h')
        ax.set_xlabel('Hora')
        ax.set_ylabel('Taxa de Upload (bytes)')

    # Adjust the layout of the subplots
    plt.tight_layout()

    # Show the plot
    plt.show()

plot_download_mean_by_hour(chromecast_data, 'Média de Upload por Hora - Chromecast')
plot_upload_mean_by_hour(chromecast_data, 'Média de Download por Hora - Chromecast')
plot_download_mean_by_hour(smart_tv_data, 'Média de Upload por Hora - Smart TV')
plot_upload_mean_by_hour(smart_tv_data, 'Média de Download por Hora - Smart TV')
