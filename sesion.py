from msilib.schema import File
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

def create_driver_session(session_id, executor_url):
    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)
    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute
    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id
    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute
    return new_driver

File='./resource/session.log'

def newSession():
    global driver
    driver = webdriver.Edge(executable_path='./msedgedriver.exe')
    executor_url = driver.command_executor._url
    session_id = driver.session_id
    driver.get("https://web.whatsapp.com/")
    with open(File,'w') as f:
        f.write(session_id+','+executor_url)
        f.close()

def openSession(id,url):
    return create_driver_session(id,url)

#newSession()