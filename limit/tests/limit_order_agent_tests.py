import unittest
from limit.limit_order_agent import LimitOrderAgent
from trading_framework.execution_client import ExecutionClient

class ExecutionClientSample(ExecutionClient):
    
    def buy(self, product_id ,amount):
        print(f"purchased {product_id}")

    def sell(self, product_id ,amount):
        print(f"sold {product_id}")
class LimitOrderAgentTest(unittest.TestCase):

    def setUp(self):
        self.limitagent = LimitOrderAgent(ExecutionClientSample())   
        
        
    def test_price_tick(self):        
        (pid,price) = self.limitagent.on_price_tick('IBM', 90)
        self.assertEqual(('IBM', 90),(pid,price))  

    # add order and execute it
    def test_add_order_buy(self):        
        testadd = self.limitagent.add_order('B', 'Prod_1', 500 , 80)
        testbuy = self.limitagent.execute_added_orders()
        self.assertEqual(testadd, testbuy)

    def test_add_order_sell(self):
        testAdd_sell = self.limitagent.add_order('S', 'Prod_2', 150 , 110)
        testsell = self.limitagent.execute_added_orders()
        self.assertEqual(testValue_sell, testsell)



if __name__ == "__main__":
    unittest.main()
    
