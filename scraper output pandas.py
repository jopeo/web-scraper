import pandas

name = 'name'
df = pandas.read_csv(f'//path/{name}.csv', index_col='column')
ndf = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
ndf = ndf.drop_duplicates()
ndf['date'] = ndf['date'].apply(lambda x: x.split(";")[0] if type(x) == str else str(x).split(";")[0])
ndf['col'] = ndf['col'].str.replace(",", chr(13))
ndf['authors'] = ndf['authors'].str.replace(",", chr(13))
ndf.to_excel(f'{name}.xlsx')