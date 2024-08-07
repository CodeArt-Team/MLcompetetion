''' 
📌 Fucntion Description :  Data frame 의 정제를 위한 기본 정보 출력
📌 Date : 2024.06.02 
📌 Author : Forrest D Park 
📌 Update : 
    2024.08.07 by pdg : DataInfo 함수 생성

'''


def colored_text(text, color='default', bold=False):
        '''
        #### 예시 사용법
        print(colored_text('저장 하지 않습니다.', 'red'))
        print(colored_text('저장 합니다.', 'green'))
        default,red,green,yellow,blue, magenta, cyan, white, rest
        '''
        colors = {
            'default': '\033[99m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m', #보라색
            'cyan': '\033[96m',
            'white': '\033[97m',
            'bright_black': '\033[90m',  # 밝은 검정색 (회색)
            'bright_red': '\033[91m',  # 밝은 빨간색
            'bright_green': '\033[92m',  # 밝은 초록색
            'bright_yellow': '\033[93m',  # 밝은 노란색
            'bright_blue': '\033[94m',  # 밝은 파란색
            'bright_magenta': '\033[95m',  # 밝은 보라색
            'bright_cyan': '\033[96m',  # 밝은 청록색
            'bright_white': '\033[97m',  # 밝은 흰색
            'reset': '\033[0m'
        }
        color_code = colors.get(color, colors['default'])
        bold_code = '\033[1m' if bold else ''
        reset_code = colors['reset']
        
        return f"{bold_code}{color_code}{text}{reset_code}"
def blue(str):return colored_text(str,'blue')
def yellow(str):return colored_text(str,'yellow')
def red(str):return colored_text(str,'red')
def green(str):return colored_text(str,'green')
def magenta(str):return colored_text(str,'magenta')
class DataPreprocessing:
    def __init__(self) -> None:
        pass
    def dataInfo(df, replace_Nan=False, PrintOutColnumber = 0,nanFillValue=0):
        column_count = len(df.columns)
        row_count = len(df.index)
        nul_count  = df.isnull().sum().sum()
        value_kind_limit =10
        under_limit_columns =[]
        if PrintOutColnumber ==0 :
            PrintOutColnumber = column_count
        print(yellow(f"- column 수 : {column_count}"))
        print(yellow(f"- row 수    : {row_count}"))
        print(yellow(f"- null 수   : {nul_count}"))
        
        
        for idx, col in enumerate(df.columns):
            if df[f"{col}"].isnull().sum():
                print(f"   => {idx}번째.[{col}]컬럼 : ",f"null {df[f'{col}'].isnull().sum()} 개,\t not null {df[f'{col}'].notnull().sum()} 개")
                ## Null data fill
                if replace_Nan : ## nan 을 0 으로 대체 
                    df=df[col].fillna(value=nanFillValue, inplace=True)  
        print(yellow("- 칼럼별 데이터 중복체크"))
        print( yellow("\tidx.columName |\t\t\t\t |Colum Info(dtype)|** "))
        print( "\t",yellow("--"*len("columIdx |\t\t\t\t **|Col(dtype)|** ")))
        for idx, col in enumerate(df.dtypes.keys()):
            if idx < PrintOutColnumber: ### -> 출력할 칼럼수 제한 
                if len(f"\t{idx}.[{col}({df.dtypes[col]})]:")<25 : ### 이쁘게 출력하기 위해 칼럼 이름 글자수 25개 이하 인것은 탭을 두번만 함. 
                    
                    value_counts = df[col].value_counts()
                    if len(df[col].unique())<10: #중복값이 10 이하일경우 value count 출력
                        under_limit_columns.append(col)
                        print(yellow(f"\t{idx}.[{col}({df.dtypes[col]})]:\t\t"),\
                            red(f"{len(df[col].unique())}"),\
                            green(f"\t/{len(df[col])} ")+ "\t[uniq/raw]",\
                            blue(f"---📌값의 종류가 {value_kind_limit}개 미만 입니다. "),\
                             sep=" ")
                        ### Value count 값 분포 확인
                        print("\t\t",magenta("--"*20))
                        for order,(i,v) in enumerate(zip(value_counts.index.tolist(), value_counts.values.tolist())):
                            print(magenta(f"\t\t |-[{order}] {i} : \t{v}"))
                        print("\t\t",magenta("--"*20))
                    else: 
                        print(yellow(f"\t{idx}.[{col}({df.dtypes[col]})]:\t\t"),\
                        red(f"{len(df[col].unique())}"),f"\t/{len(df[col])} \t[uniq/raw]",\
                             sep=" ")
                        
                    
                else:### 이쁘게 출력하기 위해 칼럼 이름 글자수 25개 이상 인것은 탭을 두번만 함. 
                    
                    value_counts = df[col].value_counts()
                    if len(df[col].unique())<10: #중복값이 10 이하일경우 value count 출력
                        under_limit_columns.append(col)
                        print(yellow(f"\t{idx}.[{col}({df.dtypes[col]})]:\t\t"),\
                        red(f"{len(df[col].unique())}"),\
                        green(f"\t/{len(df[col])} ")+ "\t[uniq/raw]",\
                            blue(f"---📌값의 종류가 {value_kind_limit}개 미만 입니다. "),\
                             sep=" ")
                        print("\t\t",magenta("--"*20))
                        for order,(i,v) in enumerate(zip(value_counts.index.tolist(), value_counts.values.tolist())):
                            print(magenta(f"\t\t |-[{order}] {i} : \t{v}"))
                        print("\t\t",magenta("--"*20))

        else: 
            print(f"\t ...etc (추가로 {len(df.dtypes.keys())-PrintOutColnumber}개의 칼럼이 있습니다 )")
            print(red("\t[RESULT]"),"🙀🙀🙀"*10)
            print(yellow(f"\t🟦{value_kind_limit}개이하의 값 종류를 가지는 칼럼 "))
            for col in under_limit_columns:
                print("\t\t-",yellow(f"{col}:{len(df[col].unique())}: {df[col].unique().tolist()}"))
            else:print("\t",red(f"총 {len(under_limit_columns)}개"))

    def main():
        print(yellow("title"))  
        

if __name__ == "__main__":
    import pandas as pd ,sys
    input_data = pd.read_csv('/Users/forrestdpark/Desktop/PDG/Python_/BerryMLcompetetion/BerryMachineLearning/예선연습_2023_tomato/Data/2023_smartFarm_AI_hackathon_dataset.csv')
    while True : 
        yellow("프로그램 시작")
        DataPreprocessing.dataInfo(input_data)
        print(green("다시 실행하시겠습니니까?(yes =1, no=0): "))
        restart_query = int(sys.stdin.readline())
        if restart_query == 0:
            break     
    
    
