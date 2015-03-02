import java.io.IOException;

public class eunorth {
	public static void main(String[] args) throws InterruptedException, IOException {
		//Asks user for configuration variables
		MiningConfiguration cc = new MiningConfiguration();
		
		//Make a new crawler and start it
		MatchMiner mc = new MatchMiner(cc);
		mc.Start();
	}
}