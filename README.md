# LinkedIn Automation Project

This project automates the process of logging into LinkedIn, solving CAPTCHAs, and downloading profile photos using Python and Selenium.

## Features

- **Login to LinkedIn**: Automates the login process using stored credentials.
- **Profile Photo Download**: Extracts and saves the user's profile photo.
- **Option photo resize**: You can resize parsed profile photo if you need.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BornToLivee/G-M_test.git
   cd linkedin
   ```

2. Create venv and install the required packages:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or .venv\Scripts\activate on Windows 
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your LinkedIn credentials:
   ```
   LINKEDIN_USERNAME=your_email@example.com
   LINKEDIN_PASSWORD=your_password
   ```

## Usage

1. Run the main script:
   ```bash
   python parse.py
   ```

2. Input captcha by hand or you can use other methods for solving described in captcha_solved.py file

3. Run image_upscale.py file for image resize
