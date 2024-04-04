import pandas as pd
import plotter
import constants as c
import stats as s
import pathlib

pathlib.Path(c.DESTINATION).mkdir(parents=True, exist_ok=True)
pathlib.Path(c.DESTINATION + '/graphs').mkdir(exist_ok=True)
pathlib.Path(c.DESTINATION + '/data').mkdir(exist_ok=True)

print('Reading from csv file...')
df = pd.read_csv('eMoods-data/entry.csv')
with open(c.DESTINATION + 'data/input.txt', 'w') as file:
    file.write(df.to_markdown(index=False, tablefmt='pipe', colalign=['center']*len(df.columns)))
with open(c.DESTINATION + 'data/input.html', 'w') as file:
    file.write(c.HTML_TEMPLATE.format(title='eMoods Data', body=df.to_html()))
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
# plotter.combined_view(df_filled)
plotter.individual_graphs(df_filled)

df_sleep_filtered = df_filled[(df_filled['SLEEP'] != 0)]
plotter.sleep_analysis(df_sleep_filtered)
df_weight_filtered = df_filled[(df_filled['WEIGHT'] != 0)]
plotter.weight_analysis(df_filled, df_weight_filtered)

print('Done.')

print('Calculating statistics...')
stats = s.stats(df, df_filled)
with open(c.DESTINATION + 'data/stats.txt', 'w') as file:
    file.write(s.text.format(stats=stats))
    
with open(c.DESTINATION + 'data/stats.html', 'w') as file:
    file.write(c.HTML_TEMPLATE.format(title='Bipolar Statistics', body=s.html.format(stats=stats)))
print('Done.')

print('Generating report...')
with open(c.DESTINATION + 'Report.html', 'w') as file:
    file.write(c.HTML_TEMPLATE.format(title='Mood Analysis Report', body=(
            '<div class="container">\n<h1>Moods and Episodes</h1>\n<img src="graphs/Moods Chart.png">\n</div>\n' + s.html.format(stats=stats)
            + '<div class="container" style="width: 100%;">\n<h1>Sleep and Weight</h1>\n<img src="graphs/Sleep Analysis Chart.png">\n<img src="graphs/Weight Analysis Chart.png">\n</div>\n'
        )))
print('Done.')

print('Output sent to "' + c.DESTINATION + '"')
