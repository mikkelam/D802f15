import java.io.IOException;

public class program {
	public static void main(String[] args) throws InterruptedException, IOException {
		//Asks user for configuration variables
		CrawlerConfiguration cc = new CrawlerConfiguration();
		
		//Make a new crawler and start it
		MatchCrawler mc = new MatchCrawler(cc);
		mc.Start();
	}
}