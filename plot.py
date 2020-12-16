import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt


def plot_1(x, y, year):
    fig = plt.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('Rain Fall (mm)')
    ax1.set_xlabel('Month')
    ax1.set_title(f'Average Rain fall in Taipei in {year}')
    ax1.set_ylim([0, max(y)+10])
    line, = ax1.plot(x, y, lw=2)

    plt.show()


def plot_2(x, y, year):
    fig = plt.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('Rain Fall (mm)')
    ax1.set_xlabel('Month')
    ax1.set_title(f'Average Rain fall in Taipei in {year}')

    ax1.bar(x, y)
    plt.show()


def plot_3(x, y_1, y_2, y_3):
    fig = plt.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('Rain Fall (mm)')
    ax1.set_xlabel('Month')
    ax1.set_title(f'Average Rain fall in Taipei (in different time slots)')
    ax1.set_ylim([np.min(np.minimum(y_1, y_2, y_3))-10, np.max(np.maximum(y_1, y_2, y_3))+10])

    line1, = ax1.plot(x, y_1, lw=2, label='1960 to 1980', marker = "^")
    line1.set_dashes([2, 2, 10, 2])
    line2, = ax1.plot(x, y_2, lw=2, label='1980 to 2000', marker = "s")
    line2.set_dashes([6, 2])
    line3, = ax1.plot(x, y_3, lw=2, label='2000 to 2017', marker = "o")
    line3.set_dashes([2, 1.5])

    ax1.legend()
    plt.show()


def main():
    year = 2017
    if(len(sys.argv) > 1 and int(sys.argv[1]) >= 1960 and int(sys.argv[1]) <= 2017):
        year = int(sys.argv[1])

    raw_data = pd.read_csv('rain.csv').values.tolist()

    data_in_year = [x[5] for x in raw_data if x[1] == year]
    data_in_year = np.array(data_in_year).reshape((12, -1)).sum(axis=1)

    data_1 = [x[5] for x in raw_data if x[1] >= 1960 and x[1] < 1980]
    data_2 = [x[5] for x in raw_data if x[1] >= 1980 and x[1] < 2000]
    data_3 = [x[5] for x in raw_data if x[1] >= 1960 and x[1] < 2018]

    data_1 = np.array(data_1).reshape((12, 22, -1)).sum(axis=1).mean(axis=1)
    data_2 = np.array(data_2).reshape((12, 22, -1)).sum(axis=1).mean(axis=1)
    data_3 = np.array(data_3).reshape((12, 22, -1)).sum(axis=1).mean(axis=1)

    plot_1(range(1, 13), data_in_year, year)
    plot_2(range(1, 13), data_in_year, year)
    plot_3(range(1, 13), data_1, data_2, data_3)


if __name__ == "__main__":
    main()
