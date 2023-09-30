import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(reviews.columns)
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})
reindexed = reviews.set_index("title")
print(reindexed.head())
reindexed = reindexed.rename_axis("wines", axis='rows')
print(reindexed.head())

