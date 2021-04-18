* Bot returns price for needed amount of currency (euro, dollar or ruble).

* Library **pytelegrambotapi** was used in making of this bot.

* User required to message bot in format (2 keywords and a number, with whitespace between each)

* For example: USD RUB 1500

* If user enters commands **/start** or **/help** instructions on how to use the bot are shown.

* If user enters command **/values** info about all available currencies is shown.

* For getting currency values API is used and requests to it are sent with help of **Requests** library.

* For parsing library **JSON** is used.

* In event of user error (for example, typing mistake or nonexistent currency or incorrect input of number) returns custom exception APIException with text of error description.

* Text of any error with type of error is sent to user in message.

* For sending requests to API class with static method **get_price()** is used, which takes 3 arguments (described below) and returns required sum in currency.
  * **base** — currency name, price of which user wants to know
  * **quote** — currency name, price in which user wants to know
  * **amount** — amount of currency to transfer

* Token of telegram-bot is in special config.

* All classes hidden in file **extensions.py**.
