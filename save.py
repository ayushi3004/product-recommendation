#################################################
# This script reads image feature vectors from a folder
# and saves the image similarity scores in json file
#################################################

#################################################
# Imports and function definitions
#################################################

import pandas as pd
import os
#################################################

#################################################
# This function; 
# Reads all image feature vectores stored in /feature-vectors/*.npz
# Adds them all in Annoy Index
# Builds ANNOY index
# Calculates the nearest neighbors and image similarity metrics
# Stores image similarity scores with productID in a json file
#################################################

features_path = "/home/as6608/aml/proj/image_feat/"
allfiles = os.listdir(features_path)
d = []

for idx, file in enumerate(allfiles):
  d.append([idx, file])

df = pd.DataFrame(d, columns=["idx", "file"])
df.to_csv('/home/as6608/aml/proj/file_hashing.csv', index=False)
