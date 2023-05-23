formatted_data = []

file_path = 'yearstats/2014.txt'  # Replace with the actual path to your file

with open(file_path, 'r') as file:
    for line in file:
        values = line.split("\t")
        # Points, Assists, 3-pointers Made, Rebounds, Blocks, Steals
        formatted_values = (
            ''.join(values[1].replace("'", "")),
            float(values[5]),
            float(values[16]),
            float(values[9]),
            float(values[15]),
            float(values[18]),
            float(values[17])
        )
        if(formatted_values not in formatted_data):
            formatted_data.append(formatted_values)
    

print(formatted_data)