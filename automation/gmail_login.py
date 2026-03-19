from appium import webdriver
import time

# Set up desired capabilities for Appium
desired_caps = {
    'platformName': 'Android',
    'platformVersion': 'YOUR_ANDROID_VERSION',
    'deviceName': 'YOUR_DEVICE_NAME',
    'appPackage': 'com.google.android.gms',
    'appActivity': 'com.google.android.gms.auth.api.signin.internal.SignInHubActivity',
    'noReset': True,
    'fullReset': False,
}

# Start Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the app to load
time.sleep(10)

# Function to handle login
def login_to_gmail(email, password):
    # Enter email
    email_field = driver.find_element_by_id('identifierId')
    email_field.send_keys(email)
    driver.find_element_by_id('identifierNext').click()
    time.sleep(2)  # Wait for next page to load

    # Enter password
    password_field = driver.find_element_by_name('password')
    password_field.send_keys(password)
    driver.find_element_by_id('passwordNext').click()

    # Handle 2FA if prompted
    time.sleep(5)  # Wait for possible 2FA page
    try:
        two_fa_field = driver.find_element_by_name('idvPin')
        if two_fa_field:
            two_fa_field.send_keys('YOUR_2FA_CODE')  # Replace with actual 2FA code or method to retrieve it
            driver.find_element_by_id('idvNext').click()
            time.sleep(5)  # Wait for login completion
    except:
        print('No 2FA required or failed to find the 2FA input field')

    # Accept ToS if prompted
    try:
        tos_accept_button = driver.find_element_by_id('accept_button_id')  # Use the actual ID
        tos_accept_button.click()
        time.sleep(2)
    except:
        print('No ToS acceptance required')

# Usage:
login_to_gmail('YOUR_EMAIL@gmail.com', 'YOUR_PASSWORD')

# Quit the driver after the task
# driver.quit()  # Uncomment this to quit the driver at the end of the script