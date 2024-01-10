import pandas as pd
import numpy as np
np.random.seed(42)
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

df.iloc[0, 2] = np.nan
df.iloc[3, 3] = np.nan
df.iloc[4, 1] = np.nan
styled_df = df.style.highlight_null(props={'background-color': 'red'})

print(styled_df)
