import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;



public class MiningConfiguration {

	//Settings
	String output_path = "mined-data/";
	String region;
	List<String> apikeys;
	int keyindex = 0;

	int request_delay_ms = 2000; //1.5 seconds
	int exception_delay_ms = 60000; //10 minutes
	int match_id; //Match played February 15th 2015. Mining will start here and go backwards.
	
	int matches_per_file_default = 1000;

	int matches_per_file;
	int mining_offset; //offset from first_match_id where mining starts
	int matches_to_mine;



	public MiningConfiguration(String region, int match_id, ArrayList<String> apikeys){
		this.match_id=match_id;
		this.region=region;
		this.apikeys = apikeys;
	}

	public String getnextkey(){
		String key = apikeys.get(keyindex % apikeys.size());
		keyindex++;
		return key;
	}
	
}
