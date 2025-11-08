from pickle import *
my_dict={"Phisics": 5,"Chemistry": 3,"Obg": 5}

with open("text.bin","rb") as file:
    subj=load(file)
    for i in subj:
        print(i, subj[i])
