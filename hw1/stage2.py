import numpy as np
from prettytable import PrettyTable
import sys

def read_file(file_name="stage2.txt"):
    with open(file_name) as file:
        lineArr=file.read().split('\n')

        bin_value_dict = dict()
        bin_weight_dict = dict()
        for (index,line) in enumerate(lineArr):
            if index == 0 or index == len(lineArr) - 1: continue
            tmp = line.split()
            rrinc = tmp[0]
            quint_index = tmp[1]
            pop = tmp[3]

            if quint_index not in bin_value_dict:
                bin_value_dict[quint_index] = [rrinc]
                bin_weight_dict[quint_index] = [pop]
            else:
                bin_value_dict[quint_index].append(rrinc)
                bin_weight_dict[quint_index].append(pop)

        t = PrettyTable(['Quntile Index(i)', 'Quintile Bin','Quintile\'s Average RRinc'])
        bin_average = dict()
        for bin in bin_value_dict:
            value_arr = np.array(bin_value_dict[bin], dtype=np.float32)
            weight_arr = np.array(bin_weight_dict[bin], dtype=np.float32)
            # Sum(value * weight)/sum(weight)
            average = round(np.dot(value_arr, weight_arr) / np.sum(weight_arr), 2)
            bin_average[bin] = average
            first_per = str(int(bin) * 5)
            second_per = str((int(bin)+1)*5)
            t.add_row([bin, "{}% to {}%".format(first_per,second_per) ,average])
        print(t)
        return bin_average
        
if __name__ == '__main__':
    read_file()
