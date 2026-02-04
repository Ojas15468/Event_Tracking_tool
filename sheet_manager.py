import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define the scope for Google APIs
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

def connect_to_drive():
    """Connects to Google Drive using the credentials.json file."""
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPE)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        print(f"❌ Auth Error: Could not load credentials.json. Details: {e}")
        return None

def update_google_sheet(new_data, sheet_name="Event Tracker"):
    """
    Updates the Google Sheet with new data.
    Performs deduplication based on the 'URL' column.
    """
    client = connect_to_drive()
    if not client: 
        return

    try:
        # Open the specific Google Sheet
        try:
            sheet = client.open(sheet_name).sheet1
        except gspread.SpreadsheetNotFound:
            print(f"❌ Error: Sheet '{sheet_name}' not found. Please share the sheet with the service email.")
            return

        # 1. Fetch Existing Data
        existing_records = sheet.get_all_records()
        existing_df = pd.DataFrame(existing_records)

        # 2. Prepare New Data
        new_df = pd.DataFrame(new_data)
        
        if existing_df.empty:
            # If sheet is empty, use new data as is
            final_df = new_df
            print("📝  Sheet is empty. Adding all scraped events.")
        else:
            # 3. Deduplication (The Logic)
            # Filter out rows from new_df where the 'URL' is already in existing_df
            if "URL" in existing_df.columns:
                existing_urls = existing_df["URL"].tolist()
                unique_new_events = new_df[~new_df["URL"].isin(existing_urls)]
            else:
                # If 'URL' column is missing in sheet, assume all are new
                unique_new_events = new_df

            if unique_new_events.empty:
                print("⚠️  No new events found. Sheet is up to date.")
                return
            
            print(f"⚡  Adding {len(unique_new_events)} new unique events...")
            # Append unique new events to the existing dataframe
            final_df = pd.concat([existing_df, unique_new_events], ignore_index=True)

        # 4. Write Back to Sheet
        # Clearing and rewriting is the safest way to ensure data consistency
        sheet.clear()
        # Write headers
        sheet.append_row(final_df.columns.tolist())
        # Write data rows
        sheet.append_rows(final_df.values.tolist())
        print("✅  Google Sheet Updated Successfully!")

    except Exception as e:
        print(f"❌ Sheet Error: {e}")