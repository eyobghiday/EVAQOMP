# 🧠 EVAQOMP Wiki Guide

**EVAQOMP** (Emotional Volatility Analysis Quantified Optimization and Machine Prediction) is an intelligent trading platform that automates trading decisions using real-time sentiment analysis from social media and financial news. This bot aims to leverage emotional sentiment indicators to execute trades using a connected brokerage API.

---

## 🧩 Architecture Overview

```
        ┌────────────┐      ┌──────────────┐      ┌────────────┐
        │   Reddit   │ ---> │ Sentiment LLM│ ---> │ Signal DB  │
        └────────────┘      └──────────────┘      └────┬───────┘
                                                       │
        ┌────────────┐      ┌──────────────┐      ┌────▼─────┐
        │ Dashboard  │ <--- │   EVAQOMP    │ ---> │ Alpaca   │
        └────────────┘      └──────────────┘      └──────────┘
```

---

## 🔧 Components

| Module        | Description |
|---------------|-------------|
| `scrapers/`   | Pulls Reddit or news content |
| `utils/`      | LLM-based sentiment analysis |
| `db/`         | SQLite database for storing signals |
| `trader/`     | Alpaca API integration to execute trades |
| `dashboard/`  | Streamlit app for visualization |
| `main.py`     | Ingests data, analyzes it, stores in DB |

---

## 🧪 Sample Workflow

1. **Collect posts** → Pull Reddit/news content.
2. **Analyze** → Use an LLM to extract ticker mentions and sentiment.
3. **Store** → Save result in a structured SQLite database.
4. **Visualize** → Display signals and filter via Streamlit dashboard.
5. **Trade** → Place market buy orders if sentiment is positive. Automatically set a 10% stop loss.

---

## 🛡️ Safety Mechanisms

- Market orders only on positive signals.
- Stop loss at 10% for every trade.
- Profit-taking logic will be modular and added in future iterations.

---

## 📊 Technologies Used

- Python, Streamlit
- Alpaca API for trading
- OpenAI API for sentiment analysis
- SQLite for lightweight storage

---

# 🚀 GitHub Hosting Instructions

## 🔹 Step 1: Upload Project

1. Go to [GitHub](https://github.com) and create a new repository (e.g., `evaqomp`).
2. On the repo page, click **"Add file" → "Upload files"**.
3. Upload the contents of the unzipped `evaqomp_package.zip`.

> 💡 *Don't upload the `.zip` itself — extract it and upload the contents.*

---

## 🔹 Step 2: Setup `.env` File

Create a file called `.env` in the root of the project:

```
OPENAI_API_KEY=your_openai_key
ALPACA_API_KEY=your_alpaca_key
ALPACA_SECRET_KEY=your_alpaca_secret
```

> Do NOT commit `.env` — it's listed in `.gitignore`.

---

## 🔹 Step 3: Install and Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/evaqomp.git
cd evaqomp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run dashboard
streamlit run evaqomp/dashboard/app.py
```

---

## 🔹 Step 4: Schedule `main.py` to Run Periodically (Optional)

You can run `main.py` on a schedule using:

- **cron** on Linux/macOS
- **Task Scheduler** on Windows
- **GitHub Actions** (advanced deployment)

---

## ✅ Next Steps

- Implement Twitter/X and news scrapers
- Add more refined LLM logic with OpenAI or Claude
- Build backtesting and risk management tools
- Deploy Streamlit app on a server or cloud platform (e.g., Streamlit Community Cloud, Heroku)
