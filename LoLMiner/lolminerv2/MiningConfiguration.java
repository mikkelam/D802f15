import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;



public class MiningConfiguration {
	int match_id;
	int keyindex = 0;
	String input_path = "miner-state/";
	String output_path = "mined-data/";
	String region;
	List<String> apikeys;

	//Settings
	int request_delay_ms = 2000; //2 seconds
	int exception_delay_ms = 60000; //1 minutes 
	int matches_per_file = 1000;

	public MiningConfiguration(String region, ArrayList<String> apikeys){
		this.region=region;
		this.apikeys = apikeys;

		try {
	    	BufferedReader br = new BufferedReader(new FileReader(input_path + region + ".txt"));
	        int line = Integer.parseInt(br.readLine());
        	if (line != 0)
        		this.match_id = line;
        	br.close();
        	System.out.print("MatchID loaded :" + this.match_id + "\n");
	    }
	    catch (IOException e) {
		}
		
	}

	public String getnextkey(){
		String key = apikeys.get(keyindex % apikeys.size());
		keyindex++;
		return key;
	}
	void LoadRegionID(String file){
		//load API key file
	    
	}
	
}
