from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.1)
training_data = np.random.rand(100, 2)
model.fit(training_data)

def detect_anomaly(features):
    data = np.array([[features["syn_count"], features["unique_ports"]]])
    prediction = model.predict(data)
    return prediction[0] == -1
