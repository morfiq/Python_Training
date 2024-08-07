import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
excel_file = 'movies.xls'
movies = pd.read_excel(excel_file)
movies.head()
movies_sheet1 = pd.read_excel(excel_file, sheetname=0, index_col=0)
movies_sheet1.head()
movies_sheet2 = pd.read_excel(excel_file, sheetname=1, index_col=0)
movies_sheet2.head()
movies_sheet3 = pd.read_excel(excel_file, sheetname=2, index_col=0)
movies_sheet3.head()
movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
movies.shape

xlsx = pd.ExcelFile(excel_file)
movies_sheets = []
for sheet in xlsx.sheet_names:
   movies_sheets.append(xlsx.parse(sheet))
movies = pd.concat(movies_sheets)
movies.shape
movies.tail()
sorted_by_gross = movies.sort_values(['Gross Earnings'], ascending=False)
sorted_by_gross["Gross Earnings"].head(10)


sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
plt.show()

movies['IMDB Score'].plot(kind="hist")
plt.show()

movies.describe()

movies["Gross Earnings"].mean()
movies_skip_rows = pd.read_excel("movies-no-header-skip-rows.xls", header=None, skiprows=4)
movies_skip_rows.head(5)
movies_skip_rows.columns = ['Title', 'Year', 'Genres', 'Language', 'Country', 'Content Rating', 'Duration', 'Aspect Ratio', 'Budget', 'Gross Earnings', 'Director', 'Actor 1', 'Actor 2', 'Actor 3', 'Facebook Likes - Director', 'Facebook Likes - Actor 1', 'Facebook Likes - Actor 2', 'Facebook Likes - Actor 3', 'Facebook Likes - cast Total', 'Facebook likes - Movie', 'Facenumber in posters', 'User Votes', 'Reviews by Users', 'Reviews by Crtiics', 'IMDB Score']
movies_skip_rows.head()
movies_subset_columns = pd.read_excel(excel_file, parse_cols=6)
movies_subset_columns.head()
movies["Net Earnings"] = movies["Gross Earnings"] - movies["Budget"]
# sorted_movies = movies[['Net Earnings']].sort_values(['Net Earnings'], ascending=[False])sorted_movies.head(10)['Net Earnings'].plot.barh()
# plt.show()
movies_subset = movies[['Year', 'Gross Earnings']]
movies_subset.head()
earnings_by_year = movies_subset.pivot_table(index=['Year'])
earnings_by_year.head()
earnings_by_year.plot()
plt.show()