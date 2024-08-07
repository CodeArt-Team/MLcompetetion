


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
class DataPreprocessing:
    def __init__(self) -> None:
        pass
    def dataInfo(df, replace_Nan=False, PrintOutColnumber = 40,nanFillValue=0):
        column_count = len(df.columns)
        row_count = len(df.index)
        nul_count  = df.isnull().sum().sum()

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
            if idx < PrintOutColnumber:
                if len(f"\t{idx}.[{col}({df.dtypes[col]})]:")<25:
                    print(yellow(f"\t{idx}.[{col}({df.dtypes[col]})]:\t\t"),\
                        red(f"{len(df[col].unique())}"),f"/{len(df[col])} \t[uniq/raw]",\
                             sep=" ")
                    print(df[col].value_count)
                else:
                    print(blue(f"\t{idx}.[{col}({df.dtypes[col]})]:\t"),\
                    red(f"{len(df[col].unique())}"),f"/{len(df[col])} \t[uniq/raw]", sep=" ")

        else: 
            print(f"\t ...etc (추가로 {len(df.dtypes.keys())-PrintOutColnumber}개의 칼럼이 있습니다 )")

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
    
    
