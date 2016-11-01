import os,sys
import json
from androwarn_main import * #get_PKG, get_API, get_PKG_From_Dex, get_API_From_Dex
import pickle
from contextlib import closing
from flask import Flask
from flask import jsonify
from timeit import default_timer as timer


def writeMetrics(timer,place):
  f = open('perfomance_measurments','a')
  f.write(place+":"+"{0:.4f}".format(timer)+" sec.\n")
  f.close()

def writeIterations(it1,it2):
	f = open('perfomance_measurments','a')
	f.write("External for loop:"+str(it1)+".\n"+"If condition:"+str(it2)+".\n")
	f.close()

def writeBegin():
	f = open('perfomance_measurments','a')
	f.write("***********\n")
	f.close()

def searchFileForAPIs(file):
	'''
		@param:		File to be searched for API related to pkg
		@rtype:		set of API calls in pkg
	'''
	f = open('temp_set','w+')
	it1 = it2 = 0 
	start2 = counter = end = 0.0
	start = timer();
	pkg_dict = pickle.load(open("pkg_dict.file","r"))
	temp_set = []
	pkg_list = get_PKG_From_Dex(file)
	d, x = get_API_From_Dex_Testing(file) #MARIOS
	try:
		for pkg in pkg_list:
			it1 += 1
			start2 = timer()
			if pkg in pkg_dict:
					it2 += 1
					#temp_set.append(get_API_From_Dex(file,pkg)) #ROHID 
					temp_set.append(get_API_From_Dex_Part_II(x,pkg)) #MARIOS
			end2 = timer()
			counter = (end2 - start2) + counter
		end = timer();
		temp_set = [item for sublist in temp_set for item in sublist]
	except Exception as ex:
		print ex
	writeIterations(it1,it2)
	writeMetrics(end-start,"get_PKG_From_Dex")
	writeMetrics((end-start)-counter,"get_API_From_Dex")
	f.close()
	return temp_set

def getFeatureVectorForFile(start1):
	'''
		@param:		File and set of API features
		@param:		start1 used for metrics MA
		@rtype:		Bit vector represting FV
	'''
	file ="classes.dex"
	writeBegin()
	start = timer()
	api_feature_set = pickle.load(open("api_feature_set.file","r"))
	api_set = searchFileForAPIs(file)
	feature_vector = []
	for api in api_feature_set:
		if api in api_set:
			feature_vector.append(1)
		else :
			feature_vector.append(0)
	#return feature_vector
	end = timer()
	writeMetrics(end-start,"getFeatureVectorForFile")
	writeMetrics(end-start1,"server")
	#writeVectorToFile(feature_vector)
	return jsonify(features = feature_vector)
