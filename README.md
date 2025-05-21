```bash
# 🧪 DemoQA Test Automation Suite

This repository contains end-to-end UI automation test cases for the https://demoqa.com/ website.  
Built using **Python**, **Selenium WebDriver**, and **Pytest**, it follows modern testing best practices.

────────────────────────────────────────────────────────────

📁 Project Structure

DemoQA_AutomatedTesting/
│
├── Test_Scripts/
│   ├── Tests/                       # Test cases grouped by feature
│   └── source/
|   |   ├── helpers/
|   |   ├── locators/
│   |   ├── pages/                  # Page Object Model (POM)
│   |   └── selenium_extended.py   # Custom Selenium functions
│   ├─── conftest.py                    # Pytest fixtures (e.g., WebDriver initialization)
|
├── requirements.txt               # Python dependencies
├── pytest.ini                     # Pytest markers and configs
└── README.md                      # You're reading it!

────────────────────────────────────────────────────────────

🚀 Getting Started

# 1. Clone the repository
git clone [https://github.com/yourusername/DemoQA-Tests.git](https://github.com/NicoletaAnghel/DemoQA_AutomatedTesting)
cd DemoQA_AutomatedTesting

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # On macOS/Linux
.venv\Scripts\activate           # On Windows

# 3. Install dependencies
pip install -r requirements.txt

────────────────────────────────────────────────────────────

🧪 Run Tests

# Run all tests
pytest

# Run a specific test file
ex. = pytest Test_Scripts/Tests/test_elements_checkbox.py

# Run tests by marker (see pytest.ini)
ex. = pytest -m radiobtn1

Available markers:
- elementcheckboxespositive      #for all Checkbox Positive Tests
  - checkbox1
  - checkbox2
  - checkbox3
  - checkbox4
  - checkbox5
  - checkbox6
- elementsradiobtnpositive      # for all RadioBtn Posivite Tests
  - radiobtn1
  - radiobtn2
  - radiobtn3
  - radiobtn4
-elementstextpositive          # for all TextBox Posivite Tests
  - textbox1
  - textbox2
  - textbox3
-elementstextnegative           # for all TextBox Negative Tests
  - textbox_negative1
  - textbox_negative2
  - textbox_negative3
  - textbox_negative4
- webtablespositive

## The List will be updated after more tests are scripted

────────────────────────────────────────────────────────────

🌐 Run on Different Browsers

# Set browser in environment variable
# Options: chrome, firefox, edge

set BROWSER=firefox              # On Windows

────────────────────────────────────────────────────────────

🧱 Highlights

✅ Pure CSS selectors  
✅ Modular Page Object Model  
✅ Custom Selenium extensions (selenium_extended.py)  
✅ Utility functions (random data generators)  
✅ Markers for logical grouping  
✅ Fixtures managed in `conftest.py`  
✅ Easy browser switching for cross-browser testing

────────────────────────────────────────────────────────────

🐞 Known Issues

- Certain elements (e.g., "No" in Radio Button) are disabled by site design.
- UI updates on demoqa.com may require locator adjustments.

────────────────────────────────────────────────────────────

👨‍💻 Author

Nicoleta Anghel  
QA Software Tester  
🔗 [https://github.com/NicoletaAnghel ](https://github.com/NicoletaAnghel)
🔗 [https://linkedin.com/in/yourlinkedin](https://www.linkedin.com/in/nicoleta-anghel-73227a17a/)

────────────────────────────────────────────────────────────

