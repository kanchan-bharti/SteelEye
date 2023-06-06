from fastapi import FastAPI, Query
from typing import List, Optional
from schema import Trade
from database import trades_db
from datetime import datetime as dt

app = FastAPI()


@app.get('/')
def root(): 
    return "Go on, trade!"

# Endpoint to fetch a list of trades
@app.get("/trades")
def get_trades(
    search: Optional[str] = Query(None, description="Searched text"),
    asset_class: Optional[str] = Query(None, description="Asset class of the of the instrument traded."),
    start: Optional[dt] = Query(None, description="The minimum date for the tradeDateTime field."),
    end: Optional[dt] = Query(None, description="The maximum date for the tradeDateTime field."),
    max_price: Optional[float] = Query(None, description="The maximum value for the tradeDetails.price field."),
    min_price: Optional[float] = Query(None, description="The minimum value for the tradeDetails.price field."),
    trade_type: Optional[str] = Query(None, description="The tradeDetails.buySellIndicator is a BUY or SELL"),
    sort_by: Optional[str] = Query(None, description="Field to sort by"),
    sort_desc: Optional[bool] = Query(False, description="Sort in descending order"),
    page: int = Query(1, description="Page number"),
    size: int = Query(3, description="Number of trades per page"),
) -> List[Trade]:
    filtered_trades = trades_db

    # To incorporate searching trades with a string
    if search:
        filtered_trades = [trade for trade in filtered_trades if search.lower() in str(trade).lower()]

    if asset_class:
        filtered_trades = [trade for trade in filtered_trades if trade.asset_class == asset_class]
    
    if start:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_date_time >= start]

    if end:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_date_time <= end]

    if max_price:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.price <= max_price]

    if min_price:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.price >= min_price]

    if trade_type:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.buySellIndicator == trade_type]

    if sort_by:
        filtered_trades = sorted(filtered_trades, key=lambda trade: getattr(trade, sort_by), reverse=sort_desc)

    # For pagination
    if page & size:
        start_idx = (page - 1) * size
        end_idx = start_idx + size
        return filtered_trades[start_idx:end_idx]

    return filtered_trades


# Endpoint to fetch a single trade by ID
@app.get("/trades/{trade_id}")
def get_trade_by_id(trade_id: str) -> Trade:
    for trade in trades_db:
        if trade.trade_id == trade_id:
            return trade
    return {"error": "Trade not found"}


#Endpoint for pagination
@app.get("/trades/paginated")
def get_paginated_trades(
    page: int = Query(1, description="Page number"),
    size: int = Query(3, description="Number of trades per page"),
) -> List[Trade]:
    sorted_trades = trades_db

    start_idx = (page - 1) * size
    end_idx = start_idx + size

    return sorted_trades[start_idx:end_idx]