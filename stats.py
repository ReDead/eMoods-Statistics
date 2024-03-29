import pandas as pd
import constants as c

def run(df, df_filled):
    with open(c.DESTINATION + 'stats.txt', 'w') as file:
        file.write('Stats\n\n')
        file.write('Total days recorded: ' + str(len(df)) + '\n')
        file.write('Total date range: ' + df_filled.index.min().strftime('%Y-%m-%d') + ' to ' + df_filled.index.max().strftime('%Y-%m-%d') + '\n')
        file.write('Total days in date range: ' + str(len(df_filled)) + '\n')
        file.write('\n')
        file.write('----- Number of Episodes Recorded -----\n')
        file.write('Depression: ' + str(episode_analysis(df_filled['DEPRESSED']).get('episode_count')) + ' episodes\n')
        file.write('Elevated: ' + str(episode_analysis(df_filled['ELEVATED']).get('episode_count')) + ' episodes\n')
        file.write('Anxiety: ' + str(episode_analysis(df_filled['ANXIETY']).get('episode_count')) + ' episodes\n')
        file.write('Irritability: ' + str(episode_analysis(df_filled['IRRITABILITY']).get('episode_count')) + ' episodes\n')
        file.write('\n')
        file.write('----- Average Time Between Episodes -----\n')
        file.write('Depression: ' + str(episode_analysis(df_filled['DEPRESSED']).get('days_between')) + ' days\n')
        file.write('Elevated: ' + str(episode_analysis(df_filled['ELEVATED']).get('days_between')) + ' days\n')
        file.write('Anxiety: ' + str(episode_analysis(df_filled['ANXIETY']).get('days_between')) + ' days\n')
        file.write('Irritability: ' + str(episode_analysis(df_filled['IRRITABILITY']).get('days_between')) + ' days\n')
        file.write('\n')
        file.write('----- Average Episode Duration -----\n')
        file.write('Depression: ' + str(episode_analysis(df_filled['DEPRESSED']).get('duration')) + ' days\n')
        file.write('Elevated: ' + str(episode_analysis(df_filled['ELEVATED']).get('duration')) + ' days\n')
        file.write('Anxiety: ' + str(episode_analysis(df_filled['ANXIETY']).get('duration')) + ' days\n')
        file.write('Irritability: ' + str(episode_analysis(df_filled['IRRITABILITY']).get('duration')) + ' days\n')



def episode_analysis(data):
    episodes = []

    start = -1
    end = -1
    asym_count = 0
    for i in range(len(data)):
        if start == -1:
            if data.iloc[i] > 0:
                start = i
                end = i
        else:
            if data.iloc[i] <= 0 and asym_count < c.DAY_THRESHOLD:
                asym_count += 1
            elif data.iloc[i] <= 0:
                episodes.append([start, end + 1])
                start = -1
                asym_count = 0
            else:
                end = i
    if start != -1:
        episodes.append([start, end])        
    
            
    return {
        'episode_count': len(episodes),
        'days_between': round(sum([episodes[i][0] - episodes[i-1][1] for i in range(1, len(episodes))])/(len(episodes) - 1), c.PRECISION),
        'duration': round(sum([episode[1] - episode[0] for episode in episodes])/len(episodes), c.PRECISION)
        }
