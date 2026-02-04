from scraper import scrape_bookmyshow
from sheet_manager import update_google_sheet

# Configuration
TARGET_CITY = "mumbai"
SHEET_NAME = "Event Tracker"

def job():
    print("🚀  Starting Event Discovery Job...")
    print("--------------------------------")
    
    # Step 1: Scrape Data
    events = scrape_bookmyshow(TARGET_CITY)
    
    if events:
        # Step 2: Update Database (if data found)
        update_google_sheet(events, SHEET_NAME)
    else:
        print("⚠️  No data scraped. Skipping DB update.")
        
    print("--------------------------------")
    print("🏁  Job Finished.")

if __name__ == "__main__":
    job()