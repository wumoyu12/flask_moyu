from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    if request.method == 'GET':
        return render_template('personinfo.html')
    else:
        GetInfo()
        return render_template('personinfo.html')
    
def GetInfo():
    name=request.form.get('txtname')
    email=request.form.get('txtemail')
    print("Hello " + name + ". Thank You for Your email " + email)
    return "Hello " + name + ". Thank You for Your email " + email
if __name__ == "__main__":
    app.run()
