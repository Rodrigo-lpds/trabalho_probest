import csv
import math

BYTES_UP_POSITION = 2
BYTES_DOWN_POSITION = 3


def update_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # skips first row
            if row[0] != 'device_id':
                row[BYTES_UP_POSITION] = updates_bytes_value(
                    row, BYTES_UP_POSITION)
                row[BYTES_DOWN_POSITION] = updates_bytes_value(
                    row, BYTES_DOWN_POSITION)
            data.append(row)
    return data


def writes_new_csv(file_path, new_data):
    with open(file_path, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(new_data)


def convert_to_log(value):
    return 0 if value == 0 else math.log(value, 10)


def updates_bytes_value(row, position):
    return convert_to_log(float(row[position]))


def main():
    # Specify the file path
    files = ["dataset_chromecast", "dataset_smart-tv"]
    for file in files:
        new_data = update_csv('original_datasets/' + file + '.csv')
        writes_new_csv('converted_datasets/' + file +
                       '_converted_version.csv', new_data)


main()
