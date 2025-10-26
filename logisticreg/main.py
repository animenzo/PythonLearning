# %%
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load iris dataset directly from sklearn
iris = load_iris()

# Convert to a pandas DataFrame
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target column (species)
iris_data['target'] = iris.target

# Show first 5 rows
print(iris_data.head())

# %%
