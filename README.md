# Computational_Chemsitry_Data_Engineering_Project
- The purpose of this project is to learn more about data engineering (API requests, SQL databases and data preprocessing). 
- Using the data a pytorch convolutional network was then trained.

Steps:
- The pubchem API was used to pull molecular structure images and molecular properties data using python's requests package.
- A MySQL database was then made to store this data using SQL queries, mysql-connector and sqlalchemy.
- A convolutional neural network was then programmed to predict each molecules number of hydrogen donors based on its molecular structure.
- The data for this network was fed in directly from the previously constructed MySQL database. The model was then trained and evaluated.
