
# Gurgaon Real Estate Market Analysis

## Project Summary

This project performs an end-to-end exploratory data analysis of residential property listings in Gurgaon. The goal is to extract actionable insights that support buyers, investors, and developers in making informed real estate decisions.

The analysis focuses on pricing trends, locality performance, builder positioning, BHK segmentation, property types, and RERA approval impact.

## Business Objective

The real estate advisory firm required data-backed insights to:

* Identify premium and high-growth localities
* Understand price variation across BHK configurations
* Compare ready-to-move vs under-construction pricing
* Evaluate whether RERA approval affects property pricing
* Identify builders operating in premium segments
* Analyze how area influences price and rate per square foot

This analysis helps stakeholders make strategic investment and pricing decisions.


## Dataset Description

The dataset contains residential property listings across multiple sectors in Gurgaon, including:

* locality
* price
* area in square feet
* rate_per_sqft
* bhk_count
* flat_type
* company_name
* status (ready to move or under construction)
* rera_approval


## Approach

1. Data Cleaning and Preprocessing

   * Standardized column names
   * Converted numerical fields
   * Cleaned categorical values
   * Removed duplicates

2. Exploratory Data Analysis

   * Locality-wise average pricing analysis
   * Rate per square foot comparison
   * BHK-based segmentation analysis
   * Property type comparison
   * Builder premium analysis
   * Correlation analysis between area and price

3. Visualization

   * Scatter plots to analyze area vs price
   * Area vs rate per square foot analysis


## Key Insights

* Certain localities consistently show higher average property prices
* Premium builders price significantly above market average
* Larger homes have higher total prices, but rate per square foot varies by segment
* BHK configuration impacts overall pricing trends
* Ready-to-move and RERA-approved properties show pricing differences


## Skills Demonstrated

* Data Cleaning and Transformation
* Exploratory Data Analysis
* GroupBy Aggregations
* Business Insight Extraction
* Data Visualization
* Real-world Problem Solving


## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn


## Project Structure

Gurgaon-Real-Estate-Analysis/
-README.md
-data.csv
-main.py



## How to Run

1. Clone the repository
2. Install dependencies
   pip install pandas numpy matplotlib seaborn
3. Place the dataset as data.csv
4. Run
   python analysis.py


## Author

Vaishnavi Gayakwad
Final Year IT Engineering Student
Aspiring Data Analyst



