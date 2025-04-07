# Bike Forecast Automation 🚴‍♂️📊

**Project:** Automated Forecast System for a Bike Manufacturing Company  
**Purpose:** This system automates forecasting and reporting for senior management.  
**Technologies:** Python, Conda, Pandas, sktime, Papermill  

## 📌 Features

- Automates time series forecasting for bike production.
- Generates reports for senior management.
- Uses sktime for advanced forecasting models.
- Leverages Papermill for running Jupyter notebooks as automated scripts.

## ⚙️ Installation

### Step 1: Clone the Repository

```sh
git clone https://github.com/Rhodapeps/bike-forecast-automation.git
cd bike-forecast-automation
```

## Step 2: Set Up Conda Environment

```sh
conda env create -f 000_environment_setup/01_conda_environment.yml
conda activate bike_forecast_automation
```

### 🛠 Usage

```sh
python src/main.py
```

### 📂 Project Structure

```text
BIKE FORECAST AUTOMATION
├── 000_environment_setup/          # Conda environment setup files
├── data/                           # Raw & processed data
├── notebooks/                      # Jupyter notebooks
├── reports/                        # Auto-generated reports
├── src/                            # Main source code
│   ├── forecasting.py              # Forecasting logic
│   ├── reporting.py                # Report automation
│   ├── main.py                     # Entry script
├── README.md                       # Documentation
├── .gitignore                      # Files ignored by Git
├── requirements.txt                # Dependencies
├── LICENSE                         # License file 
```

### 📄 License

```text
This project is licensed under the MIT License.
```
