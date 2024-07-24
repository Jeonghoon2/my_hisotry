# my_history

## Usage


### 도움말
```bash
$ p-search -h
$ p-search --help
```
<img width="648" alt="image" src="https://github.com/user-attachments/assets/d62021b2-7e9e-4cd1-978f-30ae9ec32f40">

### 커맨드의 사용 횟수 출력
```bash
$ p-search -s [입력값]
```
<img width="529" alt="image" src="https://github.com/user-attachments/assets/dca5743e-8bb9-4040-b34c-3cf0cdf00dea">

### 해당 날짜의 사용 명령어 출력 < Option 값으로 출력 개수 조정 가능 >
- 출력 개수 입력 출력 개수 없을 경우의 기능 미구현 
```bash
$ p-search -t [출력 개수] -d [검색 날짜]
```
<img width="665" alt="image" src="https://github.com/user-attachments/assets/7f5e4f19-5713-4ccd-9953-53361fc3fe84">


## Version
- 0.1.0
	- 하나의 커맨드를 입력하면 해당 커맨드의 사용 횟수를 불러온다.
- 0.1.1
	- 아웃풋 값에서 함수 주소값 출력 되는 오류 수정
	- 가독성 있는 아웃풋 값으로 변경
	- README 수정
- 0.2.0
	- 가변 안자를 통해 원하는 출력 값만 나타낸다. < 날짜에 따른 개수 지정 >
 	- 기존 p-search를 통해 **Command**의 개수를 출력하는 방식 변경 < 위 Usage 참조 >
  	- CLI 를 통해 안내 멘트 생성
