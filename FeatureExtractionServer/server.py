from flask import Flask, request
from gen_feature_vector import getFeatureVectorForFile
app = Flask(__name__)
from timeit import default_timer as timer
import logging

@app.route('/upload', methods=['POST'])
def hello_world():
	start = timer()
	file = request.files['file']
	file.save("classes.dex")
	return getFeatureVectorForFile(start)

if __name__ == '__main__':
	app.debug = True
	app.run()