import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


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

def plot_histogram(data, title):
    plt.hist(data, bins=calculate_bin_value_sturge_rule(data))
    plt.xlabel('Bytes')
    plt.ylabel('Frequência')
    plt.title(title)
    plt.savefig("histogram/" + title.replace(" ", "") + '.png')
    plt.show()

def calculate_bin_value_sturge_rule(data):
    """Calculates the number of bins using Sturge's Rule"""
    n = len(data)
    return int(1 + 3.3 * math.log(n, 10))

def plot_qqplot(data_1, data_2, title):
    # Fit a line to the QQ-plot
    sm.qqplot_2samples(data_1, data_2, line='45')

    # Customize the plot
    plt.xlabel('Quantis da distribuição normal')
    plt.ylabel('Quantis da distribuição dos dados')
    plt.title(title)
    plt.savefig("qqplot/" + title.replace(" ", "") + '.png')
    plt.show()

dataset_1 = data_by_hour(smart_tv_data, 20)['bytes_up']
dataset_2 = data_by_hour(chromecast_data, 22)['bytes_up']
dataset_3 = data_by_hour(smart_tv_data, 20)['bytes_down']
dataset_4 = data_by_hour(chromecast_data, 22)['bytes_down']

plot_histogram(dataset_1, "Smart TV - Upload - 20h")
plot_histogram(dataset_2, "Chromecast - Upload - 22h")
plot_histogram(dataset_3, "Smart TV - Download - 20h")
plot_histogram(dataset_4, "Chromecast - Download - 22h")

plot_qqplot(dataset_1, dataset_3, "QQplot - Upload")
plot_qqplot(dataset_2, dataset_4, "QQplot - Download")