class Account:
    def __init__(self, username: str, initial_deposit: float):
        """
        Initializes a new account with a given username and initial deposit.

        :param username: Unique identifier for the user.
        :param initial_deposit: Initial amount of money to deposit into the account.
        """
        self.username = username
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []
        self.initial_deposit = initial_deposit

    def deposit(self, amount: float) -> None:
        """
        Deposits an amount into the account.

        :param amount: Amount to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws an amount from the account.

        :param amount: Amount to withdraw.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount}")

    def buy_shares(self, symbol: str, quantity: int) -> None:
        """
        Buys shares of a given stock.

        :param symbol: The stock symbol to buy.
        :param quantity: The quantity of shares to buy.
        """
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        
        self.balance -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append(f"Bought {quantity} shares of {symbol} at ${share_price} each")

    def sell_shares(self, symbol: str, quantity: int) -> None:
        """
        Sells shares of a given stock.

        :param symbol: The stock symbol to sell.
        :param quantity: The quantity of shares to sell.
        """
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Not enough shares to sell.")
        
        share_price = get_share_price(symbol)
        total_revenue = share_price * quantity
        
        self.balance += total_revenue
        self.holdings[symbol] -= quantity
        self.transactions.append(f"Sold {quantity} shares of {symbol} at ${share_price} each")

    def total_portfolio_value(self) -> float:
        """
        Calculates the total value of the user's portfolio, including cash and stock value.

        :return: The total value of the portfolio.
        """
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def profit_or_loss(self) -> float:
        """
        Calculates the profit or loss from the initial deposit.

        :return: The profit or loss amount.
        """
        return self.total_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> dict:
        """
        Returns a dictionary of the user's current holdings.

        :return: A dictionary containing stock symbols and quantities owned.
        """
        return self.holdings

    def get_transactions(self) -> list:
        """
        Returns a list of the user's transactions.

        :return: A list of transaction strings.
        """
        return self.transactions


def get_share_price(symbol: str) -> float:
    """
    Mock implementation of getting the share price based on the symbol.

    :param symbol: The stock symbol.
    :return: The current price of the stock.
    """
    prices = {
        'AAPL': 150.0,
        'TSLA': 720.0,
        'GOOGL': 2800.0
    }
    return prices.get(symbol, 0.0)  # Default to 0.0 if the symbol does not exist