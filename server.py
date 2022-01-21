from flask import Flask,render_template

app = Flask(__name__)

@app.route('/<int:filas>',methods=['GET'])
def ajedres1(filas):
    return render_template("index.html",num=filas)

@app.route('/<int:filas>/<int:columnas>',methods=['GET'])
def ajedres2(filas,columnas):
    return render_template("index1.html",num=filas,colum=columnas)

@app.route('/<int:filas>/<int:columnas>/<color1>',methods=['GET'])
def ajedres3(filas,columnas,color1):
    return render_template("index2.html",num=filas,colum=columnas, pinta=color1)

@app.route('/<int:filas>/<int:columnas>/<color1>/<color2>',methods=['GET'])
def ajedres4(filas,columnas,color1,color2):
    return render_template("index3.html",num=filas,colum=columnas, pinta=color1,pinta1=color2)


if __name__ == "__main__":
    app.run(debug=True)