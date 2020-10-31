import h5py

dkeys = []  # labels of each entry in the h5
W = []      # dataset container

with h5py.File('ota_6mods8types_1e4.hdf5', 'r') as f:
    for key in f.keys():
        dkeys.append(key)
        W.append(f[key][:])
f.close()

# W can be now split into training, validation,and testing sets to run your ML algorithm on it
