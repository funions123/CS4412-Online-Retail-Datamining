# Online Retail Datamining

This repository is for a retail datamining project implemented in jupyter notebooks.

Data Source: https://archive.ics.uci.edu/dataset/352/online+retail

The dataset is small enough to be INCLUDED in the repo at data/raw/.

# How To Run

Requirements: python installed on the system

Running from the commandline:
1. Clone the repo to any folder.
2. Install dependencies: 'pip install -r requirements.txt' in the root folder
3. Launch jupyter to run the notebooks: 'jupyter 01_preprocessing.ipynb' etc

Running in Visual Studio Code (recommended):
1. Clone the repo to any folder.
2. Install dependencies: 'pip install -r requirements.txt' in the root folder
3. Install the Jupyter extension pack for VSC by Microsoft.
4. Open the notebooks in VSC.

# What's Inside

4 Notebooks:
1. 01_preprocessing.ipynb: EDA and raw data processing
2. 02_market_basket.ipynb: Association rule mining with Apriori
3. 03_customer_segmentation.ipynb: K-means clustering on RFM features
4. 04_time_series_clustering.ipynb: STL decomposition + DTW K-means clustering
