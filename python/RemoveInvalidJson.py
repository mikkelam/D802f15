import json

#Made for the ease of windows tests
def IsolateFileName(s):
    fn = s.split('/')
    return fn[len(fn)-1]

def CreateFilePath(s):
    fn = s.split('/')
    fn[len(fn)-1] = "NEW_" + fn[len(fn)-1]
    fp = '/'.join(fn)
    return fp
    
#Validates and fixes JSON files
def ValidateFile(filepath):
    fn = IsolateFileName(filepath)
    fil = open(filepath, 'r', encoding="ISO-8859-1")

    valid = True
    lin = fil.readlines()
    for l in lin:
        try:
            json.loads(l)
        except ValueError:
            valid = False
            lin.remove(l)
    fil.close
    if valid:
        print("File okay")
        return
    else:
        fil = open(filepath, 'w', encoding="ISO-8859-1")
        for l in lin:
            fil.write(l)
        print("Invalid JSONs found, file remade")
        return


ValidateFile("/home/funder/loldata/region-euw-start-1971881763-size-1000.txt")
    

                
