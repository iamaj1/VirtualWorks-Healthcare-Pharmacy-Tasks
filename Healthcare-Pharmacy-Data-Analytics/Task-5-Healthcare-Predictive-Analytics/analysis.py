"""Task 5: Predictive analytics demonstration on synthetic data only."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(32)
n = 500
age = rng.integers(18, 90, n)
stay = rng.integers(1, 18, n)
prior = rng.integers(0, 5, n)
chronic = rng.integers(0, 6, n)
logit = -3.0 + .025 * (age - 50) + .12 * stay + .32 * prior + .18 * chronic
prob = 1 / (1 + np.exp(-logit))
target = rng.binomial(1, prob)
df = pd.DataFrame({"age": age, "length_of_stay_days": stay, "prior_visits": prior, "chronic_condition_count": chronic, "synthetic_readmission_flag": target})
df.to_csv(OUT / "synthetic_readmission_data.csv", index=False)
X = df.drop(columns="synthetic_readmission_flag")
y = df["synthetic_readmission_flag"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=42, stratify=y)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
pred = model.predict(X_test)
metrics = {"accuracy": accuracy_score(y_test, pred), "precision": precision_score(y_test, pred, zero_division=0), "recall": recall_score(y_test, pred, zero_division=0), "f1": f1_score(y_test, pred, zero_division=0)}
cm = confusion_matrix(y_test, pred)
fig, ax = plt.subplots(figsize=(5, 4))
ax.imshow(cm)
ax.set_title("Confusion Matrix — Synthetic Data"); ax.set_xlabel("Predicted"); ax.set_ylabel("Actual")
ax.set_xticks([0, 1], ["No", "Yes"]); ax.set_yticks([0, 1], ["No", "Yes"])
for (i, j), val in np.ndenumerate(cm): ax.text(j, i, str(val), ha="center", va="center")
fig.tight_layout(); fig.savefig(OUT / "synthetic_model_confusion_matrix.png", dpi=160); plt.close(fig)
with (OUT / "model_evaluation.txt").open("w", encoding="utf-8") as f:
    f.write("SYNTHETIC EDUCATIONAL MODEL — NOT FOR CLINICAL USE\n")
    for key, value in metrics.items(): f.write(f"{key}: {value:.3f}\n")
    f.write("\n" + classification_report(y_test, pred, zero_division=0))
print("Evaluation metrics:", metrics)
print(classification_report(y_test, pred, zero_division=0))
