import pickle

sample_list = ["sdsd", 2, 3]
file_name = "sample.pkl"

open_file = open(file_name, "wb")
pickle.dump(sample_list, open_file)
open_file.close()

open_file = open(file_name, "rb")
loaded_list = pickle.load(open_file)
open_file.close()


sample_list2=["22sds"]
sample_list.append(sample_list2)
open_file = open(file_name, "wb")
pickle.dump(sample_list, open_file)
open_file.close()

open_file = open(file_name, "rb")
loaded_list = pickle.load(open_file)
open_file.close()

print(loaded_list)

chain=[]
print(len(chain))






