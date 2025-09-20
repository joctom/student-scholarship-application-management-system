import csv 
import json 


def exportCSV(data, filename='report.csv'):
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["name", "birthdate", "birthplace", "sex", "status", "region", "province", "city", "brgy", "code", "number", "email", "fb", "father", "occupation1", "mother", "occupation2", "siblings", "income", "application", "lrn", "school", "gwa", "college", "degree", "yesno"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for record in data["student_record"]:
                writer.writerow(record)
        print(f"Report successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing the CSV file: {e}")

