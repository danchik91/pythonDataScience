import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier

path = os.path.join(os.getcwd(), "mosh/music/music.csv")
print(path)
music_data = pd.read_csv(path)

x = music_data.drop(columns=["genre"])              # dataset without this column
y = music_data["genre"]
# print(x)
# print(y)
# print(music_data)

model = DecisionTreeClassifier()
model.fit(x, y)
print(music_data)
prediction = model.predict([[21, 1], [22, 0]])
print(prediction)                                   # ['HipHop' 'Dance']


# W3
my_list = [1, 2, 3, 4, 5, 6, 1]
series = pd.Series(my_list, index=["x", "y", "z", "xx", "yy", "zz", "q"])
"""
                x     1
                y     2
                z     3
                xx    4
                yy    5
                zz    6
                q     1
                dtype: int64
"""

# print(series)


