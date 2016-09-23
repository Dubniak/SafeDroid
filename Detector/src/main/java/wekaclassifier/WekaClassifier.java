/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package wekaclassifier;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.HttpVersion;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntity;
import org.apache.http.entity.mime.content.ContentBody;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.CoreProtocolPNames;
import org.apache.http.util.EntityUtils;
import org.apache.sling.commons.json.JSONArray;
import org.apache.sling.commons.json.JSONException;
import org.apache.sling.commons.json.JSONObject;

import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.trees.RandomForest;
import weka.core.Attribute;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.ProtectedProperties;
import weka.core.SparseInstance;
import weka.core.converters.CSVLoader;
import weka.core.converters.ConverterUtils;

/**
 *
 * @author rohitgoyal
 */
public class WekaClassifier {

    /**
     * @param args the command line arguments
     */
    
    Instances data;
    Classifier classifier;
    List<Integer> sparseFeatureVector;

    public void loadData(String fileName) {
        try {
            ConverterUtils.DataSource source = new ConverterUtils.DataSource(fileName);
            data = source.getDataSet();
            if (data.classIndex() == -1) {
                data.setClassIndex(data.numAttributes() - 1);
            }
            buildModel();
        } catch (Exception ex) {
            Logger.getLogger(WekaClassifier.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    public void buildModel() throws Exception {
        RandomForest rf = new RandomForest();
        rf.buildClassifier(data);
        classifier = rf;
        try ( // export the model to a file
                ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("rForest.model"))) {
            oos.writeObject(rf);
            oos.flush();
        } catch (Exception ex) {
            Logger.getLogger(WekaClassifier.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void evaluateModel() throws Exception {
        Evaluation eval = new Evaluation(data);
        eval.crossValidateModel(classifier, data, 2, new Random(1));
        System.out.println(eval.toSummaryString("Results", false));
    }

    public void classifyInstance(Instances unlabeledData) {
        try {
            //ConverterUtils.DataSource source = new ConverterUtils.DataSource(fileName);
            //Instances unlabeledData = source.getDataSet();
            unlabeledData.setClassIndex(unlabeledData.numAttributes() - 1);
            double clsLabel = classifier.classifyInstance(unlabeledData.firstInstance());
            System.out.println("Class label is " + clsLabel);
            
        } catch (Exception ex) {
            Logger.getLogger(WekaClassifier.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    public List<Integer> postFile() throws IOException {
        HttpClient httpclient = new DefaultHttpClient();
        httpclient.getParams().setParameter(CoreProtocolPNames.PROTOCOL_VERSION, HttpVersion.HTTP_1_1);

        HttpPost httppost = new HttpPost("http://localhost:5000/upload");
        File file = new File("classes1.dex");

        MultipartEntity mpEntity = new MultipartEntity();
        ContentBody cbFile = new FileBody(file, "multipart/form-data");
        mpEntity.addPart("file", cbFile);

        httppost.setEntity(mpEntity);
        System.out.println("executing request " + httppost.getRequestLine());
        HttpResponse response = httpclient.execute(httppost);
        HttpEntity resEntity = response.getEntity();

        System.out.println(response.getStatusLine());
        if (resEntity != null) {
            try {
                //System.out.println(EntityUtils.toString(resEntity));
                JSONObject result = new JSONObject(EntityUtils.toString(resEntity));
                JSONArray fv_json = (JSONArray) result.get("features");
                List<Integer> fv = new ArrayList<>();
                sparseFeatureVector = new ArrayList<>();

                for(int i =0 ; i < fv_json.length();i++){
                    fv.add((Integer) fv_json.get(i));
                    if (fv.get(i) != 0) {
                        sparseFeatureVector.add(i);
                    }
                }
                return fv;
            } catch (JSONException ex) {
                Logger.getLogger(WekaClassifier.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        httpclient.getConnectionManager().shutdown();
        return null;
    }

    public Instances arrayToDataset(List<Integer> fv) {
        ArrayList<Attribute> atts = new ArrayList<>();
        List<Instance> instances = new ArrayList<>();
        int numDimensions = 744;
        for (int dim = 0; dim < numDimensions; dim++) {
            
            if (dim == 0) {
                instances.add(new SparseInstance(numDimensions));
            }
            if(dim == 743){
                List<String> values = new ArrayList<>();
                values.add("0");
                values.add("1");
                Attribute current = new Attribute("Attribute" + dim, values);
                instances.get(0).setMissing(current);
                atts.add(current);
            }
            else{
                Attribute current = new Attribute("Attribute" + dim, dim);
                instances.get(0).setValue(current, fv.get(dim));
                atts.add(current);
            }
        }

        Instances newDataset = new Instances("Dataset", atts, instances.size());

        for (Instance inst : instances) {
            newDataset.add(inst);
        }
        return newDataset;
    }
    
    
    public List<String> testAPI(){
        try {
            WekaClassifier wc = this;
            
            try {
                ObjectInputStream ois = new ObjectInputStream(new FileInputStream("rForest.model"));
                wc.classifier = (Classifier) ois.readObject();
            } catch (IOException | ClassNotFoundException ex) {
                Logger.getLogger(WekaClassifier.class.getName()).log(Level.SEVERE, null, ex);
                wc.loadData("feature_set.arff");
            }
            wc.classifyInstance(wc.arrayToDataset(wc.postFile()));
            Ranker ranker = new Ranker();
            FeatureList fl = new FeatureList();
            return fl.getFeatureNames(ranker.getRanksForFeatureSet(wc.sparseFeatureVector));
            
        } catch (IOException ex) {
            Logger.getLogger(WekaClassifier.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
