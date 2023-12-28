import math
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
chromecast_df = pd.read_csv(
    'converted_datasets/dataset_chromecast_converted_version.csv')
smart_tv_df = pd.read_csv(
    'converted_datasets/dataset_smart-tv_converted_version.csv')

# Extract the values from the "bytes_up" column
chromecast_bytes_up = chromecast_df['bytes_up']
chromecast_bytes_down = chromecast_df['bytes_down']

# Extract the values from the "bytes_down" column
smart_tv_bytes_up = smart_tv_df['bytes_up']
smart_tv_bytes_down = smart_tv_df['bytes_down']


def calculate_bin_value_sturge_rule(data):
    """Calculates the number of bins using Sturge's Rule"""
    n = len(data)
    return int(1 + 3.3 * math.log(n, 10))


def plot_histogram(data, title):
    """Plots the histogram"""
    plt.hist(data, bins=calculate_bin_value_sturge_rule(data))
    plt.xlabel('Bytes')
    plt.ylabel('Frequência')
    plt.title(title)
    plt.savefig("histogram/" + title.replace(" ", "") + '.png')
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
    plt.hist(data, bins=calculate_bin_value_sturge_rule(
        data), cumulative=True, density=True)
    plt.xlabel('Bytes')
    plt.ylabel('ECDF')
    plt.title(title)
    plt.savefig("ecdf/"+ title.replace(" ", "") + '.png')
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

def write_statistics(file_name, data):
    """Writes the statistics to a file"""
    with open(file_name, 'w') as file:
        file.write('Média: ' + str(mean(data)) + '\n')
        file.write('Variância: ' + str(variance(data)) + '\n')
        file.write('Desvio padrão: ' + str(standard_deviation(data)) + '\n')

# plot upload histograms
#plot_histogram(chromecast_bytes_up, 'Taxa de upload - Chromecast')
#plot_histogram(smart_tv_bytes_up, 'Taxa de upload - Smart TV')

# plot download histograms
#plot_histogram(chromecast_bytes_down, 'Taxa de download - Chromecast')
#plot_histogram(smart_tv_bytes_down, 'Taxa de download - Smart TV')

# plot upload ecdf
#plot_ecdf_matplotlib(chromecast_bytes_up, 'FDE - Taxa de Upload - Chromecast')
#plot_ecdf_matplotlib(smart_tv_bytes_up, 'FDE - Taxa de Upload - Smart TV')

# plot download ecdf
#plot_ecdf_matplotlib(chromecast_bytes_down, 'FDE - Taxa de Download - Chromecast')
#plot_ecdf_matplotlib(smart_tv_bytes_down, 'FDE - Taxa de Download - Smart TV')

# calculate and print statistics
write_statistics('statistics/chromecast_bytes_up.txt', chromecast_bytes_up)
write_statistics('statistics/chromecast_bytes_down.txt', chromecast_bytes_down)
write_statistics('statistics/smart_tv_bytes_up.txt', smart_tv_bytes_up)
write_statistics('statistics/smart_tv_bytes_down.txt', smart_tv_bytes_down)

# plot upload boxplot

# plot_box_plot_altogether([bytes_down_values, chromecast_bytes_up], 'Upload vs Download')
