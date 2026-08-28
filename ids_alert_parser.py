import json 
import csv 

# Open file 'alerts-only.json' in 'r' read mode
try:
    with open('alerts-only.json', 'r') as f:
        alerts = json.load(f) # Load 'alerts-only.json' in a list
        print(f"\nTotal alerts read: {len(alerts)}") # Count how many elements there are
# Handle missing input file        
except FileNotFoundError: 
    print("\nFile input not found.")
    exit()
except Exception as error:
    print(f"\nError while reading JSON: {error}")
    exit()

# Open/create file .csv in 'w' write mode 
try:
    with open('alerts_parsed.csv', 'w', newline='') as csvfile:
        fieldnames = [
            'timestamp','src_ip', 'src_port', 'dest_ip', 'dest_port', 
            'proto', 'app_proto', 'signature_id', 'signature', 'category', 'severity'
            ]
        # Create a DictWriter object to map fieldnames to CSV columns
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write header row with column names 
        writer.writeheader()

        # Counters for console display
        severity_count = {}
        category_count = {}
        # List for writing in both CSV and JSON files (sorted by timestamp)
        rows_list = []

        # for loop: Extract and process each alert
        for alert in alerts:
            row = {
            # Timestamp truncated and chained, cleaned by microseconds
            'timestamp':    alert.get("timestamp", "N/A")[:19] + alert.get("timestamp", "N/A")[-5:],
            'src_ip':       alert.get("src_ip", "N/A"),
            'src_port':     alert.get("src_port", "N/A"),
            'dest_ip':      alert.get("dest_ip", "N/A"),
            'dest_port':    alert.get("dest_port", "N/A"),
            'proto':        alert.get("proto", "N/A"),
            'app_proto':    alert.get("app_proto", "N/A"),
            # Extract nested fields from alert object with fallback to "N/A"
            'signature_id': alert.get("alert", {}).get("signature_id", "N/A"),
            'signature':    alert.get("alert", {}).get("signature", "N/A"),
            'category':     alert.get("alert", {}).get("category", "N/A"),    
            'severity':     alert.get("alert", {}).get("severity", "N/A")
            }
            # Append the row to rows_list for JSON and CSV export
            rows_list.append(row) 
            
            # Track severity and category occurrences
            severity_count[row['severity']] = severity_count.get(row['severity'], 0) + 1
            category_count[row['category']] = category_count.get(row['category'], 0) + 1
            
        # Sort rows by timestamp before writing 
        rows_list.sort(key=lambda x: x['timestamp'])
        for row in rows_list:
            writer.writerow(row)
    print("Parsing completed, CSV file saved in alerts_parsed.csv")
# Error handling
except Exception as e:
    print(f"\nError while writing CSV: {e}")
    exit()

# Write to JSON file
try:
    with open('alerts_parsed.json', 'w') as jsonfile:
        json.dump(rows_list, jsonfile, indent=2)
    print("File JSON saved in alerts_parsed.json")
# Error handling
except Exception as e:
    print(f"\nError while writing JSON: {e}")
    exit()   

# Display summary tables sorted by count to stdout
severity_sorted = sorted(severity_count.items(), reverse=True)
category_sorted = sorted(category_count.items(), key=lambda x: x[1], reverse=True)

print("\n=== SEVERITY SUMMARY ===")
for severity, count in severity_sorted:
    print(f"Severity {severity}: {count} alerts")

print("\n=== CATEGORY SUMMARY ===")
for category, count in category_sorted:
    print(f"{category}: {count} alerts")    
