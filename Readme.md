# Social Bot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/mahirahmed691/social-bot.svg)](https://github.com/mahirahmed691/social-bot/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mahirahmed691/social-bot.svg)](https://github.com/mahirahmed691/social-bot/network/members)

Social Bot is a Python script designed to automate the process of posting pictures on Instagram with customizable captions and links. Leveraging the Instagram Graph API, it facilitates the seamless upload of photos, enhancing your social media management capabilities.

## Features

- **Photo Uploads:** Effortlessly upload photos to your Instagram account directly through the script.
- **Caption Customization:** Tailor your Instagram posts with captions that resonate with your audience.
- **Link Integration:** Include links in your posts, allowing you to drive traffic and engagement.

## Getting Started

### Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- The `requests` library (`pip install requests`)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/mahirahmed691/social-bot.git
    cd social-bot
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Obtain an Access Token:**
   
   Obtain an access token from the Instagram Graph API by following the instructions [here](#).

2. **Update Access Token:**
   
   Update the `access_token` variable in the script with your acquired access token.

3. **Customize Script Parameters:**
   
   Customize the following parameters in the example usage section of the script:
   - **File Path:** Set the file path to the actual location of the photo you want to upload.
   - **Caption:** Define the caption for your Instagram post.
   - **Link:** If applicable, replace `'https://your-link.com'` with your actual link.

4. **Run the Script:**

    ```bash
    python insta_automation_script.py
    ```

### Alternative Usage

You can also run the script with command-line arguments:

```bash
python insta_automation_script.py path/to/photo.jpg "Your caption here" "https://your-link.com"
