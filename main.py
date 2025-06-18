import streamlit as st
from scrape import scrape_website, split_text, clean_body, extract_data

st.title("Web Scraper")
url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
    if url:
        st.write(f"Scraping data from: {url}")
        # Here you would add the logic to scrape the URL
        # For example, using requests and BeautifulSoup
        result = scrape_website(url)

        body_content = extract_data(result)
        cleaned_content = clean_body(body_content)

        st.session_state.cleaned_content = cleaned_content

        with st.expander("View Cleaned Content"):
            st.text_area("Cleaned Content", cleaned_content, height=300)
        
        text_chunks = split_text(cleaned_content)
    else:
        st.error("Please enter a valid URL.")

