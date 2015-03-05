import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.MalformedURLException;

public class MatchMiner extends Thread {
	MiningConfiguration cc;
	int matches_in_current_file;
	int next_match_id;
	
	public MatchMiner(MiningConfiguration cc) {
		this.cc = cc;
		matches_in_current_file = 0;
		next_match_id = cc.match_id;
	}
	
	public void run() {
		try{
		FileWriter writer = null;
		FileWriter stateWriter = null;
		File file;
		String line, file_path;
		InputStream is;
		BufferedReader br;
		matches_in_current_file = cc.matches_per_file; //make sure we start by in a new file
		
	    while(true){
	    	try{Thread.sleep(cc.request_delay_ms/cc.apikeys.size());}
	    	catch(InterruptedException exception){}
	    		
	    	System.out.print("1");
	    	//Fetch data from next match
		    URL url = new URL("https://" + cc.region + ".api.pvp.net/api/lol/" + cc.region + "/v2.2/match/" + next_match_id + "/?includeTimeline=true&api_key=" + cc.getnextkey());

		    try{
		    	is = url.openStream();
		    }
			catch(FileNotFoundException exception){
				next_match_id--;
				continue;
			}
		    catch(IOException exception){
		    	System.out.println("Match id" + next_match_id + ": IO Exception - waiting " + cc.exception_delay_ms + " ms");
				Thread.sleep(cc.exception_delay_ms);
				continue;
		    }
		    System.out.print("2");
		    //Create new file if current file is full
	    	if (matches_in_current_file == cc.matches_per_file){
	    		matches_in_current_file = 0;
	    		if (writer != null){
	    			try{writer.close();}
	    			catch(IOException exception){}
	    		}
	    		file_path = cc.output_path + "region-" + cc.region + "-start-" + next_match_id + "-size-" + cc.matches_per_file + ".txt";
	    		file = new File(file_path);
	    		file.getParentFile().mkdirs();
	    		try{writer = new FileWriter(file);}
	    		catch(IOException exception){}
	    		
	    	}
		    System.out.print(cc.input_path + cc.region + ".txt");
		    //Append data from match into file
		    br = new BufferedReader(new InputStreamReader(is));
		    while ((line = br.readLine()) != null)
		    	writer.write(line + "\n");
		    matches_in_current_file++;
		    try{stateWriter = new FileWriter(cc.input_path + cc.region + ".txt");}
	    		catch(IOException exception){}
	    	stateWriter.write(Integer.toString(next_match_id));
	    	if (writer != null){
	    			try{stateWriter.close();}
	    			catch(IOException exception){}
	    	}
	    	System.out.println(cc.region + " " + next_match_id); // print current match id
		    next_match_id--;
		    

		 
	    }
	    //try{writer.close();}
	    //	catch(IOException exception){}

	}
	catch(MalformedURLException exception){
		System.out.print("fisse");
	}
	catch(Exception penises){
		System.out.print("penises");
	
	}

}
}
