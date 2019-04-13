    form1 = PaymentEntry()
    form3 = PaymentSearch()
    form2 = PaymentUpdate()
    if form1.validate_on_submit():
        if form1.submitPaymentEntry.data :
            s1 = Payment(payment = form.payment.data,customerPhone=form.customerPhoneNumber.data,
                customerEmail=form.customerEmail.data,customer=form.customer.data,value=form.value.data\
                ,qty=form.qty.data,amt=form.amount.data,amtpaid=form.paid.data)
            db.session.add(s1)
            db.session.commit()
            return render_template('payment.html',title='TRANSACTION HISTORY',form1=form1,form2=form2,form3=form3)
    if form2.validate_on_submit():
        if form2.submitPaymentUpdate.data :
            s1 = Payment.query.get(int(form.id.data))
            if form2.customerName.data != "":s1.customer = form.customerName.data
            if form2.customerPhoneNumber.data != "":s1.customerPhone = form2.customerPhoneNumber.data
            if form2.customerEmail.data != "":s1.customerEmail = form2.customerEmail.data
            if form2.stockName.data != "":s1.stock = form.stockName.data
            if form2.qty.data != "":s1.qty = form.qty.data
            if form2.value.data != "":s1.value = form2.value.data
            if form2.amount.data != "":s1.amt = form2.amount.data
            if form2.paid.data != "":s1.amtpaid = form.paid.data
            db.session.commit()
            return render_template('payment.html',title='TRANSACTION HISTORY',form1=form1,form2=form2,form3=form3)
    if form1.validate_on_submit():
        if form1.submitPaymentSearch.data :
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
            t="select * from Payment where name like '"+name+"' and qty <= "+ubqty+" and qty >= "+lbqty+" and minqty <= "+ubminqty+" and minqty >= "+lbminqty+" and sp <= "+ubsp+" and sp >= "+lbsp+" and sp <= "+ubcp+" and cp >= "+lbcp+";"
            print(t)
            s2 = conn.execute(t)
            s1=[]
            for i in s2:s1.append(i)
            conn.close()
            print(s1)
            return render_template('payment.html',title='STOCK',form=form,form1=form1,form2=form2,s1=s1)
    return render_template('payment.html',title='STOCK',form=form,form1=form1,form2=form2)
