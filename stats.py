import pandas as pd
import constants as c

def run(df):
    with open(c.DESTINATION + 'stats.txt', 'w') as file:
        file.write('Stats\n\n')
        file.write('----- Number of Episodes Recorded -----\n')
        file.write('Depression: ' + str(episode_analysis(df['DEPRESSED']).get('episode_count')) + ' episodes\n')
        file.write('Elevated: ' + str(episode_analysis(df['ELEVATED']).get('episode_count')) + ' episodes\n')
        file.write('Anxiety: ' + str(episode_analysis(df['ANXIETY']).get('episode_count')) + ' episodes\n')
        file.write('Irritability: ' + str(episode_analysis(df['IRRITABILITY']).get('episode_count')) + ' episodes\n')
        file.write('\n')
        file.write('----- Average Time Between Episodes -----\n')
        file.write('Depression: ' + str(episode_analysis(df['DEPRESSED']).get('days_between')) + ' days\n')
        file.write('Elevated: ' + str(episode_analysis(df['ELEVATED']).get('days_between')) + ' days\n')
        file.write('Anxiety: ' + str(episode_analysis(df['ANXIETY']).get('days_between')) + ' days\n')
        file.write('Irritability: ' + str(episode_analysis(df['IRRITABILITY']).get('days_between')) + ' days\n')


def episode_analysis(data):
    counts = []
    last_i = -1
    for i in range(len(data)):
        if last_i == -1:
            if data.iloc[i] > 0:
                last_i = i
        else:
            if data.iloc[i] > 0 and i - last_i - 1 <= c.DAY_THRESHOLD:
                last_i = i
            elif data.iloc[i] > 0:
                counts.append(i - last_i - 1)
                last_i = i
    return {'episode_count': len(counts) + 1, 'days_between': round(sum(counts)/len(counts), c.PRECISION)}
