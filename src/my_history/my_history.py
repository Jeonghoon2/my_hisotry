import pandas as pd
import sys

def cnt():
    df = pd.read_parquet("~/Workspace/playdata/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(sys.argv[1])]
    cnt = fdf['cnt'].sum()
    print(f"{sys.argv[1]} 커맨드 사용 횟수는 {cnt}회 입니다.")

