# Big Data Analytics Project

This project demonstrates a complete data analytics workflow, from data
understanding and preprocessing to feature engineering, modeling, and evaluation.
The work is implemented using Python and Jupyter notebooks.

The project follows a structured approach commonly used in analytics and
machine learning pipelines, while remaining appropriate for a beginner-to-
intermediate level in Big Data analytics.

---

## Project Structure
```
.
├── data/
│ ├── raw/ # Original data files
│ └── processed/ # Preprocessed train/test datasets
├── notebooks/
│ ├── 01_data_overview.ipynb
│ ├── 02_schema_and_joins.ipynb
│ ├── 03_eda.ipynb
│ ├── 04_feature_engineering_and_preprocessing.ipynb
│ └── 05_modeling_and_evaluation.ipynb
├── src/
│ └── data_utils.py # Helper functions for data loading
├── requirements.txt
└── README.md
```
---

## Environment Setup

A Python virtual environment is used to isolate project dependencies and ensure
reproducibility.

### 1. Create a virtual environment

From the project root directory, run:

```
python3 -m venv venv
```

You can verify that the environment was created by listing the directory contents:

```
ls
```

2. Activate the virtual environment
source venv/bin/activate


Once activated, all Python packages will be installed locally inside the
virtual environment.

3. Install project dependencies

All required libraries are listed in requirements.txt.

Install them using:

```
pip install -r requirements.txt
```

4. Deactivate the environment

When you are finished working on the project, you can exit the virtual
environment by running:

```
deactivate
```

Notebooks Overview

01_data_overview.ipynb
Initial exploration of the dataset and high-level understanding of the data
warehouse structure.

02_schema_and_joins.ipynb
Construction of an analytics-ready dataset by joining fact and dimension tables
following a star schema approach.

03_eda.ipynb
Exploratory Data Analysis (EDA) to identify patterns, distributions, and
potential data quality issues.

04_feature_engineering_and_preprocessing.ipynb
Feature selection, missing value handling, numerical transformations, and
categorical encoding to prepare data for modeling.

05_modeling_and_evaluation.ipynb
Training and evaluation of regression models, including baseline comparison,
Linear Regression, and Ridge Regression.

Tools and Libraries

The project uses the following main libraries:

```
pyspark==3.5.1

pandas

numpy

matplotlib

seaborn

scikit-learn

jupyter
```

These tools were selected to match the scope and complexity of the dataset and
to remain appropriate for a learning-focused analytics project.

Notes

This project focuses on clarity, reproducibility, and correct analytical
reasoning rather than advanced optimization or large-scale distributed
processing. All modeling decisions and preprocessing steps are documented
directly in the notebooks.
