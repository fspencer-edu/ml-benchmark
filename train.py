import time
import json
import os
import multiprocessing
import platform

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

os.makedirs("artifacts", exist_ok=True)

X, y = make_classification(
    n_samples=50000,
    n_features=30,
    n_informative=10,
    n_redundant=5,
    n_classes=2,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    n_jobs=-1,
    random_state=42,
)

start = time.perf_counter()
model.fit(X_train, y_train)
train_seconds = time.perf_counter() - start

pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

joblib.dump(model, "artifacts/model.joblib")

with open("artifacts/results.json", "w") as f:
    json.dump(
        {
            "machine": platform.node(),
            "arch": platform.machine(),
            "cpu_count": multiprocessing.cpu_count(),
            "train_seconds": round(train_seconds, 4),
            "accuracy": round(acc, 4),
        },
        f,
        indent=2,
    )

print("Done")
print(f"Train time: {train_seconds:.4f}s")