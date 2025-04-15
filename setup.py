from setuptools import setup, find_packages

setup(
    name="fulltext-search",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click==8.1.8",
        "exceptiongroup==1.2.2",
        "iniconfig==2.1.0",
        "joblib==1.4.2",
        "nltk==3.9.1",
        "packaging==24.2",
        "pluggy==1.5.0",
        "pytest==8.3.5",
        "regex==2024.11.6",
        "tomli==2.2.1",
        "tqdm==4.67.1"
    ]
)