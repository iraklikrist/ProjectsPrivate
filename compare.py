import pandas as pd

# Read the CSV files into pandas dataframes
file1 = pd.read_csv('mariamgavvasheli-followers (19).csv')
file2 = pd.read_csv('mariamgavvasheli-followers (20).csv')

# Count the number of rows in each file
num_rows_file1 = len(file1)
num_rows_file2 = len(file2)

# Print the number of rows in each file
print(f"Number of rows in file 1: {num_rows_file1}")
print(f"Number of rows in file 2: {num_rows_file2}")

# Check if 'User ID' and 'Username' columns are present in both files
if 'User ID' in file1.columns and 'User ID' in file2.columns \
    and 'Username' in file1.columns and 'Username' in file2.columns:

    # Get the User IDs from each file
    user_ids_file1 = set(file1['User ID'])
    user_ids_file2 = set(file2['User ID'])

    # Find User IDs that are in one file but not in the other
    unique_user_ids_file1 = user_ids_file1 - user_ids_file2
    unique_user_ids_file2 = user_ids_file2 - user_ids_file1

    # Print the User ID and Username for unmatched User IDs
    print("\nUser IDs present only in file 1:")
    for user_id in unique_user_ids_file1:
        # Search for the corresponding row in file1
        row_file1 = file1[file1['User ID'] == user_id]
        if not row_file1.empty:
            username = row_file1.iloc[0]['Username']
            print(f"User ID: {user_id}, Username: {username}")

    print("\nUser IDs present only in file 2:")
    for user_id in unique_user_ids_file2:
        # Search for the corresponding row in file2
        row_file2 = file2[file2['User ID'] == user_id]
        if not row_file2.empty:
            username = row_file2.iloc[0]['Username']
            print(f"User ID: {user_id}, Username: {username}")
else:
    print("User ID or Username column is missing in one or both files.")
