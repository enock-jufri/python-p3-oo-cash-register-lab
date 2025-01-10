#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0,total=0.0,items=None):
    self.discount=discount
    self.total=total
    self.items = items if items is not None else []
    
  def add_item(self,title,price,quantity=1):
    self.title=title
    self.price=price
    self.quantity=quantity
    
    self.total+=(self.price * self.quantity)
    self.last_transaction = price * quantity
    
    for i in range(1,quantity+1):
      self.items.append(self.title)
      
  def apply_discount(self):
    if self.discount == 0:
      print ("There is no discount to apply.")
    else:
      self.total-=((self.discount*0.01)*self.total)
      print (f"After the discount, the total comes to ${int(self.total)}.")
      
  def void_last_transaction(self):
    self.total-=self.last_transaction

