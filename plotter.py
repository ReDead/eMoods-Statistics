import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import constants as c

def multi_view(df):
    # Create a figure and a grid of subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 rows, 2 columns

    # Plotting the data on each subplot
    axs[0, 0].bar(df.index, df["DEPRESSED"], color = 'g', label='Depression')
    axs[0, 0].set_title('Depression')
    axs[0, 1].bar(df.index, df["ELEVATED"], color = 'b', label='Elevated')
    axs[0, 1].set_title('Elevated')
    axs[1, 0].bar(df.index, df["ANXIETY"], color = 'purple', label='Anxiety')
    axs[1, 0].set_title('Anxiety')
    axs[1, 1].bar(df.index, df["IRRITABILITY"], color = 'r', label='Irritability')
    axs[1, 1].set_title('Irritability')

    for ax in axs.flat:
        ax.set_ylim(0, 4)
        ax.set_yticks(range(0, 4), c.SEVERITY_LEVELS)

        # Set the limits of the x-axis to cover the entire range of dates
        ax.set_xlim(min(df.index), max(df.index))
        # Rotate the x-axis labels for better readability
        ax.tick_params(axis='x', rotation=45)
        # Customize date ticks
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format the date ticks as YYYY-MM-DD
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=c.DATE_INTERVAL))  # Set the interval between ticks to 7 days

        ax.set_xlabel('Date') 
        ax.set_ylabel('Severity') 

    plt.suptitle('Moods from ' + df.index.min().strftime('%Y-%m-%d') + ' to ' + df.index.max().strftime('%Y-%m-%d'))
    plt.tight_layout()
    plt.savefig(c.DESTINATION + 'Moods Chart.png')


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
    plt.savefig(c.DESTINATION + 'Combined Moods Chart.png')


def depression_sleep(df):
    # Create figure and axis objects
    fig, ax1 = plt.subplots()

    # Plotting depression as bar graph
    color = 'tab:green'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Depression Severity', color=color)
    ax1.bar(df.index, df['DEPRESSED'], color=color, label='Depression')
    ax1.set_ylim(0, 4)
    ax1.tick_params(axis='y', labelcolor=color)

    # x ticks
    # Set the limits of the x-axis to cover the entire range of dates
    ax1.set_xlim(min(df.index), max(df.index))
    # Rotate the x-axis labels for better readability
    ax1.tick_params(axis='x', rotation=45)
    # Customize date ticks
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format the date ticks as YYYY-MM-DD
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=c.DATE_INTERVAL))  # Set the interval between ticks to 7 days

    # Creating a secondary y-axis for hours slept
    ax2 = ax1.twinx()
    color = 'tab:purple'
    ax2.set_ylabel('Hours Slept', color=color)
    ax2.plot(df.index, df['SLEEP'], color=color, label='Hours Slept')
    ax2.tick_params(axis='y', labelcolor=color)

    # Set ticks for hours slept on the right side
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.set_ticks_position('right')


    plt.title("Depression's Effect on Sleep")
    plt.legend()
    plt.tight_layout()
    plt.savefig(c.DESTINATION + 'Depression and Sleep Chart.png')