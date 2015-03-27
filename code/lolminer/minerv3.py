import requests
from threading import Thread
import time

class Miner(Thread):
    def __init__(self, keys, region, start_match):
        Thread.__init__(self, target=self.mine)
        self.start_match = start_match
        self.keys = keys
        self.region = region
        self.current_match = start_match
        self.keyidx = 0

    def mine(self):
        f = open(self.region + str(self.start_match) + ".json", 'a+')
        while True:
            time.sleep(0.5)
            url = "https://" + self.region + ".api.pvp.net/api/lol/" + self.region + "/v2.2/match/" + str(self.current_match) + "/?includeTimeline=true&api_key=" + self.next_key();
            self.current_match -= 1

            try:
                r = requests.get(url)
                if r.status_code == 200:
                    f.write(r.text.encode('UTF-8')+'\n')
                elif r.status_code != 404:
                    print r.status_code, self.region
            except Exception, e:
                print e
        
        
    def next_key(self):
        self.keyidx += 1
        self.keyidx = (self.keyidx % len(keys))
        return keys[self.keyidx]
        
keys = ['d3f768b0-5701-4167-b643-d54fc76dd90d','8f51e649-5553-47d9-a2ac-11e4bf312d8d',
        '50ddc994-025b-4b15-8b9b-64a71daeefb1','e57994ec-1493-49d2-af49-29ebb1191446',
        '5381d6be-ac26-4f77-ac18-b6e70fb7131b','323b3b30-487b-4fe3-b625-bee0dba0b65e',
        '9e65270b-a381-4439-b77b-f5db14c8c418','cd412733-2bdb-4898-ae86-5fc4f28c795e',
        '67ec6161-94a5-4b33-9b4a-0d6850942019']

m1 = Miner(keys,"br", 496113016)
m2 = Miner(keys,"eune", 1773363447)
m3 = Miner(keys,"euw", 2032894042)
# m4 = Miner(keys,"kr",asdasdas )
m5 = Miner(keys,"lan", 152004918)
m6 = Miner(keys,"las", 192545631)
m7 = Miner(keys,"na", 1773544384)
m8 = Miner(keys,"oce", 83823308)
m9 = Miner(keys,"tr", 234480573)
m10 = Miner(keys,"ru", 45762142)
m1.start()
m2.start()
m3.start()
m5.start()
m6.start()
m7.start()
m8.start()
m9.start()
m10.start()

