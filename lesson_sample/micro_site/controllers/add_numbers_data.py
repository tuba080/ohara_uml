from app_logic import set_first_value, set_second_value, getAddition
from utils import parse_post, render_template

def addnumbers(environ):
    num1, num2, result = "", "", ""
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = parse_post(environ)
        num1=int(data.get("first_value", [0])[0])
        num2=int(data.get("second_value", [0])[0])
        set_first_value(num1)
        set_second_value(num2)
        result=getAddition()
    return render_template("boundaries/addnumber.html",result=result,first_value=num1,second_value=num2)