#!/usr/bin/python

import os
import sys
import re
from sets import Set


requirement_folder_paht = '/Users/evermal/git/tse2015/npl_tools/datasets/implementation_vs_without_classification/filtered_top_features'

positive_feature_regex = ".*1-SW-(.*),IMPLEMENTATION\)\s*(\d\.\d\d\d\d)"
negative_feature_regex = ".*1-SW-(.*),IMPLEMENTATION\)\s*\-(\d\.\d\d\d\d)"
all_feature_regex = ".*1-SW-(.*),IMPLEMENTATION.*(\d\.\d\d\d\d)"

feature_average = 0
for root, dirs, files in os.walk(requirement_folder_paht):
    for f in files:
        absolute_file_name = os.path.join(root, f)
        feature_set = Set([])
        
        with open (absolute_file_name,'r') as filtered_top_features_file:
                for line in filtered_top_features_file:
                    # print line
                    feature_matcher = re.match(all_feature_regex, line)
                    if feature_matcher is not None:
                        # counter = counter + 1 
                        # print feature_matcher.group(1)
                        # print feature_matcher.group(2)
                        feature_set.add(feature_matcher.group(1))
                print f
                print len(feature_set)
                feature_average = feature_average + len(feature_set)



feature_set = Set([])
for root, dirs, files in os.walk(requirement_folder_paht):
    for f in files:
        absolute_file_name = os.path.join(root, f)
        with open (absolute_file_name,'r') as filtered_top_features_file:
                for line in filtered_top_features_file:
                    feature_matcher = re.match(all_feature_regex, line)
                    if feature_matcher is not None:
                        feature_set.add(feature_matcher.group(1))
                

print 'average of unique features:' + str(feature_average/10)
print 'total unique features:' + str(len(feature_set))



feature_average = 0
for root, dirs, files in os.walk(requirement_folder_paht):
    for f in files:
        absolute_file_name = os.path.join(root, f)
        feature_set = Set([])
        
        with open (absolute_file_name,'r') as filtered_top_features_file:
                for line in filtered_top_features_file:
                    # print line
                    feature_matcher = re.match(positive_feature_regex, line)
                    if feature_matcher is not None:
                        # print feature_matcher.group(1)
                        # print feature_matcher.group(2)
                        feature_set.add(feature_matcher.group(1))
                print f
                print len(feature_set)
                feature_average = feature_average + len(feature_set)



feature_set = Set([])
for root, dirs, files in os.walk(requirement_folder_paht):
    for f in files:
        absolute_file_name = os.path.join(root, f)
        with open (absolute_file_name,'r') as filtered_top_features_file:
                for line in filtered_top_features_file:
                    feature_matcher = re.match(positive_feature_regex, line)
                    if feature_matcher is not None:
                        feature_set.add(feature_matcher.group(1))
                

print 'average of unique positive features:' + str(feature_average/10)
print 'total unique positive features:' + str(len(feature_set))


feature_average = 0
for root, dirs, files in os.walk(requirement_folder_paht):
    for f in files:
        absolute_file_name = os.path.join(root, f)
        feature_set = Set([])
        
        with open (absolute_file_name,'r') as filtered_top_features_file:
                for line in filtered_top_features_file:
                    # print line
                    feature_matcher = re.match(negative_feature_regex, line)
                    if feature_matcher is not None:
                        # print feature_matcher.group(1)
                        # print feature_matcher.group(2)
                        feature_set.add(feature_matcher.group(1))
                print f
                print len(feature_set)
                feature_average = feature_average + len(feature_set)



feature_set = Set([])
for root, dirs, files in os.walk(requirement_folder_paht):
    for f in files:
        absolute_file_name = os.path.join(root, f)
        with open (absolute_file_name,'r') as filtered_top_features_file:
                for line in filtered_top_features_file:
                    feature_matcher = re.match(negative_feature_regex, line)
                    if feature_matcher is not None:
                        feature_set.add(feature_matcher.group(1))
                

print 'average of unique negative features:' + str(feature_average/10)
print 'total unique negative features:' + str(len(feature_set))


