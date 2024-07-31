"""
    🔸 Team : 가나다라마바사 팀
    🔸 Date : 2024.07.30 
    🔸 Description: 사전테스트 제출 파일 
    🔸 구동방식 
        1. 환경데이터가 있는 폴더의 경로를 command 에 넣습니다. . 
        2. 생육데이터가 있는 폴더의 경로를 command 에 작성합니다. 
    
"""




## 머신러닝을 위한 라이브러리  패키지 설치 
def MLLibraryInstalls():
    import subprocess
    import sys
    import warnings
    warnings.filterwarnings('ignore')
    


    def install(package):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")
    
    # pandas 없으면 pandas 설치
    try:
        import pandas
    except ImportError:
        print("Installing pandas")
        install('pandas')
    finally:
        try:
            import pandas as pd
        except ImportError:
            print("Failed to import pandas after installation")

    # numpy 없으면 numpy 설치
    try:
        import numpy
    except ImportError:
        print("Installing numpy")
        install('numpy')
    finally:
        try:
            import numpy as np
        except ImportError:
            print("Failed to import numpy after installation")

    # sklearn 없으면 sklearn 설치
    try:
        import sklearn
    except ImportError:
        print("Installing sklearn")
        install('scikit-learn')
    finally:
        try:
            from sklearn.tree import DecisionTreeRegressor
            from sklearn.metrics import mean_squared_error, r2_score
        except ImportError:
            print("Failed to import sklearn modules after installation")
    # matplotlib 없으면 matplotlib 설치
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Installing sklearn")
        install('matplotlib')
    finally:
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("Failed to import matplotlib modules after installation")
            
    # Seaborn 없으면 Seaborn 설치
    try:
        import seaborn
    except ImportError:
        print("Installing sklearn")
        install('seaborn')
    finally:
        try:
            import seaborn
        except ImportError:
            print("Failed to import matplotlib modules after installation")
### 필요한 library package install 
MLLibraryInstalls()

try:
    import pandas as pd,numpy as np ## pandas, numpy 
    import matplotlib.pyplot as plt,seaborn as sns  # 시각화
    import warnings; warnings.filterwarnings('ignore')  # 경고 무시
    import sys,os # file directory access
    from pprint import pprint 
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import mean_squared_error, r2_score

    print("필요한 라이브러리 설치 및 임포트 완료")
    import platform; print(platform.platform())
    import sys; print("Python",sys.version)
    import sklearn; print("Scikit-Learn", sklearn.__version__)
    import xgboost; print("XGBoost", xgboost.__version__)
except ImportError as e:
    print(f"필요한 라이브러리 임포트에 실패했습니다: {e}")

# 기본 세팅
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
import math
import time


class ReadInputOutput:
    @staticmethod
    def main():
        print("\n")
        print("1. 입력한 파라미터인 이미지 경로(--path)에서 이미지들을 차례대로 읽어옵니다.")
        print("2. 키보드에서 'n'을 누르면(next 약자) 다음 이미지로 넘어갑니다. 이 때, 작업한 점의 좌표가 저장 됩니다.")
        print("3. 키보드에서 'b'를 누르면(back 약자) 직전에 입력한 좌표를 취소합니다.")
        print("4. 이미지 경로에 존재하는 모든 이미지에 작업을 마친 경우 또는 'q'를 누르면(quit 약자) 프로그램이 종료됩니다.")
        print("5. '+' 또는 '='로 확대, '-' 또는 '_'로 축소, 'r'로 리셋할 수 있습니다.")
        print("6. 마우스 오른쪽 버튼을 누른 채로 드래그하여 이미지를 이동할 수 있습니다.")
        print("\n")
        print("출력 포맷 : 이미지명,점의갯수,y1,x1,y2,x2,...")
        print("\n")
        print(green("1.환경데이터가 존재하는 폴더의 경로를 입력해주세요 :\n"))
        input_env_data_folder_path  = str(sys.stdin.readline().rstrip())
        print(" input env data folder path : ",input_env_data_folder_path)
        if os.path.isdir(input_env_data_folder_path):
            for file in os.listdir(input_env_data_folder_path):
                # print(file)
                if file == "environmentsB.csv":
                    input_b=pd.read_csv(os.path.join(input_env_data_folder_path,file))
                    print("input b 입력 완료")
                if file == "environmentsC.csv":
                    input_c=pd.read_csv(os.path.join(input_env_data_folder_path,file))
                    print("input c 입력 완료")
                if file == "environmentsD.csv":
                    input_d=pd.read_csv(os.path.join(input_env_data_folder_path,file))
                    print("input d 입력 완료")
                if file == "environmentsE.csv":
                    input_e=pd.read_csv(os.path.join(input_env_data_folder_path,file))
                    print("input e 입력 완료")  
            else: print(" 모든 데이터를 받았습니다")
        else : print("경로를 다시 입력하세요 ")
        print(green("2.생육데이터가 존재하는 폴더의 경로를 입력해주세요 :\n"))
        output_growth_data_folder_path  = str(sys.stdin.readline().rstrip())
        if os.path.isdir(output_growth_data_folder_path):
            for file in os.listdir(output_growth_data_folder_path):
                if file =="사전테스트-생육데이터.xlsx":
                    output=pd.read_excel(output_growth_data_folder_path,file)
                    print("생육데이터를 받았습니다")

        
        ### output data Fetching 
        print(yellow("🔹 Data preprocessing Start--->"))
        print(yellow(os.getcwd()))


# print(output.tail())
# print(input_b.tail())


start = time.time()

end = time.time()

print(f"{end - start:.5f} sec")



pivoted = pd.pivot_table(output, 
                        values='조사항목값', 
                        index=['시설아이디','생육주사', '조사일자', '표본번호'], 
                        columns='조사항목', 
                        aggfunc='first')

# 인덱스를 리셋합니다
pivoted = pivoted.reset_index()
pivoted.head()
data = pivoted





if __name__ == "__main__":
    ReadInputOutput.main()