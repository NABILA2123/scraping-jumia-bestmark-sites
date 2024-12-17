# Jumia and Bestmark Scraping Project

## What Is The Project About?
This project allows for scraping product data from **Jumia** and **Bestmark** websites. The scraper collects information such as product names, prices, ratings, and links to individual product pages. This data can be used for analysis, price comparison, or market research purposes.
![image](https://github.com/user-attachments/assets/704a2d54-a4ff-4f27-9b92-ed2160c60430)

**Note:** Make sure to comply with the Terms of Service of both websites and local laws regarding web scraping. This project is intended for educational purposes.

## Features

- Scrape product details from Jumia and Bestmark.
- Extract product name, price, ratings, and product URLs.
- Handle pagination to gather multiple pages of product listings.
- Save the scraped data in CSV/JSON format for further analysis.
![image](https://github.com/user-attachments/assets/217874a5-51a1-4531-a826-397063d65f36)

## How To Run The Project?

1. **Clone the repository**:
git clone https://github.com/yourusername/jumia-bestmark-scraper.git
cd jumia-bestmark-scraper
2. **Install the dependencies**:
Create a virtual environment (optional but recommended) and install the necessary packages:
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
Or you can manually install dependencies:
pip install requests beautifulsoup4 pandas lxml selenium
3. **Download the Web Driver (for Selenium)**:
Chrome: Download ChromeDriver
Firefox: Download GeckoDriver
Ensure the driver is in your PATH or specify its location in the script.
