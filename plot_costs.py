import sys, os
import matplotlib.pyplot as plt
import pandas as pd

def import_data(filename):
    data = pd.read_csv(filename, sep=',')
    return data

if __name__ == '__main__':
    pass
