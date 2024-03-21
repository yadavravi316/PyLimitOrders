from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener

# created ExecutionClientSample so that its object implements Protocol

class ExecutionClientSample:
    
    def buy(self, Product_id : str ,amount : int):
        """ code for buy """
        pass
        
    def sell(self, Product_id : str ,amount : int):
        """ code for sell """
        pass
        
class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        super().__init__()
        self.execution_client = execution_client
        
    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        # if price is below 100 then buy 1000 Shares
        
        if(price < 100):
            self.execution_client.buy(Product_id ,1000)
        return True
        
    def add_order(self, flag : str, Product_id: str, amount :int, limit : float):
        """ based on flag buy and sell can be used """
        
        if(flag == 'B'):
            self.execution_client.buy(Product_id ,amount)
            return True
            
        elif(flag == 'S'):
            self.execution_client.sell(Product_id ,amount)
            return True
