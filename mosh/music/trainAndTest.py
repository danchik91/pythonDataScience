import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

path = os.path.join(os.getcwd(), "mosh/music/music.csv")
music_data = pd.read_csv(path)

input_data = music_data.drop(columns=["genre"])
output_data = music_data["genre"]

input_train, input_test, output_train, output_test = train_test_split(input_data, output_data, test_size=0.1)
"""
The key moment: The more data we are using for training a model (the cleaner the better) 
and less data for testing, the higher accuracy is
"""

model = DecisionTreeClassifier()
model.fit(input_train, output_train)
prediction = model.predict(input_test)

score = accuracy_score(output_test, prediction)
print(score)
