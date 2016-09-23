/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.detector;

import java.io.File;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import javax.servlet.MultipartConfigElement;
import spark.Response;
import spark.Spark;
import static spark.Spark.get;
import static spark.Spark.post;

/**
 *
 * @author rohitgoyal
 */
public class Analyser {
    public static void main(String[] args) {
        Spark.stop();
        get("/analyse", (req, res) -> {
            long startTime = System.currentTimeMillis();
            wekaclassifier.WekaClassifier test = new wekaclassifier.WekaClassifier();
            List<String> response = test.testAPI();
            long endTime = System.currentTimeMillis();
            System.out.println("Time taken :"+ (endTime-startTime));
            return response;
        });
        post("/upload", (request, response) -> {
        request.attribute("org.eclipse.jetty.multipartConfig", new MultipartConfigElement("/temp"));
        try (InputStream is = request.raw().getPart("dexfile").getInputStream()) {
            // Use the input stream to create a file
            final Path destination = Paths.get("classes1.dex");
            Files.copy(is, destination);
        }
            long startTime = System.currentTimeMillis();
            wekaclassifier.WekaClassifier test = new wekaclassifier.WekaClassifier();
            List<String> response1 = test.testAPI();
            long endTime = System.currentTimeMillis();
            System.out.println("Time taken :"+ (endTime-startTime));
            return response1;
        });
    }
}
