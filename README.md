# Airline Digital Analytics

A hands-on project exploring digital analytics for a simulated airline booking website. The project demonstrates website event tracking, marketing campaign performance analysis, and consent-based event collection using JavaScript, Google Tag Manager, and Python.

## Project Overview

Digital analytics helps organisations understand how users interact with digital platforms, evaluate marketing performance, and collect data responsibly.

This project uses a fictional airline booking journey to demonstrate three practical areas:

1. **Website Event Tracking:** Capturing user interactions such as flight searches through a JavaScript data layer and Google Tag Manager.
2. **Campaign Performance Analysis:** Evaluating simulated marketing campaigns using Python and key performance indicators.
3. **Consent-Based Data Collection:** Simulating how analytics events can be filtered according to user consent preferences.

All website interactions and campaign data are simulated for educational purposes. No real customer data is used.

## Features

### 1. Website Event Tracking

A simple airline booking page allows users to enter flight details and search for flights.

The website pushes structured event data to the JavaScript `dataLayer`, including:

- Event name: `flight_search`
- Flight origin
- Flight destination
- Passenger count
- Trip type

Google Tag Manager is used to configure a custom event trigger and data layer variables for these parameters.

### 2. Marketing Campaign Analysis

A Python script analyses synthetic campaign data from three marketing channels:

- Google Search
- Instagram Ads
- Email Marketing

The following metrics are calculated:

| Metric | Calculation |
|---|---|
| Click-Through Rate (CTR) | Clicks / Impressions × 100 |
| Conversion Rate | Bookings / Clicks × 100 |
| Cost per Acquisition (CPA) | Advertising Spend / Bookings |
| Return on Ad Spend (ROAS) | Revenue / Advertising Spend |

The script compares campaign performance and identifies the strongest channel for each metric.

### 3. Consent-Based Event Collection

A Python simulation demonstrates purpose-based event filtering using three consent categories:

- **Essential:** Events required for basic website functionality.
- **Analytics:** Events used to understand website interactions.
- **Marketing:** Events used for marketing-related purposes.

The simulation tests different combinations of consent preferences and shows which events are permitted or blocked.

This is an educational demonstration of consent-aware data collection, not a complete GDPR-compliant consent management platform.

## Technology Stack

- **Languages:** Python, JavaScript, HTML, CSS
- **Analytics & Tracking:** Google Tag Manager, JavaScript Data Layer
- **Data Analysis:** Pandas
- **Development Tools:** Visual Studio Code, Git, GitHub

## Project Structure

```text
Digital_Analytics/
├── website/
│   └── airline.html
├── campaign_analysis.py
├── consent_simulation.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3
- Git
- A modern web browser

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Digital_Analytics
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the campaign analysis

```bash
python campaign_analysis.py
```

### 5. Run the consent simulation

```bash
python consent_simulation.py
```

### 6. Open the airline demo website

From the project directory, start a local web server:

```bash
cd website
python3 -m http.server 8000
```

Open the following address in your browser:

```text
http://localhost:8000/airline.html
```

Keep the terminal running while using the website. The Google Tag Manager container configured for the demo can be previewed using the relevant container setup.

## Key Learning Outcomes

Through this project, I explored:

- Structuring and capturing website interaction events.
- Understanding JavaScript data layers and Google Tag Manager fundamentals.
- Analysing digital marketing campaign performance.
- Calculating and interpreting common marketing KPIs.
- Applying basic consent-based event filtering.
- Using Python and Pandas for practical analytics workflows.

## Disclaimer

This project is intended for learning and demonstration purposes. Campaign figures are synthetic, the airline website is a demo, and the consent simulation does not replace a production consent management solution or legal GDPR assessment.