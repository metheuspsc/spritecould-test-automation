# SpriteCloud Test Automation Challenge

> This is a automated test project for spriteCloud QA Engineer position challenge. \
> Using Python, pytest,requests, selenium and Github Actions. 

## ✅ Challenge Requirements.
UI to test: : https://demoqa.com/ \
API to test: : https://petstore.swagger.io

Requirements:
- [ ] List at least 3 important automation scenarios for both the UI and the API
- [ ] Automate the scenarios.
- [X] Set up tests on CI/CD Environment.(Github Actions)
- [x] Upload to Github.
- [x] Results report inside results folder.
- [x] Upload test results to Calliope.pro.
- [ ] Readme Details.

## ✨ Assumptions

- Some of the api tests may fail due to the processing time of the api, since I'm hitting the endpoint as a user. For example: test_update_pet assertion may fail due to the time it takes for the api to internally update the pet.



## 💻 Get Started

Before starting you need the following dependencies:
* Install `Python 3` latest version 

## 🚀 Local Setup

Windows:

```
mkdir <project path>
cd <project path>
git clone https://github.com/metheuspsc/ca-test-automation.git
python -m venv venv
./venv/scripts/activate
pip install -r requirements.txt
pytest
```

## 👷 CI/CD Setup

I used Github Actions as the CI/CD platform, the tests are called on push and pull requests to the master branch.

## 📝 Calliope Pro Results
