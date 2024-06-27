#!/bin/bash

# Function to process a single file
process_file() {
  local file=$1
  local output_dir=$2
  local stock_id=$(basename "$file" .csv)

  # Call the first Python script to get 10 consecutive data points
  python3 get_data_points.py "$file" > "${output_dir}/${stock_id}_data_points.csv"

  # Call the second Python script to get predictions
  python3 predict_values.py "${output_dir}/${stock_id}_data_points.csv" > "${output_dir}/${stock_id}_predictions.csv"
}

# Main script logic
input_dir=$1
output_dir=$2
num_files_to_sample=$3

# Create output directory if it doesn't exist
mkdir -p "$output_dir"

# Process files for each exchange
for exchange_dir in "$input_dir"/*; do
  exchange=$(basename "$exchange_dir")
  echo "Processing exchange: $exchange"

  files=("$exchange_dir"/*.csv)
  total_files=${#files[@]}
  files_to_process=$((total_files < num_files_to_sample ? total_files : num_files_to_sample))

  for ((i = 0; i < files_to_process; i++)); do
    process_file "${files[i]}" "$output_dir"
  done
done

