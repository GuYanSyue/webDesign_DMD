from flask import Flask,render_template

app = Flask(__name__)

@app.route('/') #Flask路由指向 網址的根目錄
def index_Dungeons():
    return render_template('index_Dungeons.html') #return url string 中回傳index.html 做為模板

@app.route("/Algethar_Academy") #Flask路由指向 網址的根目錄
def Algethar_Academy():
    return render_template('html/Algethar_Academy.html')
@app.route("/Brackenhide_Hollow") #Flask路由指向 網址的根目錄
def Brackenhide_Hollow():
    return render_template('html/Brackenhide_Hollow.html')
@app.route("/Halls_of_Infusion") #Flask路由指向 網址的根目錄
def Halls_of_Infusion():
    return render_template('html/Halls_of_Infusion.html')
@app.route("/Neltharus") #Flask路由指向 網址的根目錄
def Neltharus():
    return render_template('html/Neltharus.html')
@app.route("/Ruby_Life_Pools") #Flask路由指向 網址的根目錄
def Ruby_Life_Pools():
    return render_template('html/Ruby_Life_Pools.html')
@app.route("/The_Azure_Vault") #Flask路由指向 網址的根目錄
def The_Azure_Vault():
    return render_template('html/The_Azure_Vault.html')
@app.route("/Uldaman_Legacy_of_Tyr") #Flask路由指向 網址的根目錄
def Uldaman_Legacy_of_Tyr():
    return render_template('html/Uldaman_Legacy_of_Tyr.html')
@app.route("/The_Nokhud_Offensive") #Flask路由指向 網址的根目錄
def The_Nokhud_Offensive():
    return render_template('html/The_Nokhud_Offensive.html')

@app.route("/M+") #Flask路由指向 網址的根目錄
def index_Mythic():
    return render_template('index_Mythic.html')

@app.route("/M_Algethar_Academy") #Flask路由指向 網址的根目錄
def M_Algethar_Academy():
    return render_template('htmlM+/M_Algethar_Academy.html')
@app.route("/M_Ruby_Life_Pools") #Flask路由指向 網址的根目錄
def M_Ruby_Life_Pools():
    return render_template('htmlM+/M_Ruby_Life_Pools.html')
@app.route("/M_The_Azure_Vault") #Flask路由指向 網址的根目錄
def M_The_Azure_Vault():
    return render_template('htmlM+/M_The_Azure_Vault.html')
@app.route("/M_The_Nokhud_Offensive") #Flask路由指向 網址的根目錄
def M_The_Nokhud_Offensive():
    return render_template('htmlM+/M_The_Nokhud_Offensive.html')
@app.route("/M_Shadowmoon_Burial_Grounds") #Flask路由指向 網址的根目錄
def M_Shadowmoon_Burial_Grounds():
    return render_template('htmlM+/M_Shadowmoon_Burial_Grounds.html')
@app.route("/M_Temple_of_the_Jade_Serpent") #Flask路由指向 網址的根目錄
def M_Temple_of_the_Jade_Serpent():
    return render_template('htmlM+/M_Temple_of_the_Jade_Serpent.html')
@app.route("/M_Court_of_Stars") #Flask路由指向 網址的根目錄
def M_Court_of_Stars():
    return render_template('htmlM+/M_Court_of_Stars.html')
@app.route("/M_Halls_of_Valor") #Flask路由指向 網址的根目錄
def M_Halls_of_Valor():
    return render_template('htmlM+/M_Halls_of_Valor.html')

if __name__ == '__main__':
    app.debug = True #開啟DEBUG模式 
    app.run()