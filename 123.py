import pandas as pd
import numpy
import sklearn
print(sklearn.__version__)
print(numpy.__version__)

import pandas as pd
data = {
    '학번' : range(2000,2010),
    '성적' : [88, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}
print('일반')
print(pd.DataFrame(data))
print('____________________________________________')
print('프레임 컬럼 순서 변경')
print(pd.DataFrame(data, columns = ['성적', '학번']))
print('프레임 인덱스 나열 변경')
print(pd.DataFrame(data, columns = ['성적', '학번'], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))