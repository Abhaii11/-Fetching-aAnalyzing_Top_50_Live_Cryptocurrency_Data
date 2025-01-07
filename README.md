# -Fetching-aAnalyzing_Top_50_Live_Cryptocurrency_Data

# Cryptocurrency Live Data Fetching and Analysis

This repository contains a Python script that fetches live cryptocurrency data for the top 50 cryptocurrencies by market capitalization, performs basic analysis, and updates an Excel sheet with the latest data every 5 minutes. The project aims to provide continuous monitoring and insights into cryptocurrency trends.

## Features

1. **Fetch Live Cryptocurrency Data**
   - Data is fetched from the [CoinGecko API](https://www.coingecko.com/en/api).
   - Fields include:
     - Cryptocurrency Name
     - Symbol
     - Current Price (in USD)
     - Market Capitalization
     - 24-hour Trading Volume
     - 24-hour Percentage Price Change

2. **Data Analysis**
   - Identifies the top 5 cryptocurrencies by market capitalization.
   - Calculates the average price of the top 50 cryptocurrencies.
   - Determines the highest and lowest 24-hour percentage price changes.

3. **Live Updating Excel Sheet**
   - Updates data every 5 minutes.
   - Includes detailed information and analysis sections.

4. **Cloud Sharing**
   - The Excel file can be uploaded to Google Drive, OneDrive, or SharePoint for sharing and collaboration.

## Requirements

### Python Packages
- `requests`: For fetching data from the CoinGecko API.
- `openpyxl`: For creating and updating Excel files.
- `time`: For scheduling periodic updates.
- `pandas`: For data processing (optional, if additional analysis is needed).

### Installation
Install the required Python packages using the following command:
```bash
pip install requests openpyxl pandas
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/Abhaii11/crypto-live-data.git
   cd crypto-live-data
   ```

2. Run the script:
   ```bash
   python crypto_live_update.py
   ```

3. The script will generate an `crypto_data.xlsx` file in the project directory and update it every 5 minutes.

## Output

- **Excel Sheet**: Contains the top 50 cryptocurrencies' data and analysis, updated every 5 minutes.
- **Analysis Sections**:
  - Top 5 cryptocurrencies by market capitalization.
  - Average price of the top 50 cryptocurrencies.
  - Highest and lowest 24-hour percentage price changes.

## Deployment
To ensure the script runs continuously:

1. **Local Deployment**:
   - Keep the script running in the background. Use a terminal multiplexer like `tmux` or `screen` to avoid interruptions.

2. **Cloud Deployment**:
   - Deploy the script on platforms like AWS Lambda, Google Cloud Functions, or Azure.
   - Schedule periodic execution using tools like AWS EventBridge or `cron` on a virtual machine.

3. **Google Sheets Integration** (Optional):
   - Modify the script to write data directly to Google Sheets using the Google Sheets API.

## API Reference

- [CoinGecko API Documentation](https://www.coingecko.com/en/api)

## Contributions

Contributions are welcome! If you encounter a bug or have a feature request, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, feel free to contact:
- **Name**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [your-username](https://github.com/your-username)
