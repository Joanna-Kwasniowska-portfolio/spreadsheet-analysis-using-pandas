import pandas as pd

df = pd.read_csv('sales.csv')

print(f"Original Data\n {df}")

# Collect all sales from each month into a single list
all_sales = df['sales'].tolist()
print(f"My all_sales List: {all_sales}")

# Output the total sales across all months
total_sales = df['sales'].sum()
print(f"\nTotal Sales Across All Months: {total_sales}")

# Find the month with the highest sales
max_sales_month = df.loc[df['sales'].idxmax()]['month']
print(f"\nMonth with Highest Sales:{max_sales_month}")

# Find the month with the lowest sales
min_sales_month = df.loc[df['sales'].idxmin()]['month']
print(f"\nMonth with Lowest Sales: {min_sales_month}")

# Calculate profit for each month
df['profit'] = df['sales'] - df['expenditure']


# Display the updated DataFrame
print(f"\nUpdated DataFrame with Profit for Each Month:\n {df}")

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_spreadsheet_with_profit.csv', index=False)

# Calculate the total expenditure
total_expenditure = df['expenditure'].sum()
print(f"\nTotal Expenditure for All Months: {total_expenditure}")


# Calculate the average sales
average_sales = df['sales'].mean()
print(f"\nAverage sales: {round(average_sales, 2)}")


# Create a summary DataFrame
summary_data = {
    'Average Sales': [average_sales],
    'Month with Highest Sales': [max_sales_month],
    'Month with Lowest Sales': [min_sales_month],
    'Total Expenditure': [total_expenditure]
}

print(f"Dictionary that contains summary information: \n{summary_data}")


summary_df = pd.DataFrame(summary_data)

# Save the summary to a new spreadsheet
summary_df.to_csv('summary_results.csv', index=False)