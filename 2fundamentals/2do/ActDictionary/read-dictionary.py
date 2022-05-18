import pickle

with open('dictionary.bin','rb') as fh:
        d = pickle.load(fh) 

print(type(d))
print(d)

print('done...')