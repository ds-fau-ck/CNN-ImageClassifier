from setuptools import setup 

with open("README.md","r", encoding="utif-8") as f:
    long_discriptions=f.read()

REPO_NAME="mlflow-project-template"
AUTHOR_USER_NAME="TUCchkul"
SRC_REPO="src"
LIST_OF_REQUIREMENTS=[]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Kulakirti Chakma",
    descriptions="A small project for mlflow",
    long_discriptions=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTOR_USER_NAME}/{REPO_NAME}",
    autor_email="kirticse.chakma869@gmail.com",
    package=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS

)