import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;

public class MatchCrawler {
	CrawlerConfiguration cc;
	int mathces_in_current_file;
	int next_match_id;
	int start_id;
	
	public MatchCrawler(CrawlerConfiguration cc) {
		this.cc = cc;
		mathces_in_current_file = 0;
		start_id = cc.first_match_id + cc.offset;
		next_match_id = start_id;
	}
	
	public void Start() throws IOException, InterruptedException {
		FileWriter writer = null;
		File file;
		String line, file_path;
		InputStream is;
		BufferedReader br;
		
    while(next_match_id < start_id + cc.matches_to_crawl){
    	Thread.sleep(cc.request_delay_ms);
    	
    	//Create new file if current file is full
    	if (mathces_in_current_file % cc.matches_per_file == 0){
    		if (writer != null)
    			writer.close();
    		file_path = cc.path + "region-" + cc.region + "-start-" + next_match_id + "-size-" + cc.matches_per_file + ".txt";
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
				System.out.println("(" + (next_match_id - start_id + 1) + "/" + cc.matches_to_crawl + ") Match id " + next_match_id + ": File not found");
				next_match_id++;
				continue;
			}
	    		
	    br = new BufferedReader(new InputStreamReader(is));
	    while ((line = br.readLine()) != null)
	    	writer.write(line + "\n");
	    System.out.println("(" + (next_match_id - start_id + 1) + "/" + cc.matches_to_crawl + ") Match id " + next_match_id + ": Crawl OK");
	    mathces_in_current_file++;
	    next_match_id++;
    }
	}
}
