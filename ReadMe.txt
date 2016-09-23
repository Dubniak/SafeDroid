1. cd into the FeatureExtraction directory. Start the python server with the command :
python server.py runserver -d

The server(FES) starts listening on port 5000. The following API has been designed:
URL: http://localhost:5000/upload
Method: POST
Params: 
	"file" : Dexfile

Response:
{
	"features" : []
}

Please test the API using Postman client. Use the sample classes.dex file provided inthe folder. The server replies with a feature vector extracted from the dex file.

2. Once the feature extraction server works, import the Detector in Netbeans (or any other IDE). Run the project. Java program starts
another server on port 4567. The following API has been defined:
URL: http://localhost:4567/upload
Method: POST
Params:
	"dexfile" : Dexfile

Response:
	List of features that make an app malicious

Test the API using Postman.


3. The spark server created by java program has to be killed manually every time the project is re-run. 
ps aux | grep spark
kill -9 PID


The API defined in (2) takes a Dex file as input and returns the feature categories that make an application malicious.