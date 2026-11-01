from bs4 import BeautifulSoup
import requests
import json

url = "https://analyst-assessment-production.up.railway.app"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("Successfully fetched website! Extracting communities...")
    
    locations = []
    
    # Look for all headings or divs that usually hold facility names
    for h in soup.find_all(['h2', 'h3', 'h4', 'a', 'div']):
        text = h.get_text(strip=True)
        # Check if it looks like a community name
        if text and "Bellhaven" in text and len(text) < 60:
            if text not in locations:
                locations.append(text)

    print(f"\nTotal unique locations found: {len(locations)}")
    for i, loc in enumerate(locations, 1):
        print(f"{i}. {loc}")
        
    # Save to JSON file for the next step
    with open("scraped_locations.json", "w") as f:
        json.dump(locations, f, indent=4)
    print("\nSaved locations to scraped_locations.json successfully!")
else:
    print(f"Failed to fetch website: {response.status_code}")