from flask import Flask, request
from gen_feature_vector import getFeatureVectorForFile
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def hello_world():
	file = request.files['file']
	file.save("classes.dex")
	return getFeatureVectorForFile()

if __name__ == '__main__':
	app.debug = True
	app.run()