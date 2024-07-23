import pandas as pd
import sys

def cnt():
    df = pd.read_parquet("~/Workspace/playdata/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(sys.argv[0])]
    cnt = fdf['cnt'].sum()
    print(cnt)

print(cnt)
