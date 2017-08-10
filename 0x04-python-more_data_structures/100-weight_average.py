#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    product_sum = 0
    total_weight = 0
    for score, weight in my_list:
        product_sum += (score * weight)
        total_weight += weight
    avg_weight = product_sum / total_weight
    return avg_weight
