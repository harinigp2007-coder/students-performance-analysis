import pandas as pd
import matplotlib.pyplot as plt

# Read CSV File
df = pd.read_csv("student_markss.csv")

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Rename columns
df.rename(columns={
    "REGISTER NO": "Register_No",
    "NAME": "Name",
    "SEM-1": "Sem1",
    "SEM-2": "Sem2",
    "SEM-3": "Sem3"
}, inplace=True)

# Calculate CGPA
df["CGPA"] = df[["Sem1", "Sem2", "Sem3"]].mean(axis=1)

# Calculate Rank
df["Rank"] = df["CGPA"].rank(ascending=False, method="dense").astype(int)

# Performance Status
def status(cgpa):
    if cgpa >= 8:
        return "Excellent"
    elif cgpa >= 7:
        return "Good"
    elif cgpa >= 6:
        return "Average"
    else:
        return "Needs Improvement"

df["Status"] = df["CGPA"].apply(status)

# Display Student Details
print("\n========== STUDENT DETAILS ==========\n")
print(df)

# Class Topper
topper = df.loc[df["CGPA"].idxmax()]

print("\n========== CLASS TOPPER ==========")
print("Register No :", topper["Register_No"])
print("Name        :", topper["Name"])
print("CGPA        :", round(topper["CGPA"], 2))
print("Rank        :", topper["Rank"])
print("Status      :", topper["Status"])

# Lowest CGPA
lowest = df.loc[df["CGPA"].idxmin()]

print("\n========== LOWEST CGPA ==========")
print("Register No :", lowest["Register_No"])
print("Name        :", lowest["Name"])
print("CGPA        :", round(lowest["CGPA"], 2))
print("Rank        :", lowest["Rank"])
print("Status      :", lowest["Status"])

# Class Average
print("\n========== CLASS AVERAGE ==========")
print("Average CGPA :", round(df["CGPA"].mean(), 2))

# Top 5 Students
print("\n========== TOP 5 STUDENTS ==========\n")
top5 = df.sort_values(by="CGPA", ascending=False).head(5)
print(top5[["Rank", "Register_No", "Name", "CGPA"]])

# Save Result
df.to_csv("student_result.csv", index=False)
print("\n✅ student_result.csv created successfully!")

# Bar Chart
plt.figure(figsize=(14,6))
plt.bar(df["Name"], df["CGPA"], color="skyblue")

plt.title("Student CGPA Analysis")
plt.xlabel("Student Name")
plt.ylabel("CGPA")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()