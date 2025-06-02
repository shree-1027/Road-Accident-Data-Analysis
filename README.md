🚧 Road Accident Data Analysis – India (2020)
This project provides a data analysis and visualization of road accident statistics from India for the year 2020, focusing on cause categories, outcomes, and city-level distributions, using Python, Pandas, Seaborn, and Matplotlib.

📁 Dataset
Source: Regulatory Affairs of Road Accident Data 2020 India.csv

Scope:

Breakdown of accidents by cause and subcategory

Distribution across million-plus cities

Outcomes of incidents (fatalities, injuries, etc.)

🧼 Data Cleaning
Inspected the dataset using .info(), .isnull(), and .head() to understand the structure.

Identified and dropped rows with missing values to ensure analysis accuracy.

Final cleaned dataset saved as:
✅ Cleaned_Road_Accident_Data.csv

📊 Visualizations
1. Accident Causes vs Outcomes
Bar chart comparing accident cause categories with outcomes.

Custom pastel color palette used.

Annotated with value labels for clarity.

2. Distribution in Million-Plus Cities
Horizontal bar plot showing frequency of road accidents across major Indian cities.

plt.xlim() used to zoom into the 175–200 record range for better visual inspection.

3. Distribution of Accident Causes
Countplot of the main categories responsible for accidents.

Gridlines added to improve visual reading.

4. Detailed Cause Subcategory Analysis
Deep-dive into subcategories of causes.

Highlighted frequently occurring subcauses like driver fatigue, mechanical failure, etc.

5. Outcome of Road Accidents
Countplot showing how many accidents resulted in different outcomes (e.g., Fatal, Injured).

Useful for understanding accident severity trends.

🛠 Tech Stack
Python 3.x

Pandas – data manipulation

Matplotlib & Seaborn – visualization

Jupyter Notebook or Python script

📁 Output
📂 Cleaned_Road_Accident_Data.csv: Cleaned and preprocessed data for future use.

📈 Graphs & plots: Displayed inline or can be saved/exported as needed.

🔍 Key Insights
Some cities had disproportionately high incident records.

Certain accident causes (like "Driver Fault") led to more severe outcomes.

A few subcategories consistently appeared as leading contributors to incidents.

🧾 To Run the Project
bash
Copy
Edit
# Clone the repo
git clone https://github.com/your-username/road-accident-analysis-2020.git

# Install dependencies
pip install pandas matplotlib seaborn

# Run the script or Jupyter notebook
python analysis.py
📌 Future Work
Time-series analysis if monthly data is added

Geo-visualization using city coordinates

ML prediction on accident severity based on features

📝 License
MIT License. Feel free to fork and build upon this project.

