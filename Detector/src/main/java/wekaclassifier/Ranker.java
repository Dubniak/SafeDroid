package wekaclassifier;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

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
            for (int feature=0; feature<temp.size(); feature++)
                rankedFeatureVector.add(rankedFeatures.get(feature));
            
            return rankedFeatureVector;
            
        } catch (FileNotFoundException ex) {
            Logger.getLogger(Ranker.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
