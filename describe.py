import sys
import pandas as pd
import numpy as np
import math

ressource = sys.argv[1]
df = pd.read_csv(ressource)

df = df.drop(['First Name', 'Last Name', 'Best Hand', 'Birthday', 'Hogwarts House'], axis=1)

line, col = np.shape(df)

data_to_sort = {}
for column in df.columns.values.tolist():
    data_to_sort[column] = df[column].to_list()

display = {'Count': {}, 'Mean': {}, 'std': {}, 'min': {}, '25%': {}, '50%': {}, '75%': {}, 'max': {}}

def sort_data(data_to_sort):
    for key in data_to_sort:
        display['Count'][key] = len(data_to_sort[key])

        # Remove NaN after storing the total number of elements
        data_to_sort[key] = [x for x in data_to_sort[key] if x == x]

        for i in range(0, len(data_to_sort[key])):
            for j in range(i + 1, len(data_to_sort[key])):
                # Both not NaN
                if (data_to_sort[key][i] == data_to_sort[key][i] and data_to_sort[key][j] == data_to_sort[key][j]):
                    # Swap
                    if (data_to_sort[key][i] > data_to_sort[key][j]):
                        tmp = data_to_sort[key][i]
                        data_to_sort[key][i] = data_to_sort[key][j]
                        data_to_sort[key][j] = tmp
    return data_to_sort

sorted_data = sort_data(data_to_sort)

def fill_feature(sorted_data):
    for column in sorted_data:
        column_length = len(sorted_data[column])
        display['Count'][column] = column_length

        if column_length == 0:
            display['Mean'][column] = 'NaN'
            display['std'][column] = 'NaN'
            display['min'][column] = 'NaN'
            display['25%'][column] = 'NaN'
            display['50%'][column] = 'NaN'
            display['75%'][column] = 'NaN'
            display['max'][column] = 'NaN'
        else:
            calculated_mean = 0

            # NaN are removed so the max is always at the end and the min at the beggining
            min_found = sorted_data[column][0]
            max_found = sorted_data[column][-1]

            for i in range(0, column_length):
                calculated_mean += sorted_data[column][i]

            calculated_mean /= column_length

            std = 0
            for i in range(0, column_length):
                std += (sorted_data[column][i] - calculated_mean) ** 2
            std /= column_length
            std = math.sqrt(std)


            p_25 = str(sorted_data[column][int(column_length * 0.25)])
            p_50 = str(sorted_data[column][int(column_length * 0.5)])
            p_75 = str(sorted_data[column][int(column_length * 0.75)])
            
            display['Mean'][column] = str(calculated_mean)[0:min(len(str(calculated_mean)), len(column))]

            # STD represent the variance between the data and the mean
            display['std'][column] = str(std)[0:min(len(str(std)), len(column))]
            display['min'][column] = str(min_found)[0:min(len(str(min_found)), len(column))]
            display['25%'][column] = p_25[0:min(len(p_25), len(column))]
            display['50%'][column] = p_50[0:min(len(p_50), len(column))]
            display['75%'][column] = p_75[0:min(len(p_75), len(column))]
            display['max'][column] = str(max_found)[0:min(len(str(max_found)), len(column))]
    return display

display = fill_feature(sorted_data)

order = list(display['Count'].keys())

print(f"      | {' | '.join([x for x in order])}")
print(f"Count | {' | '.join([' ' * max(0, len(x) - len(str(display['Count'][x]))) + str(display['Count'][x]) for x in order])}")
print(f"Mean  | {' | '.join([' ' * max(0, len(x) - len(str(display['Mean'][x]))) + str(display['Mean'][x]) for x in order])}")
print(f"Std   | {' | '.join([' ' * max(0, len(x) - len(str(display['std'][x]))) + str(display['std'][x]) for x in order])}")
print(f"Min   | {' | '.join([' ' * max(0, len(x) - len(str(display['min'][x]))) + str(display['min'][x]) for x in order])}")
print(f"25%   | {' | '.join([' ' * max(0, len(x) - len(str(display['25%'][x]))) + str(display['25%'][x]) for x in order])}")
print(f"50%   | {' | '.join([' ' * max(0, len(x) - len(str(display['50%'][x]))) + str(display['50%'][x]) for x in order])}")
print(f"75%   | {' | '.join([' ' * max(0, len(x) - len(str(display['75%'][x]))) + str(display['75%'][x]) for x in order])}")
print(f"Max   | {' | '.join([' ' * max(0, len(x) - len(str(display['max'][x]))) + str(display['max'][x]) for x in order])}")
