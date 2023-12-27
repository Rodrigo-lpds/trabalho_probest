import math
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('./dataset_chromecast_converted_version.csv')

# Extract the values from the "bytes_up" column
bytes_up_values = df['bytes_up']
bytes_down_values = df['bytes_down']

def calculate_bin_value_sturge_rule(data):
    """Calculates the number of bins using Sturge's Rule"""
    n = len(data)
    return int(1 + math.log2(n))

def plot_histogram(data, title):
    """Plots the histogram"""
    plt.hist(data, bins=calculate_bin_value_sturge_rule(data))
    plt.xlabel('Bytes')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()

def plot_boxplot(data, title):
    """Plots the boxplot"""
    plt.boxplot(data)
    plt.ylabel('Bytes')
    plt.title(title)
    plt.show()

def plot_box_plot_altogether(data, title):
    """Plots the boxplot"""
    plt.boxplot(data)
    plt.ylabel('Bytes')
    plt.title(title)
    plt.show()

def plot_ecdf_matplotlib(data, title):
    """Plots the empirical cumulative distribution function"""
    plt.hist(data, bins=calculate_bin_value_sturge_rule(data), cumulative=True, density=True)
    plt.xlabel('Bytes')
    plt.ylabel('ECDF')
    plt.title(title)
    plt.show() 

def standard_deviation(data):
    """Calculates the standard deviation"""
    return round(data.std(), 2)

def mean(data):
    """Calculates the mean"""
    return round(data.mean(), 2)

def variance(data):
    """Calculates the variance"""
    return round(data.var(), 2) 


#plot_histogram(bytes_up_values, 'Upload')
#plot_histogram(bytes_down_values, 'Download')
#plot_boxplot(bytes_up_values, 'Upload')
#plot_boxplot(bytes_down_values, 'Download')
#plot_ecdf_matplotlib(bytes_up_values, 'Upload')
plot_box_plot_altogether([bytes_down_values, bytes_up_values], 'Upload vs Download')