
# Introduction

This project/challenge is divided into 4 parts: API Access, File Type Manipulation, Data Exploration and Model Creation
​
This challenge will involve querying an API and extracting information from it. The API in question provides information on Game of Thrones, allowing one to access information on the houses, characters and books.
​
* API URL: http://anapioficeandfire.com/api/{SECTION}/{INDEX}
​
Where SECTION can be either ‘books’, ‘characters’, or ‘houses’ and INDEX is an integer to a certain entry in a section.
​
For example, to access the character Peter Baelish, the full request would be http://anapioficeandfire.com/api/characters/823, where 823 is the index corresponding to that character. 
​
It's recommended to read the full documentation, which can be found here: https://anapioficeandfire.com/Documentation.
​
We would like you to answer the following:
​
* a) What index corresponds to the house “House Breakstone”?
 
* b) How many males, females and unknown genders are there in the first 40 characters? Note, index 0 does not correspond to a character, so full range is 1 - 40 both ends inclusive. 
​
* c) How many books can be accessed from this API?
​
* d) How many books does the character ‘High Septon’ appear in? (ignoring ‘povcharacters’).
​
Hint: index value of Septon needs to be found first; it is smaller than 20.
​
* File type manipulation and formatting:
​
Three files are presented, one CSV, one TXT and one JSON file. Each contain 1000 rows of data. There are two challenges, both involving collating these files into one data frame. The fields in all files are:
​
'author.properties.friends',  'author.properties.status_count',  'author.properties.verified',  'content.body',  'location.country',  'properties.platform',  'properties.sentiment',  'location.latitude',  'location.longitude'
​
where the ‘.’ Indicates a nested field.
 
* a) Begin by collating the CSV and TXT files together into one pandas dataframe. The resulting dataframe should be 2000 rows and have all of the columns present in both files.
​
* b) Next, using the created dataframe, integrate the data from the JSON file into the existing columns. The resulting dataframe should now be 3000 rows long.
​
* Data Exploration:
​
In this challenge we would like to know something interesting about the data. You are free to explore as you wish, producing plots, tables, statistics, etc. Feel free to use any variables in the dataset or include external data you may consider relevant to complement your analysis.  
​
* Model Creation:
​
For this task you can use AutoGluon or you preferred algorithm.
​
This final task involves creating a predictive model for a response variable, given a set of features. The task is to create a predictive model for the variable ‘properties.sentiment’ using the remaining features in the data set. 
​
The data files attached should be used to create the model.  
​
What we would like to see from this task is your thoughts and decisions on training and testing a model. This will include, but not limited to, considering aspects such as feature selection & creation, parameter tuning of the model and train / validation / test split. 
​
This task is a blank canvas to work with. The only caveat is that you must be able to explain the methods and models you are using.

# Data Sources
Two datasources are used in this project:
* 1. A Public API on Game of Thrones
The API provides information on Game of Thrones, allowing one to access information on the houses, characters and books.
* API URL: http://anapioficeandfire.com/api/{SECTION}/{INDEX}
Where SECTION can be either 'books', 'characters', or 'houses' and INDEX is an integer to a certain entry in a section.
* 2. Data on Love Island Sentiment Analysis, as found in the "data" folder. Data is comprised of 3 files: csv_file.csv, json_file.json, txt_file.txt

# Environment Setup
Available initial environment setup files.

```bash
environment.yml
requirements.txt
```

```bash
conda env create -f environment.yml
conda activate twittersentiment_env


```
Step 1: Create repository on github

```
"github.com/your_username/twitter_sentiment_prediction"

```

Step 2: Clone repository in preferred directory location on local computer  
```
git clone https://github.com/gkadeoti/twitter_sentiment_prediction

```

Step 3: Create environment using `environment.yml` file

```
conda env create -f environment.yml

```

Step 4: Activate the environment

```
conda activate (ENVIRONMENT NAME)

```
conda activate twittersentiment_env


# Project Structure
- API Data Call
- DataFrame Merging
- Data Exploration
- Model Building

# API Data Call
* Important Note: Read the GOT API Documentation: https://anapioficeandfire.com/Documentation and the Requests Doumentation: https://requests.readthedocs.io/en/latest/user/quickstart/

