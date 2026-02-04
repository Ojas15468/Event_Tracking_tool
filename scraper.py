import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def scrape_bookmyshow(city="mumbai"):
    """
    Scrapes event data from BookMyShow using Selenium.
    Uses robust XPATH selectors targeting 'data-content' attributes.
    """
    print(f"🕵️‍♂️  Starting extraction for {city}...")
    
    # --- BROWSER SETUP ---
    options = Options()
    options.add_argument("--headless")  # Runs in background (no popup window)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Fake a real user to avoid being blocked
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    events_list = []
    
    try:
        url = f"https://in.bookmyshow.com/explore/events-{city}"
        driver.get(url)
        time.sleep(3) 

        # Scroll down to trigger lazy loading
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)

        # --- EXTRACTION STRATEGY ---
        # 1. Find all event cards by looking for links containing '/events/'
        event_cards = driver.find_elements(By.XPATH, "//a[contains(@href, '/events/')]")
        
        print(f"🔎  Found {len(event_cards)} raw cards. Processing...")

        for card in event_cards:
            try:
                # 2. Extract Link
                link = card.get_attribute("href")
                
                # 3. Extract Name using the 'data-content' attribute (Robust)
                try:
                    # Look inside the card (.//) for the specific div you found
                    name_element = card.find_element(By.XPATH, ".//div[@data-content]")
                    name = name_element.get_attribute("data-content")
                except:
                    # Fallback mechanism
                    lines = card.text.split('\n')
                    name = lines[0] if lines else "Unknown Event"

                # 4. Extract Category (usually the second line of text)
                text_parts = card.text.split('\n')
                category = text_parts[1] if len(text_parts) > 1 else "General"

                # 5. Build the Data Object
                event_obj = {
                    "Event Name": name,
                    "City": city.capitalize(),
                    "Category": category,
                    "Date Found": datetime.now().strftime("%Y-%m-%d"),
                    "URL": link,
                    "Status": "Active"
                }
                
                # Simple in-memory deduplication
                if event_obj not in events_list:
                    events_list.append(event_obj)
                    
            except Exception as e:
                # If a card is malformed, skip it and continue
                continue

    except Exception as e:
        print(f"❌ Critical Error: {e}")
    finally:
        driver.quit()
        
    print(f"✅  Scraping complete. Found {len(events_list)} valid events.")
    return events_list