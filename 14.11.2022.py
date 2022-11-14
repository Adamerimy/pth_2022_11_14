import pandas as pd
df = pd.read_csv("C:/Users/digdepstudent/Documents/Ada/pth_2022_11_14/data.tsv",sep="\t",index_col = "ID")
print(df.to_string())

df=df.dropna(axis=0)
print(df.to_string())
x=df['age'].mean()
df['age'].fillna(x, inplace= True)
print(df.to_string())
print(df.info())


