/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package wekaclassifier;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author rohitgoyal
 */
public class FeatureList {
    List<String> featureList;
    List<Integer> featureCategoryList;
    HashMap<Integer, String> descriptionMap;

    public FeatureList() {
        this.descriptionMap = new HashMap<>();
        createDescriptionMap();
    }
    
    
    
    public List<String> getFeatureNames(List<Integer> featureIndices){
        try {
            //read feature names from file
            Scanner scanner = new Scanner(new File("feature_list.file"));
            featureList = new ArrayList<>();
            featureCategoryList = new ArrayList<>();
            while(scanner.hasNext()){
                String[] tokens = scanner.next().split(",");
                featureList.add(tokens[0]);
                featureCategoryList.add(Integer.parseInt(tokens[1]));
            }
            scanner.close();
            List<String> featureCategoryNames= new ArrayList<>();
            List<Integer> featureCategories = new ArrayList<>();
            for (Integer featureIndex : featureIndices) {
                //featureNames.add(featureList.get(featureIndex));
                featureCategories.add(featureCategoryList.get(featureIndex));
            }
            HashMap<Integer,Integer> categoryCounterMap = new HashMap<>();
            for(Integer category: featureCategories){
                if(categoryCounterMap.containsKey(category)){
                    Integer count = categoryCounterMap.get(category);
                    categoryCounterMap.put(category, ++count);
                }
                else{
                    categoryCounterMap.put(category,1);
                }
            }
            ValueComparator bvc = new ValueComparator(categoryCounterMap);
            TreeMap<Integer,Integer> sorted_map = new TreeMap<>(bvc);
            sorted_map.putAll(categoryCounterMap);
            for (Map.Entry<Integer, Integer> entrySet : sorted_map.entrySet()) {
                Integer key = entrySet.getKey();
                featureCategoryNames.add(descriptionMap.get(key));
            }
            return featureCategoryNames;
        } catch (FileNotFoundException ex) {
            Logger.getLogger(FeatureList.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
   
    
    public void createDescriptionMap(){
        descriptionMap.put(0, "Suspicious methods called");
        descriptionMap.put(1, "Suspicious utility methods called");
        descriptionMap.put(2, "Suspicious network activity");
        descriptionMap.put(3, "Suspicious Ads related activity");
        descriptionMap.put(4, "Retrieves personal or device information");
        descriptionMap.put(5, "Suspicious system services activity");
    }
    
}


class ValueComparator implements Comparator<Integer> {
    Map<Integer, Integer> base;

    public ValueComparator(Map<Integer, Integer> base) {
        this.base = base;
    }

    // Note: this comparator imposes orderings that are inconsistent with
    // equals.
    public int compare(Integer a, Integer b) {
        if (base.get(a) >= base.get(b)) {
            return -1;
        } else {
            return 1;
        } // returning 0 would merge keys
    }
}
