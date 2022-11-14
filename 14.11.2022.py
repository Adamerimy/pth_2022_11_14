import pandas as pd
df = pd.read_csv("C:/Users/digdepstudent/Documents/Ada/pth_2022_11_14/data.tsv",sep="\t",index_col = "ID")
print(df.to_string())