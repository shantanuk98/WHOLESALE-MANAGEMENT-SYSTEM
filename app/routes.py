from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import *
from app import db
from app.models import *
from sqlalchemy import text,update
import  sqlite3
s1=""

def r(s):return '%'+s+'%'
def ub(s):
    if s.isnumeric():return str(s)
    else:return "100000000000000000"
def lb(s):
    if s.isnumeric():return str(s)
    else:return "0"

@app.route('/')
@app.route('/index')
def index():
    c = sqlite3.connect('app.db')
    s=("sum = ",list(c.execute("select sum(value) from Payments"))[0][0])
    print(s)
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/stock', methods=['GET','POST'])
def stock():
    form = StockEntry()
    form1 = StockSearch()
    form2 = StockUpdate()
    if form.validate_on_submit():
        if form.submitStockEntry.data :
            s1 = Stock(name = form.name.data,qty=form.qty.data,
                minqty=form.minqty.data,sp=form.sp.data,cp=form.cp.data)
            db.session.add(s1)
            db.session.commit()
            return render_template('stock.html',title='STOCK',form=form,form1=form1,form2=form2)
    if form2.validate_on_submit():
        if form2.submitStockUpdate.data :
            conn = sqlite3.connect('app.db')
            name = form2.name.data
            qty=form2.qty.data
            minqty=form2.minqty.data
            sp=form2.sp.data
            cp=form2.cp.data
            s2 = conn.execute("select * from Stock where name like '"+name+"';")
            s = []
            for i in s2:s.append(i)
            s=list(s[0])
            print(s)
            if qty.isnumeric():s[2] = qty
            if minqty.isnumeric():s[3] = minqty
            if sp.isnumeric():s[4] = sp
            if cp.isnumeric():s[5]=cp
            s3 = Stock.query.filter_by(name=name).first()
            print(s3)
            s3.qty = s[2]
            s3.minqty = s[3]
            s3.sp = s[4]
            s3.cp = s[5]
            db.session.commit()
            return render_template('stock.html',title='STOCK',form=form,form1=form1,form2=form2)
    if form1.validate_on_submit():
        if form1.submitStockSearch.data :
            conn = sqlite3.connect('app.db')
            name=r(form1.name.data)
            lbqty = lb(form1.lbqty.data)
            ubqty = ub(form1.ubqty.data)
            lbminqty = lb(form1.lbminqty.data)
            ubminqty = ub(form1.ubminqty.data)
            lbsp = lb(form1.lbsp.data)
            ubsp = ub(form1.ubsp.data)
            lbcp = lb(form1.lbcp.data)
            ubcp = ub(form1.ubcp.data)
            t="select * from Stock where name like '"+name+"' and qty <= "+ubqty+" and qty >= "+lbqty+" and minqty <= "+ubminqty+" and minqty >= "+lbminqty+" and sp <= "+ubsp+" and sp >= "+lbsp+" and sp <= "+ubcp+" and cp >= "+lbcp+";"
            print(t)
            s2 = conn.execute(t)
            s1=[]
            for i in s2:s1.append(i)
            conn.close()
            print(s1)
            return render_template('stock.html',title='STOCK',form=form,form1=form1,form2=form2,s1=s1)
    return render_template('stock.html',title='STOCK',form1=form1,form2=form2,form3=form3,s1=s1)

@app.route('/customer', methods=['GET','POST'])
def customer():
    form1 = CustomerEntry()
    form2 = CustomerSearch()
    form3 = CustomerUpdate()
    if form1.validate_on_submit():
        if form1.submitCustomerEntry.data:
            c1=Customer(name=form1.name.data,email=form1.email.data,phonenumber=form1.phonenumber.data,
                city=form1.city.data,state=form1.state.data,country=form1.country.data,outstandingAmount=form.oamt.data)
            db.session.add(c1)
            db.session.commit()
        return render_template('customer.html',title='CUSTOMER',form1=form1,form2=form2,form3=form3)
    if form2.validate_on_submit():
        if form2.submitCustomerSearch.data:
            conn = sqlite3.connect('app.db')
            s1 = conn.execute("select * from Customer where outstandingAmount <= "+ub(form.uboamt.data)+" and outstandingAmount >= "+lb(form.lboamt.data)+" name like '"+r(form2.name.data)+"' and email like +'"+r(form2.email.data)+"' and phonenumber like '"+r(form2.phonenumber.data)+"' and city like '"+r(form2.city.data)+"' and state like '"+r(form2.state.data)+"' and country like '"+r(form2.country.data)+"';")
        return render_template('customer.html',title='CUSTOMER',form1=form1,form2=form2,form3=form3,s1=s1)
    if form3.validate_on_submit():
        if form3.submitCustomerUpdate.data:
            s1 = Customer.query.filter_by(email=form.email.data).first()
            s1.name = form3.name.data
            s1.phonenumber = form3.phonenumber.data
            s1.city = form3.phonenumber.data
            s1.state = form3.state.data
            s1.country = form3.country.data
            s1.outstandingAmount = form3.oamt.data
            db.session.commit()    
        return render_template('customer.html',title='CUSTOMER',form1=form1,form2=form2,form3=form3)
    return render_template('customer.html',title='CUSTOMER',form1=form1,form2=form2,form3=form3)

