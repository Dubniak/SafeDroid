import os,sys
import json
from androwarn_main import get_PKG, get_API, get_PKG_From_Dex, get_API_From_Dex
import pickle
from contextlib import closing
from flask import Flask
from flask import jsonify


def searchFileForAPIs(file):
	'''
		@param:		File to be searched for API related to pkg
		@rtype:		set of API calls in pkg

	'''
	pkg_dict = pickle.load(open("pkg_dict.file","r"))
	temp_set = []
	try:
		for pkg in get_PKG_From_Dex(file):
			if pkg in pkg_dict:
					temp_set.append(get_API_From_Dex(file,pkg))
		temp_set = [item for sublist in temp_set for item in sublist]
	except Exception as ex:
		print ex
	return temp_set

def getFeatureVectorForFile():
	'''
		@param:		File and set of API features
		@rtype:		Bit vector represting FV
	'''
	file ="classes.dex"
	api_feature_set = pickle.load(open("api_feature_set.file","r"))
	api_set = searchFileForAPIs(file)
	feature_vector = []
	for api in api_feature_set:
		if api in api_set:
			feature_vector.append(1)
		else :
			feature_vector.append(0)
	#return feature_vector
	return jsonify(features = feature_vector)
