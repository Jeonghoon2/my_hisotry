import pandas as pd
import argparse

# -s : count
# -t : 지정 횟수로 해당 일자의 커맨드 값 조회
command_helper = """
Command Helper
-s : 커맨드 명령어를 인자값으로 넣어 주세요.
-t : 행 출력 개수를 지정하기 위한 인자값을 넣어 주세요.
    -d : 출력 하고 싶은 날짜의 값을 넣어 주세요. 
"""


def init():
    parser = argparse.ArgumentParser(description='테스트')

    parser.add_argument(
        '-s',
        help="커맨드 명령어를 인자값으로 넣어 주세요.",
        required=False
    )
    parser.add_argument(
        '-d',
        help="행 출력 개수를 지정하기 위한 인자값을 넣어 주세요.",
        required=False
    )
    parser.add_argument(
        '-t',
        help="출력 하고 싶은 날짜의 값을 넣어 주세요.",
        required=False
    )
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
    else:
        print(command_helper)
        return
