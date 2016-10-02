import os,sys
import json
from androwarn_main import get_PKG, get_API, get_PKG_From_Dex, get_API_From_Dex
import pickle
from contextlib import closing
from flask import Flask
from flask import jsonify
from timeit import default_timer as timer


def writeMetrics(timer,place):
  f = open('perfomance_measurments','a')
  f.write(place+":"+"{0:.4f}".format(timer)+" sec.\n")
  f.close()

def searchFileForAPIs(file):
	'''
		@param:		File to be searched for API related to pkg
		@rtype:		set of API calls in pkg

	'''
	start2 = counter = 0.0
	start = timer();
	pkg_dict = pickle.load(open("pkg_dict.file","r"))
	temp_set = []
	try:
		for pkg in get_PKG_From_Dex(file):
			#end1 = timer();
			start2 = timer()
			if pkg in pkg_dict:
					temp_set.append(get_API_From_Dex(file,pkg))
			end2 = timer()
			counter = (end2 - start2) + counter
		end = timer();
		temp_set = [item for sublist in temp_set for item in sublist]
	except Exception as ex:
		print ex
	writeMetrics(end-start,"get_PKG_From_Dex")
	#writeMetrics(counter,"get_API_From_Dex")
	writeMetrics((end-start)-counter,"get_API_From_Dex")
	return temp_set

def getFeatureVectorForFile(start1):
	'''
		@param:		File and set of API features
		@rtype:		Bit vector represting FV
	'''
	file ="classes.dex"
	
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
	return jsonify(features = feature_vector)
