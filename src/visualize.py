#!/usr/bin/env python
'''
Created on Oct 19, 2014
@author: joe
'''
import numpy as np
import argparse
import ast
import matplotlib.pyplot as plt
from calc_tsne import calc_tsne
from tsne import tsne_dist_matrix
from bhattacharyya import bhattacharyya

def read_data_into_dict(file_name):
    start_pages_to_distribution = {}
    with open(file_name, 'r') as f:
        for (line_num, line) in enumerate(f):
            if line_num%2==0:
                start_page = line.strip().split('/')[-1]
            else:
                start_pages_to_distribution[start_page] = dict(ast.literal_eval(line))
    return start_pages_to_distribution

def gen_sparse_features_from_distrs(distrs):
    '''Create a feature vector from a set of distributions.
    Each element in the feature vector corresponds to the number of times
    a distribution visisted that page
    '''
    allkeys = set()
    for distr in distrs:
        allkeys |= set(distrs[distr].keys())
    index_of = dict([(v,k) for (k,v) in enumerate(allkeys)])
        
    features = np.zeros((len(distrs),len(allkeys)))
    for (i, distr) in enumerate(distrs):
        for key, value in distrs[distr].items():
            features[i, index_of[key]] = value
    return features

def distance_matrix(distrs):
    distrs = distrs.values()
    distances = np.zeros((len(distrs), len(distrs)))
    for i in xrange(len(distrs)):
        for j in xrange(len(distrs)):
            distances[i,j] = bhattacharyya(distrs[i], distrs[j])
    return distances

class Plotter:

    def __init__(self, features):
        self.features=features
        
    def plot(self):
        x = self.features[:,0]
        y = self.features[:,1]

        fig = plt.figure()
        fig.suptitle('Distributions reached starting from random pages')
        ax = fig.add_subplot(1,1,1)
        ax.scatter(x, y)
        
    def show(self):
        plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', default='../results/data.txt', help='location of file that contains data')
    parser.add_argument('--dist-matrix', action='store_true', help='include this option if the data file is a distance matrix instead of features')
    args = parser.parse_args()
    use_dist_matrix = args.dist_matrix
    distrs = read_data_into_dict(args.data)
    if use_dist_matrix:
        distances = distance_matrix(distrs)
        distances = distances + 1
        plotting_data = tsne_dist_matrix(distances, perplexity=10)
    else:
        sparse_features = gen_sparse_features_from_distrs(distrs)
        plotting_data = calc_tsne(sparse_features, PERPLEX=30)
    c = Plotter(plotting_data)
    c.plot()
    c.show()
    
if __name__ == '__main__':
    main()
