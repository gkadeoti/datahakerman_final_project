
# Introduction
  Data Hackerman Final Project

# Data Sources
Two datasources are used in this project:
1. A Public API on Game of Thrones
The API provides information on Game of Thrones, allowing one to access information on the houses, characters and books.
* API URL: http://anapioficeandfire.com/api/{SECTION}/{INDEX}
Where SECTION can be either 'books', 'characters', or 'houses' and INDEX is an integer to a certain entry in a section.
2. Data on 

### Data Set Information:


### Attribute Information:

# Environment Setup
Available initial enviroment setup files.

```bash
environment.yml
```

```bash
conda env create -f environment.yml
conda activate hackermanproject_env

```
Step 1: Create repository on github

```
"github.com/your_username/datahackerman_final_project"

```

Step 2: Clone repository in preferred directory location on local computer  
```
git clone https://github.com/gkadeoti/datahakerman_final_project.git

```

Step 3: Create environment using `environment.yml` file

```
conda env create -f environment.yml

```
# API Data Call
Step 


# Data Exploration

Step 1: Install additional packages for exploration: matplotlib, folium

```
pip install matplotlib -q
pip install folium
```

Step 2: Read in merged data

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
Step 1: Install additional packages for model building: scikit-learn, autogluon, streamlit

```
pip install torch==1.13.1 torchvision==0.14.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install autogluon streamlit
pip install -U scikit-learn

```
- - -
### Note: this is for Mac devices, for Windows users, check the package documentation

### Test your installation as follows:

(hackermanproject_env) macbook@Gbemilekes-MBP datahakerman_final_project % python
Python 3.9.16 | packaged by conda-forge | (main, Feb  1 2023, 21:42:20) 
[Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from autogluon.tabular import TabularDataset, TabularPredictor
```

If that works, you have good installation for `autogluon`.

And then for `Streamlit`

```bash

(tescochurn) macbook@Gbemilekes-MBP tesco_customer_churn % streamlit hello
  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.227:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!

This will automatically pop up on your default browser on this address: http://localhost:8501/









