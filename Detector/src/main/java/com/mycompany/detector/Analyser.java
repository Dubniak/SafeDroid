package com.mycompany.detector;

import java.io.InputStream;
import java.util.List;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.servlet.MultipartConfigElement;
import spark.Spark;
import static spark.Spark.get;
import static spark.Spark.post;

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