from app_logic import setFirstValue, setSecondValue, getAddition
from utils import parse_post, render_template

def addnumbers(environ):
    num1, num2, result = "", "", ""
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = parse_post(environ)
        num1 = data.get("first_value", [""])[0]
        num2 = data.get("second_value", [""])[0]
        num1=setFirstValue(num1)
        num2=setSecondValue(num2)
        result=getAddition(num1,num2)
    return render_template("boundaries/addnumber.html",result=result,first_value=num1,second_value=num2)