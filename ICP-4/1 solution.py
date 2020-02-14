import pandas as pd
train_df= pd.read_csv('train_preprocessed.csv')
print(train_df.columns.values)
print(train_df['Survived'].corr(train_df['Sex']))