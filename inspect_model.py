import pickle
import numpy as np
import os
import sklearn

print(f"Scikit-Learn Version: {sklearn.__version__}")

file_path = "c:/Users/Siva/Desktop/project/model.pkl"

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

try:
    with open(file_path, "rb") as f:
        model = pickle.load(f)
    
    print(f"Model Type: {type(model)}")
    
    if hasattr(model, "n_features_in_"):
        print(f"Number of features expected: {model.n_features_in_}")
    else:
        print("Model does not store n_features_in_")
        
    if hasattr(model, "feature_names_in_"):
        print(f"Feature names: {model.feature_names_in_}")
    else:
        print("Model does not store feature_names_in_")
        
except Exception as e:
    print(f"Error loading model: {e}")
