import pandas as pd
import plotter
import constants as c
import stats

print('Reading from csv file...')
df = pd.read_csv('eMoods-data/entry.csv')
print('Done.')

print('Filtering data and plotting...')
df[c.DATE] = pd.to_datetime(df[c.DATE])

df['DEPRESSED'] = df['DEPRESSED'].sub(1)
df['ANXIETY'] = df['ANXIETY'].sub(1)
df['IRRITABILITY'] = df['IRRITABILITY'].sub(1)
df['ELEVATED'] = df['ELEVATED'].sub(1)

# Create a complete date range including missing dates
complete_dates = pd.date_range(start=df[c.DATE].min(), end=df[c.DATE].max())
# Reindex the DataFrame with the complete date range and fill missing values with zeros
df_filled = df.set_index(c.DATE).reindex(complete_dates).fillna(0)

plotter.multi_view(df_filled)
plotter.combined_view(df_filled)

df_sleep_filtered = df[(df['SLEEP'] != 0)]
plotter.depression_sleep(df_sleep_filtered)

print('Done.')
print('Output sent to "' + c.DESTINATION + '"')

print('Calculating statistics...')
stats.run(df_filled)
print('Done.')