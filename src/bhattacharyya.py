from __future__ import division
from collections import defaultdict
import ast
import math

data_file = open("data.txt")
distance_file = open("bhattacharyya_distance.txt", "a")
distance_file.truncate()

#Dictionary of the discrete distributions found by the crawler
distr_dict = defaultdict(dict)

#Create a discrete distribution from the data found by the crawler
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


#calculate the bhattacharyya distance between two distributions
def bhattacharyya(distr1, distr2):
    total = 0
    for key in distr1:
        if key in distr2:
            total += math.sqrt(distr1[key] * distr2[key])
    if (total > 0):
        return math.log(total) * -1
    return -1 

#Calculates the K-L divergence between two distributions 
def kl_divergence(distr1, distr2):
    total = 0
    for key in distr1:
        if key in distr2:
            total += distr1[key] * math.log(distr1[key]/distr2[key])
    """
    Note that if the key is not in both distributions, then the
    Kullback-Leibler divergence is not defined, so this will have skewed
    results
    """
    return total



#Find the pairwise distances, output the average distance
average_distance = 0
average_div = 0
count = 0
count_div = 0
for key1 in distr_dict:
    for key2 in distr_dict:
        if (key1 != key2):
            distance_file.write("Distance between these distributions " +
                    str(key1) + ", " + str(key2) + ": ")
            #Compute the Bhattacharyya distance
            dist = bhattacharyya(distr_dict[key1],distr_dict[key2])
            if dist != -1:
                count += 1
                average_distance += dist
            distance_file.write(str(dist))
            distance_file.write("\n")

            #Compute the K-L divergence
            div = kl_divergence(distr_dict[key1], distr_dict[key2])
            distance_file.write("K-L divergence between the distributions " +
                    str(key1) + ", " + str(key2) + ": ")
            distance_file.write(str(div))
            distance_file.write("\n")
            count_div += 1
            average_div += div

average_distance = average_distance/count
distance_file.write("The average pairwise distance between distributions is: " +
        str(average_distance))
average_div = average_div/count_div
distance_file.write("\n")
distance_file.write("The average pairwise K-L divergence between distributions \
        is: " + str(average_div))


