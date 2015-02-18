import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;

public class MatchMiner {
	MiningConfiguration cc;
	int matches_in_current_file;
	int next_match_id;
	int start_id;
	
	public MatchMiner(MiningConfiguration cc) {
		this.cc = cc;
		matches_in_current_file = 0;
		start_id = cc.first_match_id - cc.mining_offset;
		next_match_id = start_id;
	}
	
	public void Start() throws InterruptedException, IOException {
		FileWriter writer = null;
		File file;
		String line, file_path;
		InputStream is;
		BufferedReader br;
		matches_in_current_file = cc.matches_per_file; //make sure we start by in a new file
		
	    while(next_match_id > start_id - cc.matches_to_mine){
	    	Thread.sleep(cc.request_delay_ms);
	    	
	    	//Create new file if current file is full
	    	if (matches_in_current_file == cc.matches_per_file){
	    		matches_in_current_file = 0;
	    		if (writer != null){
	    			writer.close();
	    		}
	    		file_path = cc.output_path + "region-" + cc.region + "-start-" + next_match_id + "-size-" + cc.matches_per_file + ".txt";
	    		file = new File(file_path);
	    		file.getParentFile().mkdirs();
	    		writer = new FileWriter(file);
	    	}
	    	
	    	//Fetch data from next match
		    URL url = new URL("https://" + cc.region + ".api.pvp.net/api/lol/" + cc.region + "/v2.2/match/" + next_match_id + "/?api_key=" + cc.api_key);
		    try{
		    	is = url.openStream();
		    }
			catch(FileNotFoundException exception){
				System.out.println("(" + (start_id - next_match_id + 1) + "/" + cc.matches_to_mine + ") Match id " + next_match_id + ": File not found");
				next_match_id--;
				continue;
			}
		    catch(IOException exception){
		    	System.out.println("(" + (start_id - next_match_id + 1) + "/" + cc.matches_to_mine + ") Match id " + next_match_id + ": IO Exception - waiting " + cc.exception_delay_ms + " ms");
				Thread.sleep(cc.exception_delay_ms);
				continue;
		    }
		    
		    //Append data from match into file
		    br = new BufferedReader(new InputStreamReader(is));
		    while ((line = br.readLine()) != null)
		    	writer.write(line + "\n");
		    System.out.println("(" + (start_id - next_match_id + 1) + "/" + cc.matches_to_mine + ") Match id " + next_match_id + ": Mining OK");
		    matches_in_current_file++;
		    next_match_id--;
	    }
	    writer.close();
	}
}