@app.route('/payment', methods=['GET','POST'])
def payment():
    form1 = PaymentEntry()
    form3 = PaymentSearch()
    form2 = PaymentUpdate()
    if form1.validate_on_submit():
        if form1.submitPaymentEntry.data :
            s1 = Payments(stock = form1.stockName.data,customerPhone=form1.customerPhonenumber.data,
                customerEmail=form1.customerEmail.data,customer=form1.customerName.data,value=form1.value.data\
                ,qty=form1.qty.data,amt=form1.amount.data,amtpaid=form1.paid.data)
            db.session.add(s1)
            db.session.commit()
            return render_template('payment.html',title='TRANSACTION HISTORY',form1=form1,form2=form2,form3=form3)
    if form2.validate_on_submit():
        if form2.submitPaymentUpdate.data :
            s1 = Payments.query.get(int(form2.id.data))
            if form2.customerName.data != "":s1.customer = form2.customerName.data
            if form2.customerPhonenumber.data != "":s1.customerPhone = form2.customerPhonenumber.data
            if form2.customerEmail.data != "":s1.customerEmail = form2.customerEmail.data
            if form2.stockName.data != "":s1.stock = form2.stockName.data
            if form2.qty.data != "":s1.qty = form.qty.data
            if form2.value.data != "":s1.value = form2.value.data
            if form2.amount.data != "":s1.amt = form2.amount.data
            if form2.paid.data != "":s1.amtpaid = form2.paid.data
            db.session.commit()
            return render_template('payment.html',title='TRANSACTION HISTORY',form1=form1,form2=form2,form3=form3)
    if form3.validate_on_submit():
        if form3.submitPaymentSearch.data :
            print("submit payment search clicked")
            conn = sqlite3.connect('app.db')
            name=r(form3.stockName.data)
            pn = r(form3.customerPhonenumber.data)
            lbqty = lb(form3.lbqty.data)
            ubqty = ub(form3.ubqty.data)
            lbvalue = lb(form3.lbvalue.data)
            ubvalue = ub(form3.ubvalue.data)
            lbpaid = lb(form3.lbpaid.data)
            ubpaid = ub(form3.ubpaid.data)
            lbamount = lb(form3.lbamount.data)
            ubamount = ub(form3.ubamount.data)
            t="select * from Payments where stock like '"+name+"' and qty <= "+ubqty+" and qty >= "+lbqty+" and value <= "+ubvalue+" and value >= "+lbvalue+" and amtpaid <= "+ubpaid+" and amtpaid >= "+lbpaid+" and amt <= "+ubamount+" and amt >= "+lbamount+";"
            print(t)
            s2 = conn.execute(t)
            s1=[]
            for i in s2:s1.append(i)
            conn.close()
            print(s1)
            return render_template('payment.html',title='STOCK',form1=form1,form2=form2,form3=form3,s1=s1)
    return render_template('payment.html',title='STOCK',form1=form1,form2=form2,form3=form3)


@app.route('/itb', methods=['GET','POST'])
def itb():
    conn = sqlite3.connect('app.db')
    s2 = conn.execute('select *  from Stock where minqty>=qty;')
    s1=[]
    for i in s2:s1.append(i)
    conn.close()
    return render_template('itb.html',title='ITEMS TO BUY',s1=s1)

@app.route('/supplier', methods=['GET','POST'])
def supplier():
    form1 = SupplierEntry()
    form2 = SupplierSearch()
    form3 = SupplierUpdate()
    if form1.validate_on_submit():
        if form1.submitSupplierEntry.data:
            c1=Supplier(name=form1.name.data,stock=form.stock.data,email=form1.email.data,phonenumber=form1.phonenumber.data,
                city=form1.city.data,state=form1.state.data,country=form1.country.data,outstandingAmount=form.oamt.data)
            db.session.add(c1)
            db.session.commit()
        return render_template('supplier.html',title='Supplier',form1=form1,form2=form2,form3=form3)
    if form2.validate_on_submit():
        if form2.submitSupplierSearch.data:
            conn = sqlite3.connect('app.db')
            s1 = conn.execute("select * from Supplier where stock like "+r(form2.stock.data)+" and name like '"+r(form2.name.data)+"' and email like +'"+r(form2.email.data)+"' and phonenumber like '"+r(form2.phonenumber.data)+"' and city like '"+r(form2.city.data)+"' and state like '"+r(form2.state.data)+"' and country like '"+r(form2.country.data)+"';")
        return render_template('supplier.html',title='Supplier',form1=form1,form2=form2,form3=form3,s1=s1)
    if form3.validate_on_submit():
        if form3.submitSupplierUpdate.data:
            s1 = Supplier.query.filter_by(email=form.email.data).first()
            s1.name = form3.name.data
            s1.phonenumber = form3.phonenumber.data
            s1.city = form3.phonenumber.data
            s1.state = form3.state.data
            s1.country = form3.country.data
            s1.stock = form3.stock.data
            db.session.commit()    
        return render_template('supplier.html',title='Supplier',form1=form1,form2=form2,form3=form3)
    return render_template('supplier.html',title='Supplier',form1=form1,form2=form2,form3=form3)
@app.route('/defaulter', methods=['GET','POST'])
def defaulter():
    return render_template('defaulter.html',title='DEFAULTER')