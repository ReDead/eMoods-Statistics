import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import constants as c

def individual_graph(ax, df, i):
    ax.bar(df.index, df[c.MOODS[i]], color = c.MOOD_COLORS[i])
    ax.set_title(c.MOOD_TITLES[i])

    ax.set_ylim(0, 4)
    ax.set_yticks(range(0, 4), c.SEVERITY_LEVELS)

    # Set the limits of the x-axis to cover the entire range of dates
    ax.set_xlim(min(df.index) - pd.Timedelta(days=c.PADDING), max(df.index) + pd.Timedelta(days=c.PADDING))
    # Rotate the x-axis labels for better readability
    ax.tick_params(axis='x', rotation=45)
    # Customize date ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format the date ticks as YYYY-MM-DD
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=c.DATE_INTERVAL))  # Set the interval between ticks to 7 days

    ax.set_xlabel('Date') 
    ax.set_ylabel('Severity')

def individual_graphs(df):
    for i in range(4):
        plt.figure()
        ax = plt.subplot()
        individual_graph(ax, df, i)
        plt.tight_layout()
        plt.savefig(c.DESTINATION + 'graphs/' + c.MOOD_TITLES[i] + ' Chart.png')

def multi_view(df):
    # Create a figure and a grid of subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 rows, 2 columns

    for i in range(4):
        individual_graph(axs[(i & 2) >> 1, i & 1], df, i)
    
    plt.suptitle('Moods from ' + df.index.min().strftime('%Y-%m-%d') + ' to ' + df.index.max().strftime('%Y-%m-%d'))
    plt.tight_layout()
    plt.savefig(c.DESTINATION + 'graphs/Moods Chart.png')


def combined_view(df):
    plt.figure()

    bar_width = .2
    # Define the x-axis positions for the bars
    x = np.arange(len(df))
    # Plot the bars for each value, adjusting the x-coordinates based on the bar width
    for i, col in enumerate(df.columns[2:6]):
        plt.bar(x + (bar_width * i), df[col], width=bar_width, label=col.title())

    # plt.bar(df.index, df["DEPRESSED"], color = 'g', label='Depression')
    # plt.bar(df.index, df["ELEVATED"], color = 'b', label='Elevated')
    # plt.bar(df.index, df["ANXIETY"], color = 'purple', label='Anxiety')
    # plt.bar(df.index, df["IRRITABILITY"], color = 'r', label='Irritability')

    plt.ylim(0, 5)
    plt.yticks(range(0, 5))

    
    # Set the limits of the x-axis to cover the entire range of dates
    # plt.xlim(-DATE_INTERVAL, len(df.index) + DATE_INTERVAL)
    # Rotate the x-axis labels for better readability'
    plt.xlim(-1, len(df))
    plt.xticks(x, df.index.strftime('%Y-%m-%d'), rotation=45)

    plt.xlabel('Date') 
    plt.ylabel('Severity')
    
    plt.title('Moods Combined View')
    plt.legend()
    plt.tight_layout()
    plt.savefig(c.DESTINATION + 'graphs/Combined Moods Chart.png')


def sleep_analysis(df):
    # Create figure and axis objects
    fig, axs = plt.subplots(1, 2, figsize=(20, 8))

    for i in range(2):
        individual_graph(axs[i], df, i)

        # Creating a secondary y-axis for hours slept
        ax2 = axs[i].twinx()
        ax2.set_ylabel('Hours Slept', color='purple')
        ax2.plot(df.index, df['SLEEP'], color='purple', label='Hours Slept')
        ax2.tick_params(axis='y', labelcolor='purple')

        # Set ticks for hours slept on the right side
        ax2.yaxis.set_label_position('right')
        ax2.yaxis.set_ticks_position('right')


    plt.suptitle("Sleep Analysis")
    plt.tight_layout()
    plt.savefig(c.DESTINATION + 'graphs/Sleep Analysis Chart.png')

def weight_analysis(df, df_filtered):
    plt.figure(figsize=(10, 8))
    ax = plt.subplot()

    individual_graph(ax, df, 0)

    ax2 = ax.twinx()
    ax2.set_ylabel('Weight (lbs)', color='purple')
    ax2.plot(df_filtered.index, df_filtered['WEIGHT'], color='purple', label='Weight')
    ax2.tick_params(axis='y', labelcolor='purple')

    ax2.yaxis.set_label_position('right')
    ax2.yaxis.set_ticks_position('right')

    plt.suptitle("Weight Analysis")
    plt.tight_layout()
    plt.savefig(c.DESTINATION + 'graphs/Weight Analysis Chart.png')