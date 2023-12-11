from math import *

from workflow3 import DataAnalyzer

workflow1 = DataAnalyzer('data1.csv', 'data2.csv', 'weights.csv')
workflow1.display_results()