Step 1: Preambles.
* 1a: Import the relevant libraries and packages for the API call: pandas and requests.
* 1b: Confirm acess to the API root url

Step 2: For Question (a)
* 2a: Specify the Houses URL
* 2b: Specify the parameters for Breakstone
* 2c: Make a request to the API
* 2d: Read in the result as a json file

Step 3: For Question (b)
* 3a: Write a function to obtain a single character from the API.
* 3b: Write another function to obtain multiple characters from the API.
* 3c: Obtain the first 40 characters (the result should be a list)
* 3d: Convert the list into a dataframe.
* 3e: Check the unique values for the "gender")column.
* 3f: Check/determine the number of each unique value in the "gender" column.

Step 4: For Question (c)
* 4a: Specify the API URL with the section and index.
* 4b: Send a GET request to the API.
* 4c: Using while loop, write a function for the SECTION 'books', which returns a count for INDEXES successfully called in the URL.
* 4d: If the response status code is not 200 (success), exit the loop.
* 4e: Increment the count and index.
* 4f: Call the function to get the number of books.

Step 5: For Question (d)
* 5a: Specify the Characters URL
* 5b: Specify the parameters for "High Septon"
* 5c: Make a request to the API
* 5d: Read in the result as a json file



# DataFrame Merging
Step 1: Preambles.
* 1a: Import the relevant libraries for the DataFrame merge: pandas, numpy, os.
* 1b: Check the working directory.
* 1c: Specify the relevant folders in working directory: main_working_folder, data_folder, output_folder.
* 1d: Specify the file path.
* 1e: Check the contents of the file path (you should have three files: one CSV, one TXT and one JSON file).

Step 2: Merge CSV and TXT files.
* 2a: Read in CSV file.
* 2b: Inspect the CSV data.
* 2c: Adjust the data types.
* 2d: Confirm the data type has been adjusted.
* 2e: Read in the TXT file.
* 2f: Inspect the TXT data.
* 2g: Check that the TXT data and CSV data have corresponding data types and shapes.
* 2h: Use pd.concat to combine the CSV and TXT dataframes.
* 2i: Inspect the combined dataframe.

Step 3: Merge the combined dataframe with the JSON file.
* 3a: Use Python JSON module to load in JSON file.
* 3b: Use json_normalize to convert JSON file to pandas dataframe.
* 3c: Inspect JSON data.
* 3d: Check that the TXT and CSV dataframe and the JSON data have corresponding data types and shapes.
* 3e: Use pd.concat to merge JSON dataframe to combined TXT and CSV dataframe.
* 3f: Inspect the final merged dataframe.
* 3g: Specify save path and write merged dataframe into a new CSV file.


# Data Exploration
Step 1: Preambles.
* 1a: Import the required packages for data exploration: matplotlib, folium, scikit-learn
* 1b: Confirm working directory
* 1c: Read in final merged data

Step 2: Data Inspection
* 2a: Inspect the merged dataframe
* 2b: To check and identify null values
* 2c: Drop rows with null values in the predicted/outcome column (sentiment)
* 2d: Use fillna to propagate non-NULL values forward for rows with one missing value.
* 2e: Asjust the data types of the relevant columns
* 2f: Write adjusted dataframe to a csv file in working directory.

Step 3: Initial Tables and Plots
* 3a: Draw a table showing status count by country.
* 3b: Use Matplotlib to plot a pie chart showing sentiment count distribution (positive, negative or neutral). Read documentation here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
* 3c: Use Matplotlib to draw Histogram, showing Distribution of Friends and Status Count Relationship. Read documentation here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist2d.html

Step 4: Correlation
* 4a: Calculate the correlation between number of friends and status count
* 4b: Calculate the correlation between number of friends and sentiment
* 4c: Calculate the correlation between status count and sentiment


# Model Building
Step 1:  Prepare the dataset for modelling
* 1a: Read in the combined dataset
* 1b: Inspect the dataset
* 1c: Drop duplicate and irrelevant columns in dataframe

Step 2:
* 2a: Set the train_test_split for the dataset at 0.3 (test) and 0.7 (train).
* 2b: Set the label and save path.

Step 3:
* 3: Use Autogluon Tabular Predictor to build model and evaluate features. See documentation : https://auto.gluon.ai/dev/tutorials/tabular/tabular-quick-start.html



