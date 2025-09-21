📧 **Email News App**

A Python automation project that brings the world’s latest headlines directly to your inbox.

Whether you're tracking technology trends, market updates, or breaking world news, this lightweight app fetches real-time articles on a topic of your choice and emails them to you daily — no distractions, no ads, just pure news in your inbox.

📰 **What It Does:**

Uses NewsAPI to fetch the latest news based on a topic (like “Tesla”, “AI”, or “Stock Market”).

Summarizes the top 20 articles with title, description, and link.

Sends the news digest via email using Gmail's secure SMTP (SSL) server.

Designed for automation — perfect for daily or scheduled runs using cron or Task Scheduler.


🔧 **Project Structure**


├── **main.py**           # Core script: fetches news and triggers the email

├── **SendEmail.py**      # Handles secure email sending via SMTP

├── **README.md**         # Documentation for the project


✅ **Features**

🌐 Live News Fetching – Real-time data from NewsAPI

🔒 Secure Emailing – Uses Gmail’s SSL encryption

✉️ Minimalist Digest Format – No HTML, no clutter — just the essentials

📦 Environment Variable Support – No hardcoded passwords

🔁 Easily Automatable – Set it and forget it with scheduled runs

🧩 Modular Codebase – Separated logic for fetching and sending


🔑 **Required Setup**

✅ 1. Gmail App Password

If using Gmail:
* Enable 2-Step Verification for your Google account.
* Go to App Passwords
* Generate an app password for "Mail".
* Store this securely – you'll need it in the next step.

✅ 2. Get NewsAPI Key

* Sign up at https://newsapi.org/
* Generate your free API key


🧠 **How It Works**

main.py

* Accepts a topic (e.g. tesla, crypto)
* Queries NewsAPI and parses article data
* Formats the email body
* Sends it via the send_email() function

SendEmail.py

* Connects to Gmail’s SMTP server using SSL
* Authenticates using the sender's email and app password
* Sends the email to the desired recipient