
# Introduction
  Data Hackerman Final Project

# Data Sources
Public API on Game of Thrones
The API provides information on Game of Thrones, allowing one to access information on the houses, characters and books.
* API URL: http://anapioficeandfire.com/api/{SECTION}/{INDEX}
Where SECTION can be either 'books', 'characters', or 'houses' and INDEX is an integer to a certain entry in a section.

### Data Set Information:


### Attribute Information:

# Environment Setup

Step 1: Create repository on github

```
"github.com/your_username/datahackerman_final_project"

```

Step 2: Clone repository in preferred directory location on local computer  
```
git clone https://github.com/gkadeoti/datahakerman_final_project.git
```
Step 3: Create `environment.yml` file with relevant dependencies (see `environment.yml` file for full list of dependencies)

```
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - numpy
  - pandas
  - pip
  - pip:
    - torch==1.12.1
    - torchvision==0.13.1
    - torchtext==0.13.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
    - autogluon
    - streamlit
    - jupyter
```

Step 4: Create environment using `environment.yml` file

```
conda env create -f environment.yml

```
