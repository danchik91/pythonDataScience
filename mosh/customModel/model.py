import joblib
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


path = os.path.join(os.getcwd(), "mosh/music/music.csv")
music_data = pd.read_csv(path)

input_data = music_data.drop(columns=["genre"])
output_data = music_data["genre"]
input_train, input_test, output_train, output_test = train_test_split(input_data, output_data, test_size=0.1)

model = DecisionTreeClassifier()
model.fit(input_data, output_data.values)

joblib.dump(model, "music-recommender.joblib")
