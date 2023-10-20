from flask import Flask,render_template,request
import requests
app=Flask(__name__)

URL="https://api.mfapi.in/mf/"
list_1=[]

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        Name=request.form.get("Name")
        fund_code=request.form.get("fund_code")
        funds=requests.get(URL+str(fund_code))
        fund_house1=funds.json().get("meta").get("fund_house")
        investment=request.form.get("investment")
        unit_held=request.form.get("unit_held")
        nav=funds.json().get("data")[0].get("nav")

        dict_1={}
        dict_1.update({"Name":Name})
        dict_1.update({"fund_house1":fund_house1})
        dict_1.update({"investment":investment})
        dict_1.update({"unit_held":unit_held})
        dict_1.update({"nav":nav})
        current_value=float(dict_1.get("nav"))*int(dict_1.get("investment"))
        dict_1.update({"current_value":current_value})
        growth=float(dict_1.get("current_value"))-int(dict_1.get("unit_held"))
        dict_1.update({"growth":growth})
        list_1.append(dict_1)

    return render_template("index.html",mf=list_1)

if __name__ == "__main__":
    app.run(debug=True)