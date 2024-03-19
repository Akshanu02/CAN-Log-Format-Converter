import pandas as pd
import re

def parse_asc_line(line):
    timestamp = re.search(r'Timestamp: (\d+\.\d+)', line).group(1)
    can_id = re.search(r'ID: ([0-9A-Fa-f]+)', line).group(1)
    data_match = re.search(r'DL: \s*(\d+)\s+((?:[0-9A-Fa-f]{2}\s*)+)', line)
    data = data_match.group(2) if data_match else ""
    channel = re.search(r'Channel: (\d+)', line).group(1)

    return [timestamp, can_id, data, channel]

def asc_to_csv(input_file, output_file):
    can_data = []

    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith("Timestamp:"):
                can_data.append(parse_asc_line(line))

    df = pd.DataFrame(can_data, columns=['Timestamp', 'ID', 'Data', 'Channel'])

    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "battery.asc"  # Replace with your input .asc file
    output_file = "output_log.csv"  # Replace with your desired output .csv file

    asc_to_csv(input_file, output_file)
