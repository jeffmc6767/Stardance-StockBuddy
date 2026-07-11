This is a custom slackbot that works by pulling information from Alpha Vantage through its API key. Im running it on my Ubuntu server/homlab and it is connected to Hack Club's server: https://app.slack.com/client/E09V59WQY1E/C0P5NE354 

Here are the working commmands:

**/stock-price** 
  gets current stock price
**/stock-info** 
EXAMPLE: 
   Apple Inc. (AAPL)
  Sector: TECHNOLOGY
  Market Cap: 4644435657000
  P/E Ratio: 38.24
  52 Week High: $317.4
  52 Week Low: $200.7
  Powered by StockBuddy

**/stock-help**:
  Shows all stock commands



If you want to use this run bot.py and change the .env file to your own API keys through this format: 
SLACK_BOT_TOKEN=your_xoxb_token
SLACK_APP_TOKEN=your_xapp_token
ALPHA_KEY=your_alpha_vantage_key
