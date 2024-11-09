## Data Cleaning

This process was distributed between two notebooks:

- [InitialDataCleaning.ipynb](https://github.com/faendal/MushroomEdibilityPrediction/blob/main/Notebooks/1.1-InitialDataCleaning.ipynb)
- [EDA-FullDataCleaning.ipynb](https://github.com/faendal/MushroomEdibilityPrediction/blob/main/Notebooks/1.2-EDA-FullDataCleaning.ipynb)

In the first notebook, we performed the following steps:

1. Load the data
2. Eliminate irrelevant columns
3. Check for missing values
4. Handle missing values
5. Check unique values per column and filter categorical data
6. Save the clean data

This produced the partially cleaned dataset available in [`Data/PartiallyCleaned/`](https://github.com/faendal/MushroomEdibilityPrediction/tree/main/Data/PartiallyClean)

In the second notebook, we performed the following steps:

1. Load the partially cleaned dataset.
2. Generate a profiling report of the dataset.
3. Statistical analysis of the dataset.
4. Check for outliers and clean them.
5. Check for correlations.
6. Save the fully cleaned dataset.

This produced the fully cleaned dataset available in [`Data/FullyClean/`](https://github.com/faendal/MushroomEdibilityPrediction/tree/main/Data/FullyClean)

Also this produced the figures available in [`Reports/Figures/`](https://github.com/faendal/MushroomEdibilityPrediction/tree/main/Reports/Figures)

And the profilings available in [`Reports/Profiles/`](https://github.com/faendal/MushroomEdibilityPrediction/tree/main/Reports/Profiles)

## Data Transformation

This was performed in the notebook [DataTransformation.ipynb](https://github.com/faendal/MushroomEdibilityPrediction/blob/main/Notebooks/1.3-DataTransformation.ipynb)

The following steps were performed:

- MinMaxScaler for numerical data
- LabelEncoder for class
- Dummy creation for categorical data
- Sampling to work with a smaller dataset.

This produced the final workind dataset available in [`Data/WorkingData/`](https://github.com/faendal/MushroomEdibilityPrediction/tree/main/Data/WorkingData)
