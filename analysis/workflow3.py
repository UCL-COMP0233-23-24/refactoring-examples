from math import *

class DataAnalyzer:
    def __init__(self, data1_path, data2_path, weights_path):
        self.data1 = self.read_csv(data1_path)
        self.data2 = self.read_csv(data2_path)
        self.weights = [float(w.strip()) for w in open(weights_path).readline().split(',')]
        self.results = self.calculate_d_index()

    def read_csv(self, file_path):
        with open(file_path) as file:
            lines = file.readlines()
            data = []
            for line in lines:
                row = [float(n.strip()) for n in line.split(',')]
                data.append(row)
        return data

    def calculate_d_index(self):
        return [sum(w * abs(self.data1[i][j] - self.data2[i][j]) for j, w in enumerate(self.weights)) for i in range(len(self.data1))]

    def check_criticality(self, threshold=5):
        critical_count = sum(1 for result in self.results if result > threshold)
        return critical_count

    def display_results(self):
        criticality = self.check_criticality()
        d_index = sum(self.results) / len(self.results)
        print("Criticality:", criticality, "results above 5")
        print("D-Index:", d_index)
