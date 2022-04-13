# mlflow-project-template
MLflow project template

## Steps -
### STEP 01 Create a repository by using template repository
### STEP 02 clone the repository
### STEP 03 create a conda environment after opening the repository in VSCODE
```bash
conda create --prefix ./env python=3.7 -y && conda activate ./env
```
OR
```bash
conda activate ./env
```
### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 05 create conda.yaml file
```bash
conda env export > conda.yaml
```
### STEP 06 commit and push the changes to the remote repository