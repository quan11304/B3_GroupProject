import pandas as pd

input_file = 'ForGit/DDoS-Detection-By-ML/feature_extraction/LDAP-training.csv'
output_file = 'ForGit/DDoS-Detection-By-ML/feature_extraction/converted_flow_features.csv'

column_mapping = {
    " Source IP": "Source",
    " Destination IP": "Destination",
    " Protocol": "Protocol",
    " Timestamp": "Time",
    " Label": "label",

}

output_header = ["Time", "Source", "Destination", "Protocol", "Length","Info","label"]

data = pd.read_csv(input_file)

data['Length'] = data["Total Length of Fwd Packets"] + data[" Total Length of Bwd Packets"]
data['Info'] = data[" Source Port"].astype(str) + " -> " + data[" Destination Port"].astype(str)

data = data.rename(columns=column_mapping)
filtered_data = data[output_header]

filtered_data.to_csv(output_file, index=False)
print(f"Filtered data saved to {output_file}.")
