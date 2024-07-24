import pandas as pd
import argparse


# -s : count
# -t : 지정 횟수로 해당 일자의 커맨드 값 조회

def init():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', required=False)
    parser.add_argument('-d', required=False)
    parser.add_argument('-t', required=False)
    return parser


def cnt():
    # Parquet 파일 읽기
    df = pd.read_parquet(path="~/data/parquet")

    # 인자값 초기화
    parser = init()
    args = parser.parse_args().__dict__

    # s값이 있다면
    if args['s'] is not None:
        fdf = df[df['cmd'] == args['s']]
        cnt = fdf['cnt'].sum()
        print(f"{args['s']} 커맨드 사용 횟수는 {cnt}회 입니다.")
    elif args['t'] is not None:
        fdf = df[df['dt'] == args['d']]

        fdf = fdf.head(int(args.get('t')))
        print(fdf.to_string(index=False))
