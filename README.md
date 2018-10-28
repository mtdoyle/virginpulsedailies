This script automates the completion of daily cards / healthy habits in Virgin Pulse

Requirements:
    
    1. Chrome browser
    2. Chromedriver: http://chromedriver.chromium.org/
    3. Selenium library
    
How to run:
    
    1. Add the following envionment variables:
        *  USERNAME - your virgin pulse username.
        *  PASSWORD - your virgin pulse password.
        *  CHROMEDRIVER - path to your chromedriver binary. Can be skipped if it's on the system path.
    2. Run the script
    
    
    
This script will probably fail in it's current state. The cards change often and so far I've only captured the simple 
"GOT IT!" card and a True/False card. There are pop-ups that occur often that I haven't accounted for which will likely
cause this script to fail until they are accounted for.
