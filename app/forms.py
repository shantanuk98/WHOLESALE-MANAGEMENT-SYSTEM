from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CustomerEntry(FlaskForm):
    name = StringField('Customer name' )
    email = StringField('email' )
    phonenumber = StringField('phone' )
    city = StringField('city' )
    state = StringField('state' )
    country = StringField('country' )
    oamt = StringField('Outstanding amount')
    submitCustomerEntry = SubmitField('enter customer details')

class CustomerSearch(FlaskForm):
    name = StringField('Customer name' )
    email = StringField('email' )
    phonenumber = StringField('phone' )
    city = StringField('city' )
    state = StringField('state' )
    country = StringField('country' )
    uboamt = StringField('uboamt')
    lboamt = StringField('lboamt')
    submitCustomerSearch = SubmitField('search customer details')

class CustomerUpdate(FlaskForm):
    name = StringField('Customer name' )
    email = StringField('email' )
    phonenumber = StringField('phone')
    city = StringField('city')
    state = StringField('state')
    oamt = StringField('Outstanding amount')
    country = StringField('country')
    submitCustomerUpdate = SubmitField('update customer details')

class StockEntry(FlaskForm):
    name = StringField('Stock name')
    qty = StringField('Qunantity')
    minqty = StringField('Minimum quantity')
    sp = StringField('Selling Price')
    cp = StringField('Cost Price')
    submitStockEntry = SubmitField('enter')

class StockUpdate(FlaskForm):
    name = StringField('Stock name' )
    qty = StringField('Qunantity')
    minqty = StringField('Minimum quantity')
    sp = StringField('Selling Price')
    cp = StringField('Cost Price')
    submitStockUpdate = SubmitField('Update stock details')


class StockSearch(FlaskForm):
    name = StringField('Stock name')
    lbqty = StringField('lbqty')
    ubqty = StringField('upqty')
    lbminqty = StringField('lbminqty')
    ubminqty = StringField('upminqty')
    lbsp = StringField('lbsp')
    ubsp = StringField('upsp')
    lbcp = StringField('lbcp')
    ubcp = StringField('ubcp')
    submitStockSearch = SubmitField('search')


class SupplierEntry(FlaskForm):
    name = StringField('supplier name' )
    stockName = StringField('Stock name' )
    email = StringField('email' )
    phonenumber = StringField('phone' )
    city = StringField('city' )
    state = StringField('state' )
    country = StringField('country' )
    submitSupplierEntry = SubmitField('Enter supplier details')

class SupplierUpdate(FlaskForm):
    name = StringField('supplier name' )
    stockName = StringField('Stock name' )
    email = StringField('email' )
    phonenumber = StringField('phone' )
    city = StringField('city' )
    state = StringField('state' )
    country = StringField('country' )
    submitSupplierUpdate = SubmitField('Update supplier details')

class SupplierSearch(FlaskForm):
    name = StringField('Supplier name' )
    stockName = StringField('stock name' )
    email = StringField('email' )
    phonenumber = StringField('phone' )
    city = StringField('city' )
    state = StringField('state' )
    country = StringField('country' )
    submitSupplierSearch = SubmitField('search suppliers details')

class PaymentEntry(FlaskForm):
    customerName = StringField('Customer name' )
    customerPhonenumber = StringField('Customer phonenumber' )
    customerEmail = StringField('Customer email' )
    stockName = StringField('Stock name' )
    qty = StringField('quantity' )
    value = StringField('item value' )
    amount = StringField('total bill amount' )
    paid = StringField('amount paid' )
    submitPaymentEntry = SubmitField('enter payment details')

class PaymentUpdate(FlaskForm):
    id = StringField('Id')
    customerName = StringField('Customer name' )
    customerPhonenumber = StringField('Customer phonenumber' )
    customerEmail = StringField('Customer email' )
    stockName = StringField('Stock name' )
    qty = StringField('quantity' )
    value = StringField('item value' )
    amount = StringField('total bill amount' )
    paid = StringField('amount paid' )
    submitPaymentUpdate = SubmitField('Update payment deatails')

class PaymentSearch(FlaskForm):
    id = StringField('customerId')
    customerName = StringField('Customer name' )
    customerPhonenumber = StringField('Customer name' )
    customerEmail = StringField('Customer name' )
    stockName = StringField('Stock name' )
    ubqty = StringField('ubqty' )
    lbqty = StringField('lbqty' )
    ubvalue = StringField('ubvalue' )
    lbvalue = StringField('lbvalue' )
    lbamount = StringField('total bill amount' )
    ubamount = StringField('total bill amount' )
    lbpaid = StringField('ubpaid' )
    ubpaid = StringField('lbpaid' )
    submitPaymentSearch = SubmitField('Search payment deatails')
