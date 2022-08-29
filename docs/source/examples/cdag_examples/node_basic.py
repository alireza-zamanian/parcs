import numpy as np
import pandas as pd
from parcs.cdag.graph_objects import Node
np.random.seed(1)

node = Node(
    name='Z_1',
    parents=[],
    output_distribution='bernoulli',
    dist_params_coefs={
        'p_': {
            'bias': 0.7, 'linear': np.array([]), 'interactions': np.array([])
        }
    }
)

samples = node.sample(data = pd.DataFrame([]))
print(samples[:5])
# [1 1 0 1 0]
print(samples.mean())
# 0.702