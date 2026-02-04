import numpy as np
import random
import json

hidden_layers = 5
neurons_per_hidden = 15

hidden_weights = []

hidden_weights = np.random.rand(hidden_layers, neurons_per_hidden)

print(hidden_weights)


all_weights = {}
count = 0
for l in hidden_weights:
  for w in l:
    all_weights[count] = w
    count += 1
    
with open("param.json", "w") as param:
  json.dump(all_weights, param, indent = 4)