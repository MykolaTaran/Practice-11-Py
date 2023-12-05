import csv 
import os 

def read_csv(file_path): 
    data = [] 
    try: 
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile: 
            reader = csv.DictReader(csvfile) 
            data = list(reader) 
    except FileNotFoundError: 
        print(f"File not found: {file_path}") 
    except Exception as e: 
        print(f"An error occurred: {e}") 
    return data

def filter_data(data, start_year, end_year):  
    filtered_data = {}  
    for row in data:  
        for key, value in row.items():  
            year_str = key[:4]  
            if year_str.isdigit():  
                year = int(year_str)  
                if start_year <= year <= end_year:  
                    if value != '': 
                        filtered_data[key] = value  
    return filtered_data

def write_csv(data, output_file): 
    try: 
        # Check if the file exists
        file_exists = os.path.isfile(output_file) 

        with open(output_file, 'a', newline='', encoding='utf-8') as csvfile: 
            fieldnames = data.keys() 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 

            # If the file doesn't exist, write the header
            if not file_exists: 
                writer.writeheader() 

            # Write data as a single row
            writer.writerow(data) 
    except Exception as e: 
        print(f"An error occurred while writing to {output_file}: {e}") 

file_path = 'UKR.csv'
output_file = 'out.csv'
country = 'Ukraine'

data = read_csv(file_path) 
if data: 
    print("File contents:") 
    print(data) 

    try: 
        # start_year = 2000
        # end_year = 2010 
        start_year = int(input("Enter start year: ")) 
        end_year = int(input("Enter end year: ")) 
    except ValueError: 
        print("Invalid input. Please enter a valid year.") 

    filtered_data = filter_data(data, start_year, end_year) 
    if filtered_data: 
        print(f"Filtered data for {country} from {start_year} to {end_year}:") 
        print(filtered_data) 

        # Write the filtered data as a single row
        write_csv(filtered_data, output_file)

        print(f"Filtered data written to {output_file}") 
    else: 
        print(f"No data found for {country} in the specified year range.") 
else: 
    print("No data to process.") 
