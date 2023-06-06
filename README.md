# SteelEye
Assignment submission for Data Engineering internship

**Submission of KANCHAN BHARTI**

## The Approach

1. As [FastAPI](https://fastapi.tiangolo.com/) was mentioned, to run the API installed [Uvicorn](https://www.uvicorn.org/) too:

    `pip3 install fastapi "uvicorn[standard]"`

2. Configured a `schema.py`  with the [Schema Model](https://github.com/steeleye/recruitment-ext/wiki/API-Developer-Assessment#schema-model) provided.
3. Configured `database.py` for the [Mock Database Interation Layer](https://github.com/steeleye/recruitment-ext/wiki/API-Developer-Assessment#database) by creating the `trades_db` with a few example trade objects for testing purposes.
4. In `main.py`, created an instance of the  [FastAPI](https://fastapi.tiangolo.com/)
5. [Listing Trades](https://github.com/steeleye/recruitment-ext/wiki/API-Developer-Assessment#listing-trades) 
	- Configured the `/trades` path by defining `get_trades` function, which returns the `trades_db` on `GET`
6. [Searching Trades](https://github.com/steeleye/recruitment-ext/wiki/API-Developer-Assessment#searching-trades): 
	- configured the search endpoint on `/trades/` such that it performs a case-insensitive search on the specified fields (`counterparty`, `instrumentId`, `instrumentName`, and `trader`). It returns a list of trades where the search text exists in any of these fields.
	- I used FastAPI's `Query` parameters to handle optional filtering based on the searched term.
7. and [Advanced Filtering](https://github.com/steeleye/recruitment-ext/wiki/API-Developer-Assessment#advanced-filtering) : **`/trades`,**
	- For the endpoint to fetch a list of trades (`GET` on  `/trades`), again used `Query` parameters for filtering based on the query parameters provided (`assetClass`, `end`, `maxPrice`, `minPrice`, `start`, and `tradeType`.
	- The server then threw 4 validation errors, like this one: `instrumentId field required (type=value_error.missing)`. I changed all the field types to Optional, to see the output once. It showed the JSON output with `null` values in the corresponding fields which threw Validation Errors. From that output I figured, in my `trades_db` I had not named my fields according to the `alias` used in `schema.py`. So I did the necessary changes and it worked fine.
8. [Single Trade](https://github.com/steeleye/recruitment-ext/wiki/API-Developer-Assessment#single-trade) : **`/trades/{trade_id}`**
	- The endpoint to fetch a single trade by ID (`GET` on `/trades/{trade_id}`) iterates over the `trades_db` list and returns the trade with the matching ID.
9. [Sorting](https://github.com/steeleye/recruitment-ext/wiki/API-Developer-Assessment#bonus-points):
	- Configured sorting on `/trades`  using the `sort_by` and `sort_desc` parameter. 
	- `/trades?sort_by=counterparty` sorts the `filtered_trades` in the ascending order by default (`sort_desc` is `False`)
10. Finally, pagination:
	- Implemented the pagination using `page`(page number, default is 1) and `size`(number of trades per page, default is 3) parameters. 
	- `http://127.0.0.1:8000/trades` now returns 3 trades per page by default.