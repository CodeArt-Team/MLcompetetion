"""
    🔸 Team : 가나다라마바사 팀
    🔸 Date : 2024.07.30 
    🔸 Description: 사전테스트 제출 파일 
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

### output data Fetching 
print(yellow("🔹 Data preprocessing ---"))


print(yellow(os.getcwd()))

## input Filer read 
input_b=pd.read_csv(os.path.join(os.getcwd(),"BerryMachineLearning/Data/environmentsB.csv"))
input_c=pd.read_csv(os.path.join(os.getcwd(),"BerryMachineLearning/Data/environmentsC.csv"))
input_d=pd.read_csv(os.path.join(os.getcwd(),"BerryMachineLearning/Data/environmentsD.csv"))
input_e=pd.read_csv(os.path.join(os.getcwd(),"BerryMachineLearning/Data/environmentsE.csv"))

output=pd.read_excel(os.path.join(os.getcwd(),"BerryMachineLearning/Data/사전테스트-생육데이터.xlsx"))
print(output.tail())
print(input_b.tail())


pivoted = pd.pivot_table(output, 
                        values='조사항목값', 
                        index=['시설아이디','생육주사', '조사일자', '표본번호'], 
                        columns='조사항목', 
                        aggfunc='first')

# 인덱스를 리셋합니다
pivoted = pivoted.reset_index()
pivoted.head()
data = pivoted
plt.rcParams['font.family'] = 'AppleGothic'  # 맥OS의 경우
plt.rcParams['axes.unicode_minus'] = False 
plt.plot([1,2,3],[1,2,3])
# df = pd.DataFrame(data)
# df['조사일자'] = pd.to_datetime(df['조사일자'], format='%Y%m%d')
# 시각화할 컬럼 선택
print(data)


plt.show()