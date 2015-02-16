import java.util.Scanner;


public class CrawlerConfiguration {

	//Settings
	String api_key = "d3f768b0-5701-4167-b643-d54fc76dd90d";
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
		
		System.out.print("\nOutput path (default C://lol-crawl): ");
		path = in.nextLine();
		path = path.equals("") ? "C://lol-crawl" : path;
		if (!path.endsWith("/"))
			path += "/";
		
		System.out.print("Matches per file (default 100): ");
		str_input = in.nextLine();
		matches_per_file = 100;
		if (tryParseInt(str_input))
			matches_per_file = Integer.parseInt(str_input);
		
		System.out.print("\nCrawl offset (default 0): ");
		str_input = in.nextLine();
		offset = 0;
		if (tryParseInt(str_input))
			offset = Integer.parseInt(str_input);
		
		System.out.print("\nMatches to crawl (default 1000): ");
		str_input = in.nextLine();
		matches_to_crawl = 1000;
		if (tryParseInt(str_input))
			matches_to_crawl = Integer.parseInt(str_input);
		
		in.close();
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
