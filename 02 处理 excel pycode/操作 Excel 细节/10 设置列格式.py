import pandas as pd
import numpy as np

np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})

df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
df.iloc[0, 2] = np.nan

df.to_excel('./result.xlsx',index=False)

def highlight_greaterthan(s, threshold, column):
    is_max = pd.Series(data=False, index=s.index)
    is_max[column] = s.loc[column]= threshold
    return ['background-color: yellow' if is_max.any() else '' for v in is_max]

df1=pd.read_excel('./result.xlsx')
df1.style.apply(highlight_greaterthan, threshold=1.0, column=['C', 'B'], axis=1)

df1.to_excel('./result1.xlsx',index=False)
