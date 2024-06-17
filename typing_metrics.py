import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def process_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file, processes the data to compute daily averages of words per minute and accuracy.

    Args:
        file_path (str): The path to the CSV file containing the data.

    Returns:
        pd.DataFrame: A DataFrame containing the daily averages of words per minute and accuracy.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Convert timestamp to datetime format
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms').dt.date

    # Calculate the mean wpm and acc for each date
    df['wpm'] = pd.to_numeric(df['wpm'], errors='coerce')
    df['acc'] = pd.to_numeric(df['acc'], errors='coerce')
    
    daily_averages = df.groupby('date').agg({
        'wpm': 'mean',
        'acc': 'mean'
    }).reset_index()

    return daily_averages

def plot_daily_averages(daily_averages: pd.DataFrame) -> None:
    """
    Plots the daily averages of words per minute and accuracy.

    Args:
        daily_averages (pd.DataFrame): A DataFrame containing the daily averages of words per minute and accuracy.
    """
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot words per minute on the primary y-axis
    ax1.plot(daily_averages['date'], daily_averages['wpm'], label='Words Per Minute', color='b', linestyle='-', marker='o')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Words Per Minute', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.grid(True)

    # Create a secondary y-axis for accuracy
    ax2 = ax1.twinx()
    ax2.plot(daily_averages['date'], daily_averages['acc'], label='Accuracy', color='r', linestyle='--', marker='o')
    ax2.set_ylabel('Accuracy', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    ax2.grid(False)

    # Adding titles and labels
    plt.title('Daily Averages of Words Per Minute and Accuracy')
    fig.tight_layout()  # Adjust layout to fit both y labels

    # Add legends
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Save plot to a file
    plt.savefig('daily_averages.png', bbox_inches='tight')

def plot_histogram(data: pd.Series, xlabel: str, title: str, bins: int = 10) -> None:
    """
    Plots a histogram of the given data.

    Args:
        data (pd.Series): The data series to plot.
        xlabel (str): Label for the x-axis.
        title (str): Title of the plot.
        bins (int): Number of bins for the histogram (default is 10).
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.title(title)
    plt.grid(True)
    plt.savefig('histogram.png', bbox_inches='tight')
    plt.show()

def plot_scatter(x_data: pd.Series, y_data: pd.Series, xlabel: str, ylabel: str, title: str) -> None:
    """
    Plots a scatter plot of x_data vs y_data.

    Args:
        x_data (pd.Series): Data for the x-axis.
        y_data (pd.Series): Data for the y-axis.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig('scatter.png', bbox_inches='tight')
    plt.show()

# Example usage:
if __name__ == "__main__":
    file_path = 'results.csv'
    daily_averages = process_csv(file_path)
    
    plot_daily_averages(daily_averages)
    
    # Example of plotting histogram of words per minute (wpm)
    plot_histogram(daily_averages['wpm'], 'Words Per Minute', 'Histogram of Words Per Minute')

    # Example of plotting scatter plot of words per minute (wpm) vs accuracy (acc)
    plot_scatter(daily_averages['wpm'], daily_averages['acc'], 'Words Per Minute', 'Accuracy', 'Scatter Plot: WPM vs Accuracy')

