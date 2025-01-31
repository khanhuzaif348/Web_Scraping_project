# Web Scraping Laptops Data 🖥️💻  

This project uses **Python**, **BeautifulSoup**, and **Pandas** to scrape laptop product details from [Web Scraper's test site](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops). It extracts product names, prices, and ratings, then stores the data in a structured CSV file.  

## Features ✨  
✔ Scrapes product details from the webpage  
✔ Extracts **Names**, **Prices**, and **Ratings**  
✔ Saves the data into a CSV file for further analysis  
✔ Uses **requests** for fetching web pages and **BeautifulSoup** for parsing  

## Requirements 📌  
Ensure you have the following Python libraries installed:  
```bash
pip install requests beautifulsoup4 pandas lxml
```

## Usage 🚀  
Run the script to scrape the latest laptop details:  
```bash
python scrape_laptops.py
```
The extracted data will be saved in `product_details.csv`.  

## Future Improvements 🚀  
- Add support for scraping multiple pages  
- Extract additional product details (e.g., specifications, availability)  
- Automate data updates  

📌 Feel free to contribute or fork the project! 😊  


