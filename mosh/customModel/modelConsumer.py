import joblib
from sklearn.metrics import accuracy_score

import model

test_data = model.input_test
custom_model = joblib.load("music-recommender.joblib")
predictions = custom_model.predict(test_data)
print(test_data)
print(predictions)
score = accuracy_score(model.output_test, predictions)
print(score)
