from __future__ import division
from collections import defaultdict
import ast
import math

data_file = open("data.txt")
distance_file = open("bhattacharyya_distance.txt", "a")

distr_dict = defaultdict(dict)


i = 0
for line in data_file:
    if line[0] != "s":
        tmp = list(ast.literal_eval(line))
        dict_list = dict(tmp)
        total = 0
        for key,val in dict_list.items():
           total += val 
        for key,val in dict_list.items():
            dict_list[key] = val/total
        distr_dict[i] = (dict_list)
        i += 1


def bhattacharyya(distr1, distr2):
    total = 0
    for key in distr1:
        if key in distr2:
            total += math.sqrt(distr1[key] * distr2[key])
    if (total > 0):
        return math.log(total) * -1
    return -1 



for key1 in distr_dict:
    for key2 in distr_dict:
        if (key1 != key2):
            distance_file.write("Distance between these distributions " +
                    str(key1) + ", " + str(key2) + ": ")
            distance_file.write(str(bhattacharyya(distr_dict[key1],distr_dict[key2])))
            distance_file.write("\n")


