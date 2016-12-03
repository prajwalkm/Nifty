# Nifty50scrapeAPP

scrape_script.py scrapes the data from Nifty 50 table 
(from URl:https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G)
and stores it in redis instance

cherrypy stand alone web app cherrypyapp.py fetch data from redis and display it in browser(Card layout style)
it in CherryPyApp.py

steps:

1. activate your virtualenv.

2. run: pip install -r requirements.txt in your shell.

3. run: python scrape_script.py using shell

4. run: python cherrypyApp.py using shell

5.run browser on 127.0.0.1:8000 or localhost:8000

