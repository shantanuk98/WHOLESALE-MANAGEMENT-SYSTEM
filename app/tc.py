@app.route('/customer', methods=['GET','POST'])
def customer():
    try:
        form1 = CustomerEntry()
        form2 = CustomerSearch()
        form3 = CustomerUpdate()
        if form1.validate_on_submit():
            if form1.submitCustomerEntry.data:
                c1=Customer(name=form1.name.data,email=form1.email.data,phonenumber=form1.phonenumber.data,
                    city=form1.city.data,state=form1.state.data,country=form1.country.data,outstandingAmount=form1.oamt.data)
                db.session.add(c1)
                db.session.commit()
            return render_template('customer.html',title='CUSTOMER',form1=form1,form2=form2,form3=form3)
        if form2.validate_on_submit():
            if form2.submitCustomerSearch.data:
                conn = sqlite3.connect('app.db')
                s1 = conn.execute("select * from Customer where outstandingAmount <= "+ub(form2.uboamt.data)+" and outstandingAmount >= "+lb(form2.lboamt.data)+" name like '"+r(form2.name.data)+"' and email like +'"+r(form2.email.data)+"' and phonenumber like '"+r(form2.phonenumber.data)+"' and city like '"+r(form2.city.data)+"' and state like '"+r(form2.state.data)+"' and country like '"+r(form2.country.data)+"';")
                for a in s1:
                    print(a)
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
    except Exception as e:
        print("in customer = ",str(e))
        return render_template('customer.html',title='CUSTOMER',form1=form1,form2=form2,form3=form3)
