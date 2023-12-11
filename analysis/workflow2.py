from math import *

from workflow3 import DataAnalyzer

workflow2 = DataAnalyzer('samples1.csv', 'samples2.csv', 'weights.csv')
workflow2.display_results()