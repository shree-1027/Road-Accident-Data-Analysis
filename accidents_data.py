import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("C:/Users/admin/OneDrive/Desktop/Regulatory Affairs of Road Accident Data 2020 India.csv")

# View basic info
print(df.head())
print(df.shape)
print(df.info())
print(df.columns)
print(df.isnull().sum())

# Show dropped rows
dropped_rows = df[df.isnull().any(axis=1)]
print("Dropped rows:\n", dropped_rows)

# Drop rows with missing values
df_cleaned = df.dropna()

# Confirm cleaning
#print(df_cleaned.isnull().sum())
 
outcome_vs_cause = df_cleaned.groupby(['Cause category', 'Outcome of Incident'])['Count'].sum().unstack()

# Define custom brighter pastel colors
bright_pastels = ['#FFA07A', '#87CEFA', '#FFB6C1', '#98FB98', '#DA70D6', '#FFD700', '#40E0D0']

# Plot without bar edges
ax = outcome_vs_cause.plot(
    kind='bar',
    stacked=False,
    figsize=(8, 6),
    color=bright_pastels
)

# Titles and axis labels
plt.title('Accident Causes vs Outcomes', fontsize=14, color='darkblue')
plt.xlabel('Cause Category', fontsize=12, color='darkgreen')
plt.ylabel('Number of Incidents', fontsize=12, color='darkgreen')
plt.xticks(rotation=15)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Add data labels
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3, color='black', fontsize=9)

plt.show()



# Plot: Distribution of Road Accidents in Million-Plus Cities
plt.figure(figsize=(12, 8))  # Increase the figure height for better spacing
ax = sns.countplot(y='Million Plus Cities', data=df_cleaned,
                   order=df_cleaned['Million Plus Cities'].value_counts().index,
                   palette='Set2')

plt.title('Distribution of Road Accidents in Million-Plus Cities', fontsize=14, color='darkblue')
plt.xlabel('Number of Records (Accidents)', fontsize=12, color='darkgreen')
plt.ylabel('Cities', fontsize=12, color='darkgreen')
# 👇 Set x-axis range from 175 to 200
plt.xlim(175, 200)

# Rotate the y-axis labels to avoid overlap
plt.yticks(rotation=0, fontsize=10)

plt.tight_layout()

# Add value labels to each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3)

plt.show()

# Plot: Distribution of Accident Causes
plt.figure(figsize=(8, 6))
ax = sns.countplot(y='Cause category', data=df_cleaned,
                   order=df_cleaned['Cause category'].value_counts().index,
                   palette='Set3')

plt.title('Distribution of Accident Causes', fontsize=14, color='darkblue')
plt.xlabel('Number of Accidents', fontsize=12, color='darkgreen')
plt.ylabel('Cause Category', fontsize=12, color='darkgreen')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.xlim(1000, 2100)
plt.tight_layout()

# Add value labels to each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3)

plt.show()

# Detailed analysis by cause subcategory
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))  # Consistent figure size
ax = sns.countplot(
    y='Cause Subcategory',
    data=df_cleaned,
    order=df_cleaned['Cause Subcategory'].value_counts().index,
    palette='Set1'  # Try Set1, Set2, pastel, etc.
)

plt.title('Detailed Analysis of Accident Causes by Subcategory', fontsize=14, color='darkblue')
plt.xlabel('Number of Accidents', fontsize=12, color='darkgreen')
plt.ylabel('Cause Subcategory', fontsize=12, color='darkgreen')
plt.tight_layout()

# Add value labels to each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3)

plt.show()

# Plot: Outcome of Incidents
plt.figure(figsize=(8, 6))
ax = sns.countplot(
    x='Outcome of Incident',
    data=df_cleaned,
    order=df_cleaned['Outcome of Incident'].value_counts().index,
    palette='Set2'
)

plt.title('Outcome of Road Accidents', fontsize=14, color='darkblue')
plt.xlabel('Outcome', fontsize=12, color='darkgreen')
plt.ylabel('Number of Incidents', fontsize=12, color='darkgreen')
plt.ylim(1250, 2100)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=30)

# Add value labels to each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3)

plt.tight_layout()
plt.show()

# Save the cleaned DataFrame
df_cleaned.to_csv("C:/Users/admin/OneDrive/Desktop/Cleaned_Road_Accident_Data.csv", index=False)

print("\nCleaned file saved successfully!")
