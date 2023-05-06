import random
import numpy as np
import matplotlib.pyplot as plt

def get_bucket(fixed_bucket_size, min_, max_):
    bucket = []
    for i in range(fixed_bucket_size):
        bucket.append(random.randint(min_, max_))
    return bucket


def get_init_centroids(num_cl, min_, max_):
    rand_list = []
    for i in range(num_cl):
        rand_list.append(random.randint(min_, max_))
    return rand_list


def get_new_centroids(cluster_dict):
    new_centroids= []
    for each in cluster_dict.keys():
        sum_=0
        length = len(cluster_dict[each])
        for each_value in cluster_dict[each]:
            sum_+=each_value
        avg = sum_/length
        new_centroids.append(avg)
    return new_centroids


def findClusters(num_cl, bucket):
    init_centroids = get_init_centroids(num_cl, min(bucket), max(bucket))
    optimal_state= False
    cluster_dict = {}
    centroids = init_centroids
    while(optimal_state == False):
        cluster_dict.clear()
        for value in bucket:
            min_dist = 1000000000000000
            which_centroid = 1000000000000000
            for each in centroids:
                if(abs(each-value)<min_dist):
                    min_dist=abs(each-value)
                    which_centroid = each
            if(which_centroid not in cluster_dict):
                cluster_dict[which_centroid] = [value]
            else:
                cluster_dict[which_centroid].append(value)
                
        new_centroids = get_new_centroids(cluster_dict)
        if new_centroids == centroids:
            optimal_state=True
        centroids = new_centroids
    clusters = []
    for each in cluster_dict.keys():
        clusters.append(cluster_dict[each])
    return clusters, init_centroids


def kMeans_(k, fixed_bucket_size, min_bucket_val, max_bucket_val):
    bucket = get_bucket(fixed_bucket_size, min_bucket_val, max_bucket_val)
    output, init_centroids = findClusters(k,bucket)
    from plot import plotTheClusters, plot_general
    return plot_general(bucket), plotTheClusters(output)



