import pickle
import os

def save_me(evalErr, trainErr, model, description, name):
	#takes float, float, logisticregressionmodel, string, string 

	savepath = "../../results/"
	mypath = savepath + name
	if not os.path.isdir(mypath):
 		os.makedirs(mypath)

 	pickle.dump( model, open(mypath + "model.p", "wb" ) )
	fr = open(mypath + name + ".txt", 'w+')
	fr.write(description + "Training Error on Evaluation Data = " + str(evalErr) + "\nTraining Error on Evaluation Data = " + str(trainErr))