from stage2 import read_file
import math
from prettytable import PrettyTable

#Growth[i] = (2008Quintile[i] - 1988Quintile[i])/1988Quntile[i]
def calcualte_grow(bin_average_1988, bin_average_2008):
    growth_dict = dict()
    for bin in bin_average_1988:
        average_1998 = bin_average_1988[bin]
        average_2008 = bin_average_2008[bin]
        growth_dict[bin] = math.ceil((average_2008-average_1998)/average_1998 * 100)
    return growth_dict

if __name__ == '__main__':
    bin_average_1988 = read_file("stage2.txt")
    bin_average_2008 = read_file("stage3.txt")

    growth_dict = calcualte_grow(bin_average_1988, bin_average_2008)

    t = PrettyTable(['Quntile Index(i)', 'Quintile Bin','Quintile\'s Growth'])
    for bin in growth_dict:
        first_per = str(int(bin) * 5)
        second_per = str((int(bin)+1)*5)
        t.add_row([bin, "{}% to {}%".format(first_per,second_per) ,"{}%".format(growth_dict[bin])])
    print(t)
