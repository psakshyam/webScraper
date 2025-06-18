import streamlit as st

st.title("Web Scraper")
url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
    if url:
        st.write(f"Scraping data from: {url}")
        # Here you would add the logic to scrape the URL
        # For example, using requests and BeautifulSoup
    else:
        st.error("Please enter a valid URL.")