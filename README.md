# Telco Phone Number Monitor 🤖

A simple Python script that automatically refreshes a telco webpage and monitors available phone numbers for a desired number.

Built with **Python** and **Selenium**.

## Features

* Automatically refreshes the webpage
* Expands the available number list using **"See more"**
* Searches for a specified phone number or number ending
* Stops refreshing when a matching number is found
* Keeps the browser open so the user can proceed with the purchase manually

## Requirements

* Python 3
* Google Chrome
* Selenium

Install Selenium with:

```bash
pip install selenium
```

## Usage

Set the webpage URL and desired number in the script:

```python
url = "https://www.gomo.sg/plan-detail/98"
search_strings = ["1747"]
```

Then run:

```bash
python telco_number_monitor.py
```

The script will refresh the page every second until a matching number is found.

Once the desired number is detected, the script stops refreshing and keeps the browser open.

## Disclaimer

For personal use and monitoring of publicly displayed phone number availability. The script does not automatically purchase or reserve a number.
