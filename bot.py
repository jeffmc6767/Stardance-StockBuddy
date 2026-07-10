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



@app.command("/stock")
def stock_command(ack, respond, command):

    ack()

    symbol = command["text"].upper()

    price, change = get_stock_price(symbol)


    if price:

        respond(
            f"""
📈 *{symbol} Stock*

Price: ${price}
Change: {change}

Powered by StockBuddy
"""
        )

    else:

        respond(
            "❌ Stock not found. Try something like `/stock AAPL`"
        )



@app.command("/stock-help")
def help_command(ack, respond):

    ack()

    respond(
        """
📈 *StockBuddy Commands*

`/stock AAPL`
Get current stock price

`/stock-help`
Show commands
"""
    )



if __name__ == "__main__":

    SocketModeHandler(
        app,
        os.environ["SLACK_APP_TOKEN"]
    ).start()