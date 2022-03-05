import pickle

def write_dump():

    dog_dict = {"Ozzy": 3, "Filou": 8, "Luna": 3}
    filename = "dogs"
    outfile = open(filename, "wb")
    pickle.dump(dog_dict, outfile)
    outfile.close()

def read_load():

    filename = "dogs"
    infile = open(filename, "rb")
    new_dict = pickle.load(infile)
    print (new_dict)
    infile.close()

write_dump()
read_load()