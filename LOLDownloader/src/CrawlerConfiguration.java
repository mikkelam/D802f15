import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;


public class CrawlerConfiguration {

	//Settings
	String api_key;
	String api_key_file = "api-key.txt";
	String region = "euw";
	int request_delay_ms = 1500;
	int first_match_id = 1971892117; //Match played February 15th 2015. Crawl will start here and go backwards.

	int matches_per_file;
	int offset;
	int matches_to_crawl;
	String path;

	public CrawlerConfiguration(){
		
		Scanner in = new Scanner(System.in);
		String str_input;
		//Get output path
		System.out.print("\nOutput path (default C://lol-crawl): ");
		path = in.nextLine();
		path = path.equals("") ? "C://lol-crawl" : path;
		if (!path.endsWith("/"))
			path += "/";
		
		LoadApiKey();
		if (api_key == null || api_key == ""){
			System.out.print("Something went wrong. Mare sure the api-key is stored correctly as raw text in: " + path + api_key_file);
			System.exit(0);
		}
		
	    //Get matches per file
		System.out.print("Matches per file (default 100): ");
		str_input = in.nextLine();
		matches_per_file = 100;
		if (tryParseInt(str_input))
			matches_per_file = Integer.parseInt(str_input);
		
		//Get crawl offset
		System.out.print("\nCrawl offset (default 0): ");
		str_input = in.nextLine();
		offset = 0;
		if (tryParseInt(str_input))
			offset = Integer.parseInt(str_input);
		
		//Get matches to crawl
		System.out.print("\nMatches to crawl (default 1000): ");
		str_input = in.nextLine();
		matches_to_crawl = 1000;
		if (tryParseInt(str_input))
			matches_to_crawl = Integer.parseInt(str_input);
		
		in.close();
	}
	
	void LoadApiKey(){
		//load API key file
	    try {
	    	BufferedReader br = new BufferedReader(new FileReader(path + api_key_file));
	        String line = br.readLine();
        	if (line != null)
        		api_key = line;
        	br.close();
	    }
	    catch (IOException e) {
		}
	}
	
	boolean tryParseInt(String value)  
	{  
	     try  
	     {  
	         Integer.parseInt(value);  
	         return true;  
	      } catch(NumberFormatException nfe)  
	      {  
	          return false;  
	      }  
	}
	
}
