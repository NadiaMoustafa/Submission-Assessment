# Import libraries to use it
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Now i will upload a sample dataset and save it into csv file
# Example dataset
data = {
    'Size': [2000, 1500, 2500, 1800, 2200, 1600, 2400, 1900, 1700, 2300, 2100, 1550, 2600, 1750, 2000, 1650, 2450, 1850, 1700, 2250],
    'Bedrooms': [3, 2, 4, 3, 3, 2, 4, 3, 2, 4, 3, 2, 5, 3, 3, 2, 4, 3, 2, 4],
    'Location': ['Urban', 'Suburban', 'Urban', 'Rural', 'Suburban', 'Urban', 'Rural', 'Urban', 'Suburban', 'Urban', 'Suburban', 'Rural', 'Urban', 'Suburban', 'Rural', 'Urban', 'Suburban', 'Rural', 'Urban', 'Suburban'],
    'Price': [500000, 350000, 750000, 200000, 450000, 400000, 300000, 520000, 370000, 680000, 490000, 220000, 800000, 410000, 280000, 390000, 610000, 240000, 370000, 640000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

df.to_csv('house_prices.csv', index=False)
print('CSV file saved successfully.')

# Display the first few rows of the dataframe
print(df.head())

# Now i will Prepare the Data for Regression - preprocessing step
# Convert categorical variable 'Location' into dummy/indicator variables
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# Separate features (X) and target variable (y)
X = df.drop(columns=['Price'])
y = df['Price']

# Display X and y to ensure they are correctly formatted
print("Features (X):")
print(X.head())
print("\nTarget (y):")
print(y.head())

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the sizes of the train and test sets
print("Training set size:", X_train.shape[0])
print("Testing set size:", X_test.shape[0])

# Now, i will train the model using the training data.
# Initialize the linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Print the coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


# Now i will evaluate the model's performance on the testing set using metrics such as Mean Squared Error (MSE) and R-squared.
# Predict on the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE) and R-squared
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared:", r2)

print("I used MSE and R-squared as Metrics because they provide insights into the model's accuracy and goodness of fit.")

# I will test my model now, by giving some info and waiting for a predicited price.

'''If you want to predict new price, Just un-comment the next block, 
    how?  select all the next block and crtl+? and it works'''

#print("I will make the model predict some prices now")
# # Example of taking user input and predicting the price
# size = float(input("Enter the size of the house (in square feet): "))
# bedrooms = int(input("Enter the number of bedrooms: "))
# location = input("Enter the location (Urban/Suburban/Rural): ")

# # Create a dictionary with user input
# new_data = {
#     'Size': [size],
#     'Bedrooms': [bedrooms],
#     'Location': [location]
# }

# # Convert to DataFrame
# new_df = pd.DataFrame(new_data)

# # Convert categorical variable 'Location' into dummy/indicator variables
# new_df = pd.get_dummies(new_df, columns=['Location'], drop_first=True)

# # Ensure 'Location' column exists in new_df and set all values to 0 if not present
# for col in ['Location_Urban', 'Location_Suburban']:
#     if col not in new_df.columns:
#         new_df[col] = 0

# # Reorder columns to match the order in X_train
# new_df = new_df.reindex(columns=X_train.columns, fill_value=0)

# # Predict the price for the user input
# predicted_price = model.predict(new_df)

# # Convert predicted price to integer
# predicted_price_int = int(predicted_price)

# # Print the predicted price
# print("Predicted Price:", predicted_price_int)


