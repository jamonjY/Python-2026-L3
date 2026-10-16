
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("scores.csv")

# Scatter plot
plt.figure(figsize=(10, 6))

plt.scatter(df["student_id"], df["math"], label="Math")
plt.scatter(df["student_id"], df["python"], label="Python")
plt.scatter(df["student_id"], df["database"], label="Database")

plt.xlabel("Student ID")
plt.ylabel("Score")
plt.title("Student Scores by Subject")
plt.legend()
plt.tight_layout()
plt.savefig("scattered.png")
plt.close()

# Histograms

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].hist(df["math"], bins=10, edgecolor="black")
axes[0].set_title("Math")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Frequency")

axes[1].hist(df["python"], bins=10, edgecolor="black")
axes[1].set_title("Python")
axes[1].set_xlabel("Score")
axes[1].set_ylabel("Frequency")

axes[2].hist(df["database"], bins=10, edgecolor="black")
axes[2].set_title("Database")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Frequency")

fig.tight_layout()
fig.savefig("histo.png")
plt.close(fig)

# Box plots

plt.figure(figsize=(8, 6))

plt.boxplot([
    df["math"],
    df["python"],
    df["database"]
])

plt.xticks([1, 2, 3], ["Math", "Python", "Database"])
plt.title("Student Scores by Subject")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("box.png")
plt.close()

