import os
import requests
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
load_dotenv()
app = App(
    token=os.environ["SLACK_BOT_TOKEN"]
)
API_KEY = os.environ["ALPHA_KEY"]
def get_stock_price(symbol):
    url = (
        "https://www.alphavantage.co/query?"
        "function=GLOBAL_QUOTE"
        f"&symbol={symbol}"
        f"&apikey={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    try:
        price = data["Global Quote"]["05. price"]
        change = data["Global Quote"]["10. change percent"]
        return price, change
    except:
        return None, None
@app.command("/stock-price")
def stock_price(ack, respond, command):
    ack()
    symbol = command["text"].upper()
    if not symbol:
        respond(
            "❌ Use it like this:\n`/stock-price AAPL`"
        )
        return
    price, change = get_stock_price(symbol)
    if price:
        respond(
            f"""
📈 *{symbol} Stock Price*
💵 Price: ${price}
📊 Change: {change}
Powered by StockBuddy
"""
        )
    else:

        respond(
            "❌ Stock not found. Try `/stock-price AAPL`"
        )
@app.command("/stock-info")
def stock_info(ack, respond, command):
    ack()
    symbol = command["text"].upper()
    if not symbol:
        respond(
            "❌ Use it like this:\n`/stock-info AAPL`"
        )
        return
    url = (
        "https://www.alphavantage.co/query?"
        "function=OVERVIEW"
        f"&symbol={symbol}"
        f"&apikey={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    if "Symbol" in data:

        respond(
            f"""
🏢 *{data['Name']} ({data['Symbol']})*
Sector: {data.get('Sector', 'N/A')}
Market Cap: {data.get('MarketCapitalization', 'N/A')}
P/E Ratio: {data.get('PERatio', 'N/A')}
52 Week High: ${data.get('52WeekHigh', 'N/A')}
52 Week Low: ${data.get('52WeekLow', 'N/A')}
Powered by StockBuddy
"""
        )
    else:
        respond(
            "❌ Company not found. Try `/stock-info AAPL`"
        )
@app.command("/stock-help")
def stock_help(ack, respond):
    ack()
    respond(
        """
📈 *StockBuddy Commands*
`/stock-price AAPL`
Get current stock price
`/stock-info AAPL`
Get company information
`/stock-help`
Show available commands
"""
    )
if __name__ == "__main__":

    SocketModeHandler(
        app,
        os.environ["SLACK_APP_TOKEN"]
    ).start()