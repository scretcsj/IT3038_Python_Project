import csv
import argparse
import re


def NIST_Control_Description(file, nist_control):
    try:
        with open(file, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            pattern = re.compile(nist_control)
            
            for row in reader:
                if pattern.match(row['control_id']):
                    print(f"Description for Control ID {row['control_id']}: {row['description']}\n")
                    return
            print(f"No Control ID matching the pattern {nist_control} found.")
    except FileNotFoundError:
        print(f"File {file} not found.")
    
    # Check any changes to the controlsheet
    except KeyError as e:
        print(f"Column not found in the CSV: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Return description of a NIST CSF control. Regex is used to check formatting.")
    parser.add_argument('file', type=str, help='Path to the CSV file.')
    parser.add_argument('control_id', type=str, help='NIST control ID to look up.')
    args = parser.parse_args()

    # Regex pattern to check format
    control_id_format = re.compile(r'^[A-Z]{2}\.[A-Z]{2}-\d{2}$')

    # Check pattern
    if not control_id_format.match(args.control_id):
        print("Control ID must be in the format XX.XX-##, ex: RC.AM-07\n")
    else:
        NIST_Control_Description(args.file, args.control_id)
