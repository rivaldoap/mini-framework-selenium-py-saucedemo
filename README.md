# 🚀 Scalable Test Automation Framework

A simple test automation framework designed using industry standards to minimize hardcoding and increase script maintenance efficiency.

This framework is built on the knowledge and best practices I learned from bootcamp, then further developed to simulate real-world work requirements.

## ✨ Key Features
* Minimal Hardcode: Data structures and elements are well separated for easy configuration.
* Negative Test Handling: Detects system anomalies and ensures errors are caught according to the expected result.
* Robust Framework Architecture: Not just a regular linear script, but a scalable structure.

## 🛠️ Technologies Used
* **Language:** Py
* **Automation Tools:** Selenium WebDriver
* **Test Runner:** PyTest
* **Design Pattern:** Page Object Model (POM)

## 📌 Roadmap & Future Improvements (Future Homework)
This framework is still under active development (*work in progress*). Future improvement targets:
- [ ] Integration of the **Automatic Screenshot** function
- [ ] Creation of more interactive automation reports
- [ ] Optimization of *state* management and *wait handling*.

## 🏃‍♂️ How to Run a Project
1. Clone this repository.
2. If using a Virtual Environment, activate it first. If using CMD, use ".Venv\Scripts\activate.bat"; if using PowerShell, use ".Venv\Scripts\Activate.ps1"
3. Select the Excel file to be tested, then in column "A," type "RUN" for the scenario to be run.
4. Run the test with the command "pytest TestCase/Folder/file_name::function_name -v -s"
