# Submission-Assessment
Its contents :
* Part 1

* Part 2

* Part 3
* Readme file
* Notebook

Notes regarding Part 1 :
* You can just take the code copy and run it without download the dataset.csv file, the code includes the data. i just put the dataset for clarrifcation.
* I provided 2 datasets (the orignal one, and clean one), code.py for python code, and app.py for flask app
* In the files there are comments illustrate everything.
* In the APP flask :
    * you can test your /top_employees and /employees_in_department endpoints using various tools, For example like curl.
    * And the answers will return as json format
    * you can use these curl for two endpoints when you try to test :
      1. To get the top N highest-paid employees, you can make a GET request to the /top_employees endpoint with the optional parameter N.
      2. For example : curl "http://127.0.0.1:5000/top_employees?N=3".  Just write this http://127.0.0.1:5000/top_employees?N=3 in the URL (You can choose any number not just 3 of course).
      3. To get the number of employees in a specific department, you need to provide the X parameter.
      4. For example : curl "http://127.0.0.1:5000/employees_in_department?X=Finance"  The same as point 2.

Notes regarding Part 2 :
* In the code.py file, you will find the model with metrics, and there is a final block. I made it as a comment, but if you want to predict new prices for any house, just uncomment it, and it will run successfully. It just asks you for information about your house, which you need to predict its price.
