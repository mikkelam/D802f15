import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;


public class MiningConfiguration {

	//Settings
	String api_key;
	String api_key_path = "api-keys/";
	String output_path = "mined-data/";
	String region = "euw";
	int request_delay_ms = 2000; //1.5 seconds
	int exception_delay_ms = 600000; //10 minutes
	int first_match_id = 1971892117; //Match played February 15th 2015. Mining will start here and go backwards.
	
	int matches_per_file_default = 1000;
	int mining_offset_default = 0;
	int matches_to_mine_default = 200000;

	int matches_per_file;
	int mining_offset; //offset from first_match_id where mining starts
	int matches_to_mine;

	public MiningConfiguration(){
		
		Scanner in = new Scanner(System.in);
		String str_input;
		
	    //Get API file
		while (true){
			System.out.print("Enter the name of your API key file (e.g. 'key1.txt'): ");
			String api_key_file_name = in.nextLine();
			if (api_key_file_name.equals("")){
				System.out.print("\nWARNING! You did not provide a correct filename for your api key file.\n");
				continue;
			}
			String api_key_file_path = api_key_path + api_key_file_name;
			LoadApiKey(api_key_file_path);
			if (api_key == null || api_key == ""){
				System.out.print("\nSomething went wrong. Mare sure the api-key is stored correctly as raw text at: " + api_key_file_path + "\n");
				continue;
			}
			break;
		}
		
	    //Get matches per file
		System.out.print("\nMatches per file (default "+ matches_per_file_default + "): ");
		str_input = in.nextLine();
		matches_per_file = matches_per_file_default;
		if (tryParseInt(str_input))
			matches_per_file = Integer.parseInt(str_input);
		else if (!str_input.equals(""))
			System.out.print("\nWARNING! Could not parse matches per file, using value: " + matches_per_file);

		//Get mining offset
		System.out.print("\nMining offset (default " + mining_offset_default + "): ");
		str_input = in.nextLine();
		mining_offset = mining_offset_default;
		if (tryParseInt(str_input))
			mining_offset = Integer.parseInt(str_input);
		else if (!str_input.equals(""))
			System.out.print("\nWARNING! Could not parse crawl offset, using value: " + mining_offset);
		
		//Get matches to mine
		System.out.print("\nMatches to mine (default " + matches_to_mine_default + "): ");
		str_input = in.nextLine();
		matches_to_mine = matches_to_mine_default;
		if (tryParseInt(str_input))
			matches_to_mine = Integer.parseInt(str_input);
		else if (!str_input.equals(""))
			System.out.print("\nWARNING! Could not parse matches to mine, using value: " + matches_to_mine);
		
		in.close();
	}
	
	void LoadApiKey(String file){
		//load API key file
	    try {
	    	BufferedReader br = new BufferedReader(new FileReader(file));
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
