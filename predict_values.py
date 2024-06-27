import sys
import pandas as pd

def predict_values(data_points):
    stock_id = data_points['Stock-ID'].iloc[0]
    timestamps = data_points['Timestamp']
    prices = data_points['stock price'].tolist()
    
    n1 = sorted(prices)[-2]  # Second highest value in the 10 data points
    n2 = prices[-1] + 0.5 * (n1 - prices[-1])
    n3 = n2 + 0.25 * (n2 - prices[-1])
    
    predictions = [
        [stock_id, timestamps.iloc[-1], prices[-1]],
        [stock_id, "", n1],
        [stock_id, "", n2],
        [stock_id, "", n3]
    ]
    return predictions

if __name__ == "__main__":
    input_file = sys.argv[1]
    data_points = pd.read_csv(input_file)
    predictions = predict_values(data_points)
    prediction_df = pd.DataFrame(predictions, columns=['Stock-ID', 'Timestamp', 'stock price'])
    prediction_df.to_csv(sys.stdout, index=False)

