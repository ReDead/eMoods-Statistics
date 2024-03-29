import pandas as pd
import constants as c

html = '''<body>
    <div class="container">
        <h1>Bipolar Episode Statistics</h1>

        <h2>Totals</h2>
        <table>
            <tr>
                <th>Statistic</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Days Recorded</td>
                <td>{stats.totals.days}</td>
            </tr>
            <tr>
                <td>Date Range</td>
                <td>{stats.totals.date_range}</td>
            </tr>
            <tr>
                <td>Days in Date Range</td>
                <td>{stats.totals.days_in_range}</td>
            </tr>
        </table>

        <h2>Number of Episodes Recorded</h2>
        <table>
            <tr>
                <th>Mood Type</th>
                <th>Episodes</th>
            </tr>
            <tr>
                <td>Depression</td>
                <td>{stats.episode_count.depression}</td>
            </tr>
            <tr>
                <td>Elevated</td>
                <td>{stats.episode_count.elevated}</td>
            </tr>
            <tr>
                <td>Anxiety</td>
                <td>{stats.episode_count.anxiety}</td>
            </tr>
            <tr>
                <td>Irritability</td>
                <td>{stats.episode_count.irritability}</td>
            </tr>
        </table>

        <h2>Average Time Between Episodes</h2>
        <table>
            <tr>
                <th>Mood Type</th>
                <th>Average Time</th>
            </tr>
            <tr>
                <td>Depression</td>
                <td>{stats.days_between.depression}</td>
            </tr>
            <tr>
                <td>Elevated</td>
                <td>{stats.days_between.elevated}</td>
            </tr>
            <tr>
                <td>Anxiety</td>
                <td>{stats.days_between.anxiety}</td>
            </tr>
            <tr>
                <td>Irritability</td>
                <td>{stats.days_between.irritability}</td>
            </tr>
        </table>

        <h2>Average Episode Duration</h2>
        <table>
            <tr>
                <th>Mood Type</th>
                <th>Average Duration</th>
            </tr>
            <tr>
                <td>Depression</td>
                <td>{stats.duration.depression} days</td>
            </tr>
            <tr>
                <td>Elevated</td>
                <td>{stats.duration.elevated} days</td>
            </tr>
            <tr>
                <td>Anxiety</td>
                <td>{stats.duration.anxiety} days</td>
            </tr>
            <tr>
                <td>Irritability</td>
                <td>{stats.duration.irritability} days</td>
            </tr>
        </table>
    </div>
</body>
</html>
'''

text = '''Stats

Total days recorded: {stats.totals.days}
Total date range: {stats.totals.date_range}
Total days in date range: {stats.totals.days_in_range}

----- Number of Episodes Recorded -----
Depression: {stats.episode_count.depression}
Elevated: {stats.episode_count.elevated}
Anxiety: {stats.episode_count.anxiety}
Irritability: {stats.episode_count.irritability}

----- Average Time Between Episodes -----
Depression: {stats.days_between.depression}
Elevated: {stats.days_between.elevated}
Anxiety: {stats.days_between.anxiety}
Irritability: {stats.days_between.irritability}

----- Average Episode Duration -----
Depression: {stats.duration.depression}
Elevated: {stats.duration.elevated}
Anxiety: {stats.duration.anxiety}
Irritability: {stats.duration.irritability}
'''


class totals:
    def __init__(self, df, df_filled):
        self.days = len(df)
        self.date_range = df_filled.index.min().strftime('%Y-%m-%d') + ' to ' + df_filled.index.max().strftime('%Y-%m-%d')
        self.days_in_range = len(df_filled)
class episode_count:
    def __init__(self, df_filled):
        self.depression = episode_analysis(df_filled['DEPRESSED']).get('episode_count')
        self.elevated = episode_analysis(df_filled['ELEVATED']).get('episode_count')
        self.anxiety = episode_analysis(df_filled['ANXIETY']).get('episode_count')
        self.irritability = episode_analysis(df_filled['IRRITABILITY']).get('episode_count')
class days_between:
    def __init__(self, df_filled):
        self.depression = episode_analysis(df_filled['DEPRESSED']).get('days_between')
        self.elevated = episode_analysis(df_filled['ELEVATED']).get('days_between')
        self.anxiety = episode_analysis(df_filled['ANXIETY']).get('days_between')
        self.irritability = episode_analysis(df_filled['IRRITABILITY']).get('days_between')
class duration:
    def __init__(self, df_filled):
        self.depression = episode_analysis(df_filled['DEPRESSED']).get('duration')
        self.elevated = episode_analysis(df_filled['ELEVATED']).get('duration')
        self.anxiety = episode_analysis(df_filled['ANXIETY']).get('duration')
        self.irritability = episode_analysis(df_filled['IRRITABILITY']).get('duration')
class stats:
    def __init__(self, df, df_filled):
        self.totals = totals(df, df_filled)
        self.episode_count = episode_count(df_filled)
        self.days_between = days_between(df_filled)
        self.duration = duration(df_filled)


def run(df, df_filled):
    with open(c.DESTINATION + 'stats.txt', 'w') as file:
        file.write(text.format(stats=stats(df, df_filled)))
    
    with open(c.DESTINATION + 'stats.html', 'w') as file:
        file.write(c.HTML_HEAD.format(title='Bipolar Statistics') + html.format(stats=stats(df, df_filled)))


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
