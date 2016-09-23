/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package wekaclassifier;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author rohitgoyal
 */
public class Ranker {
    ArrayList<Integer> rankedFeatures;
    
    public List<Integer> getRanksForFeatureSet(List<Integer> featureBitVector){
        try {
            //read ranks from file
            Scanner scanner = new Scanner(new File("feature_rank.file"));
            rankedFeatures = new ArrayList<>();
            while(scanner.hasNext()){
                rankedFeatures.add(scanner.useDelimiter(",").nextInt());
            }
            scanner.close();
            List<Integer> temp = new ArrayList<>();
            for(Integer feature: featureBitVector){
                temp.add(rankedFeatures.indexOf(feature));
            }
            Collections.sort(temp);
            List<Integer> rankedFeatureVector = new ArrayList<>();
            for(Integer feature: temp){
                rankedFeatureVector.add(rankedFeatures.get(feature));
            }
            return rankedFeatureVector;
            
        } catch (FileNotFoundException ex) {
            Logger.getLogger(Ranker.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
}
