import streamlit as st
import pandas as pd
from db.database import fetch_all_signals
import alpaca_trade_api as tradeapi

st.set_page_config(page_title="EVAQOMP Dashboard", layout="wide")
st.title("📈 EVAQOMP - Sentiment-Based Auto Trading Dashboard")

signals = fetch_all_signals()
df = pd.DataFrame(signals, columns=["ID", "Timestamp", "Source", "Raw Text", "Tickers", "Sentiment", "Summary"])
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values("Timestamp", ascending=False)

st.subheader("📋 Recent Sentiment Signals")
st.dataframe(df[["Timestamp", "Source", "Tickers", "Sentiment", "Summary"]], use_container_width=True)

st.sidebar.header("🔍 Filter")
sent_filter = st.sidebar.selectbox("Sentiment", ["All", "Positive", "Negative", "Neutral"])
if sent_filter != "All":
    df = df[df["Sentiment"] == sent_filter]

st.subheader("📊 Signal Frequency Over Time")
plot_df = df.copy()
plot_df["Date"] = plot_df["Timestamp"].dt.date
chart_data = plot_df.groupby(["Date", "Sentiment"]).size().unstack(fill_value=0)
st.line_chart(chart_data)

st.subheader("💼 Alpaca Open Positions")
try:
    api = tradeapi.REST("YOUR_ALPACA_API_KEY", "YOUR_ALPACA_SECRET_KEY", "https://paper-api.alpaca.markets")
    positions = api.list_positions()
    pos_data = [{
        "Symbol": p.symbol,
        "Qty": p.qty,
        "Entry Price": p.avg_entry_price,
        "Current Price": p.current_price,
        "Unrealized P/L": p.unrealized_pl
    } for p in positions]
    st.table(pd.DataFrame(pos_data))
except Exception as e:
    st.warning(f"Could not fetch Alpaca positions: {e}")
# Placeholder for Reddit scraper using PRAW or requests