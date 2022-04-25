from flask import Flask, render_template
from flask import request

app= Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/FRMTP2')
def FRMTP2():
    return render_template('FRMTP2.html')

@app.route('/FRMTP2e2')
def FRMTP2e2():
    return render_template('FRMTP2e2.html')

@app.route('/login', methods=['POST'])
def login():
    z = request.form['user']
    usr = request.form['usr']
    mdp = request.form['mdp']
    Administrator = {
        'Login': 'admin',
        'password': 'admin'
    }
    Guest = {
        'Login': 'user',
        'password': 'user'
    }
    if z=='Administrator':
        if usr == Administrator.get('Login') and mdp == Administrator.get('password'):
            return render_template('user.html', value=usr)
        else:
            return render_template('denied.html')
    else:
        if usr == Guest.get('Login') and mdp == Guest.get('password'):
            return render_template('user.html', value=usr)
        else:
            return render_template('denied.html')

@app.route('/somme',methods=['POST'])
def somme():
    x=request.form.get('x')
    y=request.form['y']
    r=int(x)+int(y)
    return render_template('somme.html',value=r,value1=x,value2=y)
    
@app.route('/Facture',methods=['POST'])
def Facture():
    nom=request.form.get('nom')
    prn=request.form.get('prn')
    cp=request.form['cp']
    cq=request.form['cq']
    pc=float(cp)*float(cq)
    sp = request.form['sp']
    sq = request.form['sq']
    ps = float(sp) * float(sq)
    scp = request.form['scp']
    scq = request.form['scq']
    psc = float(scp) * float(scq)
    pT=pc+ps+psc
    return render_template('tFacture.html',value=nom,value1=prn,value2=cp,value3=cq,value4=sp,value5=sq,value6=scp,value7=scq,value8=pc,value9=ps,value10=psc,value11=pT)




@app.route('/produit',methods=['POST'])
def produit():
    x=request.form.get('x')
    y=request.form['y']
    r=int(x)*int(y)
    return render_template('produit.html',value=r,value1=x,value2=y)





@app.route('/division',methods=['POST'])
def division():
    x=request.form.get('x')
    y=request.form['y']
    r=int(x)/int(y)
    return render_template('division.html',value=r,value1=x,value2=y)



@app.route('/factoriel',methods=['POST'])
def factoriel():
    x=request.form.get('x')
    r=1
    for i in range(2,int(x)+1):
        r=r*i

    return render_template('factoriel.html',value=r,value1=x)



if __name__ =="__main__":
    app.run(host="localhost",port=5000,debug=True)