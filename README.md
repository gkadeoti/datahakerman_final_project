
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
a) What index corresponds to the house “House Breakstone”?
 
b) How many males, females and unknown genders are there in the first 40 characters? Note, index 0 does not correspond to a character, so full range is 1 - 40 both ends inclusive. 
​
c) How many books can be accessed from this API?
​
d) How many books does the character ‘High Septon’ appear in? (ignoring ‘povcharacters’) 
​
Hint: index value of Septon needs to be found first; it is smaller than 20.
​
# File type manipulation and formatting
​
Three files are presented, one CSV, one TXT and one JSON file. Each contain 1000 rows of data. There are two challenges, both involving collating these files into one data frame. The fields in all files are:
​
'author.properties.friends',  'author.properties.status_count',  'author.properties.verified',  'content.body',  'location.country',  'properties.platform',  'properties.sentiment',  'location.latitude',  'location.longitude'
​
where the ‘.’ Indicates a nested field.
 
a) Begin by collating the CSV and TXT files together into one pandas dataframe. The resulting dataframe should be 2000 rows and have all of the columns present in both files.
​
b) Next, using the created dataframe, integrate the data from the JSON file into the existing columns. The resulting dataframe should now be 3000 rows long.
​
# Data Exploration
​
In this challenge we would like to know something interesting about the data. You are free to explore as you wish, producing plots, tables, statistics, etc. Feel free to use any variables in the dataset or include external data you may consider relevant to complement your analysis.  
​
# Model Creation
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
1. A Public API on Game of Thrones
The API provides information on Game of Thrones, allowing one to access information on the houses, characters and books.
* API URL: http://anapioficeandfire.com/api/{SECTION}/{INDEX}
Where SECTION can be either 'books', 'characters', or 'houses' and INDEX is an integer to a certain entry in a section.
2. Data on Love Island Sentiment Analysis, as found in the "data" folder. Data is comprised of 3 files: csv_file.csv, json_file.json, txt_file.txt

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

```

# Project Structure
- API Data Call
- DataFrame Merging
- Data Exploration
- Model Building


# Repository Structure
- inputs/data
- models
- outputs
- .gitignore
- README.md
- TS01_API_Access_.ipynb
- TS02_Dataframe_Merging.ipynb
- TS03_Data_Exploration.ipynb
- TS04_Model_Building.ipynb
- environment.yml
- requirements.txt

# API Data Call

Step 1
Confirm acess to the API root url

```

got_url = "https://anapioficeandfire.com/api/"
got_response = requests.get(got_url)

```

If got_response = 200, then access is confirmed.

```
Step 2
For question a, read in the Houses URL and specify parameters

```
got_houses_url="https://anapioficeandfire.com/api/houses"
query_params = {"name": "House Breakstone",}

```
For question b, read in the Houses URL and specify parameters




# Data Exploration

Step 1: Preambles
1a: Import the required packages for data exploration: matplotlib, folium, scikit-learn
1b: Confirm working directory
1c: Read in merged data

Step 2: Data Inspection
2a: Inspect the merged dataframe
2b: To check and identify null values
2c: Drop rows with null values in the predicted/outcome column (sentiment)
2d: Use fillna to propagate non-NULL values forward for rows with one missing value.
2e: To format the data type

```
love_island_data = pd.read_csv('outputs/all_merged_data.csv')
```

Step 3: 
3a: Data Inspection
```
love_island_data.info()

```
3b: Deal with null values

```
love_island_data = love_island_data.dropna(axis = 0)
```
3c: Adjust data types
```
love_island_data['author.properties.friends'] = love_island_data['author.properties.friends'].astype(int)
```

# Model Building
Step 1:  Prepare the dataset for modelling

```
1a Read in the combined dataset

```
love_island_data = pd.read_csv('outputs/love_island_data.csv')

```

1b Inspect the dataset

```

love_island_data.info()
love_island_data.shape

```

1c Drop duplicate and irrelevant columns in dataframe

```
del love_island_data ['COLUMN+NAME']

Step 2:
2a: Set the train_test_split for the dataset at 0.3 (test) and 0.7 (train).
2b: Set the label and save path.

Step 3:
3 Use Autogluon Tabular Predictor to build model and evaluate features. See documentation : https://auto.gluon.ai/dev/tutorials/tabular/tabular-quick-start.html









