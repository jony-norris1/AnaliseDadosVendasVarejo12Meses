import pandas as pd

data = {
    'Date': ['9/28/2020', '10/2/2020', '10/6/2020', '10/10/2020', '10/14/2020', '10/18/2020', '10/22/2020', '10/26/2020', '10/30/2020', '11/3/2020', '11/7/2020', '11/11/2020', '11/15/2020', '11/19/2020', '11/23/2020', '11/27/2020', '12/1/2020', '12/5/2020', '12/9/2020'],
    'ID': [1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126],
    'Model': ['Fit', 'Palio', 'Golf', 'S10', 'Cruze', 'Onix', 'EcoSport', 'Toro', 'Civic', 'Corolla', 'Gol', 'Fit', 'Palio', 'Golf', 'S10', 'Cruze', 'Onix', 'EcoSport', 'Toro'],
    'Make': ['Honda', 'Fiat', 'Volkswagen', 'Chevrolet', 'Chevrolet', 'Chevrolet', 'Ford', 'Fiat', 'Honda', 'Toyota', 'Volkswagen', 'Honda', 'Fiat', 'Volkswagen', 'Chevrolet', 'Chevrolet', 'Ford', 'Fiat', 'Fiat'],
    'Color': ['Preto', 'Branco', 'Preto', 'Branco', 'Prata', 'Preto', 'Branco', 'Prata', 'Preto', 'Branco', 'Branco', 'Preto', 'Branco', 'Preto', 'Branco', 'Prata', 'Preto', 'Branco', 'Prata', 'Preto'],
    'Price': [75000, 48000, 69000, 95000, 91000, 62000, 79000, 89000, 90000, 92000, 56000, 75000, 48000, 69000, 95000, 91000, 62000, 79000, 89000, 90000],
    'Seller': ['Willian', 'Sandro', 'Paulo', 'Willian', 'Willian', 'Sandro', 'Paulo', 'Willian', 'Wagner', 'Camila', 'Wagner', 'Paulo', 'Willian', 'Paulo', 'Willian', 'Willian', 'Sandro', 'Paulo', 'Willian', 'Wagner']
}

df = pd.DataFrame(data)
df['Price'] = df['Price'].apply(lambda x: x / 1000) # convert the price to thousands
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y') # convert the date to datetime format
df = df.set_index('Date') # set the date as the index
df.sort_index(inplace=True) # sort the dataframe by date

# Display the dataframe
print(df)
