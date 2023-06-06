from schema import Trade, TradeDetails
from datetime import datetime


# Mock Database Interations
trades_db = [
    Trade(
        assetClass="Equity",
        counterparty="ABC Broking",
        instrumentId="RELIANCE",
        instrumentName="Reliance Industries Ltd.",
        tradeDateTime=datetime(2022, 1, 1, 9, 30),
        tradeDetails=TradeDetails(buySellIndicator="BUY", price=2500.0, quantity=100),
        tradeId="1",
        trader="Rahul Sharma"
    ),
    Trade(
        assetClass="Equity",
        counterparty="XYZ Securities",
        instrumentId="TCS",
        instrumentName="Tata Consultancy Services Ltd.",
        tradeDateTime=datetime(2022, 2, 15, 14, 45),
        tradeDetails=TradeDetails(buySellIndicator="SELL", price=3100.0, quantity=50),
        tradeId="2",
        trader="Priya Gupta"
    ),
    Trade(
        assetClass="Equity",
        counterparty="DEF Investments",
        instrumentId="HDFCBANK",
        instrumentName="HDFC Bank Ltd.",
        tradeDateTime=datetime(2022, 3, 21, 11, 0),
        tradeDetails=TradeDetails(buySellIndicator="BUY", price=1400.0, quantity=200),
        tradeId="3",
        trader="Amit Patel"
    ),
    Trade(
        assetClass="Equity",
        counterparty="PQR Securities",
        instrumentId="INFY",
        instrumentName="Infosys Ltd.",
        tradeDateTime=datetime(2022, 4, 5, 10, 15),
        tradeDetails=TradeDetails(buySellIndicator="SELL", price=1700.0, quantity=75),
        tradeId="4",
        trader="Sneha Verma"
    ),
    Trade(
        assetClass="Equity",
        counterparty="LMN Broking",
        instrumentId="ICICIBANK",
        instrumentName="ICICI Bank Ltd.",
        tradeDateTime=datetime(2022, 5, 10, 15, 30),
        tradeDetails=TradeDetails(buySellIndicator="BUY", price=600.0, quantity=300),
        tradeId="5",
        trader="Ajay Singh"
    )
]