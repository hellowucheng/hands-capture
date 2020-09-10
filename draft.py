import pickle
from config import args


with open(args.boxes_path, 'rb') as f:
    boxes = pickle.load(f)

for k, v in boxes.items():
    print(k, v)
print(len(boxes.keys()))