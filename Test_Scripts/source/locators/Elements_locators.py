from selenium.webdriver.common.by import By

class ElementsPageLocators:

    PagesCardsName = (By.CSS_SELECTOR, '.card-body')
    TextBoxButton = (By.CSS_SELECTOR, 'li#item-0')
    CheckBoxButton = (By.CSS_SELECTOR, 'li#item-1')
    RadioButtonButton = (By.CSS_SELECTOR, 'li#item-2')

    FullNameField = (By.CSS_SELECTOR, '#userName')
    EmailField = (By.CSS_SELECTOR, '#userEmail')
    CurrentAddressField = (By.CSS_SELECTOR, '#currentAddress')
    PermanentAddressField = (By.CSS_SELECTOR, '#permanentAddress')
    SubmitButton = (By.CSS_SELECTOR, '#submit')

    CollapseAllButton = (By.CSS_SELECTOR, 'button.rct-collapse.rct-collapse-btn')
    Checkboxes = (By.CSS_SELECTOR, ".rct-checkbox")
    CheckboxResultMessage = (By.CSS_SELECTOR, "#result")

    YesRadio = (By.CSS_SELECTOR, 'input[type="radio"][id="yes"]')
    ImpressiveRadio = (By.CSS_SELECTOR, 'input[type="radio"][id="impressive"]')
    NoRadio = (By.CSS_SELECTOR, 'input[id="noRadio"]')
    RadioLabelYes = (By.CSS_SELECTOR, "label[for='yesRadio']")
    RadioLabelImpressive = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    RadioLabelNo = (By.CSS_SELECTOR, "label[for='noRadio']")
    RadioBoxResultMessage = (By.CSS_SELECTOR, '.mt-3')

    AddBtnWeb = (By.CSS_SELECTOR, '#addNewRecordButton')
    FNameFieldWeb = (By.CSS_SELECTOR,'#firstName')
    LNameFieldWeb = (By.CSS_SELECTOR,'#lastName')
    EmailFieldWeb = (By.CSS_SELECTOR,'#userEmail')
    AgeFieldWeb = (By.CSS_SELECTOR,'#age')
    SalaryFieldWeb = (By.CSS_SELECTOR,'#salary')
    DepartmentFieldWeb = (By.CSS_SELECTOR,'#department')
    SubmitBtnWeb = (By.CSS_SELECTOR, '#submit')
    EditBtnFirstUser = (By.CSS_SELECTOR, '#edit-record-1')
    SalaryAmountInTableFirstUser = (By.CSS_SELECTOR, 'div.rt-tbody > div.rt-tr-group:nth-child(1) > div.rt-tr > div.rt-td:nth-child(5)')
    DeleteSecondUser = (By.CSS_SELECTOR, '#delete-record-2')



