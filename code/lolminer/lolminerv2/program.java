import java.io.IOException;
import java.util.List;
import java.util.ArrayList;


public class program {
	public static void main(String[] args) throws InterruptedException, IOException {
		//Asks user for configuration variables
        ArrayList<String> apikeys = new ArrayList<String>(){{
        add("d3f768b0-5701-4167-b643-d54fc76dd90d");
        add("8f51e649-5553-47d9-a2ac-11e4bf312d8d");
        add("50ddc994-025b-4b15-8b9b-64a71daeefb1");
        add("e57994ec-1493-49d2-af49-29ebb1191446");
        add("5381d6be-ac26-4f77-ac18-b6e70fb7131b");
        add("323b3b30-487b-4fe3-b625-bee0dba0b65e");
        add("9e65270b-a381-4439-b77b-f5db14c8c418");
        add("cd412733-2bdb-4898-ae86-5fc4f28c795e");
        add("67ec6161-94a5-4b33-9b4a-0d6850942019");
    }
};

	MiningConfiguration cc1 = new MiningConfiguration("br", apikeys);
    MiningConfiguration cc2 = new MiningConfiguration("eune", apikeys);
    MiningConfiguration cc3 = new MiningConfiguration("euw", apikeys);
    MiningConfiguration cc4 = new MiningConfiguration("kr", apikeys);
    MiningConfiguration cc5 = new MiningConfiguration("lan", apikeys);
    MiningConfiguration cc6 = new MiningConfiguration("las", apikeys);
    MiningConfiguration cc7 = new MiningConfiguration("na", apikeys);
    MiningConfiguration cc8 = new MiningConfiguration("oce", apikeys);
    MiningConfiguration cc9 = new MiningConfiguration("tr", apikeys);
    MiningConfiguration cc10 = new MiningConfiguration("ru", apikeys);
    
	MatchMiner mc1 = new MatchMiner(cc1);
	mc1.start();
    MatchMiner mc2 = new MatchMiner(cc2);
    mc2.start();
    MatchMiner mc3 = new MatchMiner(cc3);
    mc3.start();
    MatchMiner mc4 = new MatchMiner(cc4);
    mc4.start();
    MatchMiner mc5 = new MatchMiner(cc5);
    mc5.start();
    MatchMiner mc6 = new MatchMiner(cc6);
    mc6.start();
    MatchMiner mc7 = new MatchMiner(cc7);
    mc7.start();
    MatchMiner mc8 = new MatchMiner(cc8);
    mc8.start();
    MatchMiner mc9 = new MatchMiner(cc9);
    mc9.start();
    MatchMiner mc10 = new MatchMiner(cc10);
    mc10.start();



	}
}