PublicKey = "***REMOVED***"
SecretKey = "***REMOVED***"

QuotedCurrency = 'USD' #Котируемая валюта
Quantity = 4 #Колисчество валютных пар для торговли
Profit = 0.03 #необходимый навар (0.01 = 1%)
StockFee = 0.001 #комиссия биржи (0.01 = 1%)
Period = 60 #время для расчетов (1 = 1 мин)
Sleep = 120 #время ожидания бота (1 = 1 сек)
MinRank = 2000 #минимальный ранг торгуемых валют
MinDegree = -2 #минимальный градус наклона рынка, при котором можно покупать валюту
MaxDegree = 180 #максимальный градус рынка, при котором можно покупать валюту

#Private setings
Balance = [] #Баланс
MaxPrice = 0 #Максимальная цена
TradedCurrency = [] #Валюты для торговли
Orders = [] #Ордера ??
Mask = '{"symbol": "text", "ask": 0, "bid": 0, "rank": 0, "quantityIncrement": 0, "quantity": 0}' #Объект валюты на продажу