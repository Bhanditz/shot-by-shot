import numpy as np
import pandas as pd

shots = [ [k % 18, 'black', np.sin(k)] for k in range(100)]

df = pd.DataFrame(shots, columns=['shotNo', 'frameColor', 'volLevel'])
df.to_csv('dist/data/dummy.csv', index=False)
