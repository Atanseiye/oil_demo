from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_3(data):


    # Assuming 'data' is your DataFrame
    cali_scaler = MinMaxScaler()
    gr_scaler = MinMaxScaler()
    dt_scaler = MinMaxScaler()

    # Store the original values
    original_depth = data['DEPTH'].values  # Store original DEPTH values
    original_values = {
        'CALI': data['CALI'].values,
        'GR': data['GR'].values,
        'DT': data['DT'].values,
    }

    # Scale the values
    feature_ = pd.DataFrame()
    feature_['CALI'] = cali_scaler.fit_transform(data[['CALI']]).flatten()
    feature_['GR'] = gr_scaler.fit_transform(data[['GR']]).flatten()
    feature_['DT'] = dt_scaler.fit_transform(data[['DT']]).flatten()
    feature_['DEPTH'] = dt_scaler.fit_transform(data[['DEPTH']]).flatten()  # Scaled depth

    features = ['CALI', 'GR', 'DT']

    plt.figure(figsize=(7, 78))  # Create a single figure

    for feature in features:
        sns.lineplot(
            y=feature_['DEPTH'], 
            x=feature_[feature], 
            label=feature, 
            orient='y'
        )

    # Convert y-axis (DEPTH) back to original values
    ax = plt.gca()
    ax.set_yticks(feature_['DEPTH'][::500])  # Select tick locations
    ax.set_yticklabels(original_depth[::500])  # Set tick labels to original values

    # Convert x-axis (features) back to original values
    def scale_back(value, feature_name):
        """Convert scaled values back to original scale."""
        min_val, max_val = original_values[feature_name].min(), original_values[feature_name].max()
        return value * (max_val - min_val) + min_val

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{scale_back(x, 'CALI'):.2f}"))

    # Add title, labels, and legend
    plt.title('Distribution of Features Across DEPTH', fontsize=16)
    plt.xlabel('Feature Value', fontsize=14)
    plt.ylabel('DEPTH', fontsize=14)
    plt.legend(title='Features', fontsize=12)
    plt.grid(True)

    plt.gca().invert_yaxis()
    plt.gca().invert_xaxis() 

    plt.tight_layout()
    plt.show()
