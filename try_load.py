import pickle
import sys

print(f"Python: {sys.version}")

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    print("Success!")
    print(type(model))
except Exception as e:
    print(f"Error: {e}")
