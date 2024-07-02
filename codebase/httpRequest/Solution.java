import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.io.OutputStream;
import java.io.InputStream;

public class Solution {
    public static void main(String[] args) throws MalformedURLException, IOException {
        URL url = new URL("http://www.example.com/api");
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setDoOutput(true);

        // Set the request body to an XML string
        String xmlString = "<root><element>value</element></root>";
        byte[] bytes = xmlString.getBytes("UTF-8");
        connection.setRequestProperty("Content-Length", Integer.toString(bytes.length));
        connection.setRequestProperty("Content-Type", "application/xml");
        OutputStream outputStream = connection.getOutputStream();
        outputStream.write(bytes);
        outputStream.close();

        // Get the response from the server
        InputStream inputStream = connection.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        reader.close();

        connection.disconnect(); // Add this line to fix the resource leak issue
    }
}