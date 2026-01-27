import re

import urllib.request

URL = "https://www.yvbeach.com/yvmeteo.htm"

def fetch_temperature(url: str) -> str | None:
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None

    # Look for a pattern like "25°C" or "25 °C"
    match = re.search(r'(\d+)\s*°C', html)
    if match:
        return match.group(1) + "°C"

    # Fallback: look for "Temp: 25°C" or "Température: 25°C"
    match = re.search(r'TEMPERATURE :?[:\s]*([0-9]+)\s*°C', html, re.IGNORECASE)
    if match:
        return match.group(1) + "°C"

    return None

def main() -> None:
    temp = fetch_temperature(URL)
    if temp:
        print(f"Température actuelle : {temp}")
    else:
        print("Température non trouvée.")

if __name__ == "__main__":
    main()