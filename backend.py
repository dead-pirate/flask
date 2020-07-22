from flask import Flask,render_template,request,redirect,url_for,jsonify,make_response
from flask_restful import Resource,Api


app = Flask(__name__)
api = Api(app)


def calculate(m,n,op):
    d=['+','-','*','/','//','^','%']
    if op in d:
        ops={'+':m+n,
             '-':m-n,
             '*':m*n,
             '/':m/n,
             '^':m**n,
             '%':m%n,
             '//':m//n}
        return ops[op]
    else :
        return 'Error'

class Calculator(Resource):


    def get(self):
        # print(request.method)
        # print(request.form)
        # print(request.args)
        try:
            self.m  = int(request.args.get('value1'))
            self.n  = int(request.args.get('value2'))
            self.op = request.args.get('operation')
            self.final = calculate(self.m,self.n,self.op)

            return {'Output': self.final}
        except:
            return make_response(render_template("index.html"))

    def post(self):
        # print(request.method)
        # print(request.form)
        # print(request.args)
        try:
            self.m  = int(request.form.get('value1'))
            self.n  = int(request.form.get('value2'))
            self.op = request.form.get('operation')
        except:
            self.m  = int(request.values.get('value1'))
            self.n  = int(request.values.get('value2'))
            self.op = request.values.get('operation')

        self.final = calculate(self.m,self.n,self.op)


        return {'Output': self.final}



#class home(Resource):
#    def get(self):
#        return render_template("index.html")


api.add_resource(Calculator,"/calc")
#api.add_resource(home,"/")




# @app.route("/")
# def index():
#     return render_template("index.html")


@app.route("/",methods=['POST','GET'])
def result():
    print(request.method)
    print(request.form)
    print(request.args)
    #print(request.get_json())


    if request.method == 'POST':
        m  = int(request.form.get('value1'))
        n  = int(request.form.get('value2'))
        op = request.form.get('operation')
        final = calculate(m,n,op)
        print(final)
        #return jsonify({'result':final})
        return render_template("result.html",solution = final, string = (str(m) + op +str(n)) )

    elif request.method == 'GET':
        flag=False
        for _ in ['value1','value2','operation']:
            if _ not in request.args.keys():
                flag = True

        if not request.args or flag:
            return render_template("index.html")
        else:
            m  = int(request.args.get('value1'))
            n  = int(request.args.get('value2'))
            op = request.args.get('operation')
            final = calculate(m,n,op)
            print(final)
            return render_template("result.html",solution = final, string = (str(m) + op +str(n)))
            #return jsonify({'result':final})

    else:
        return render_template("index.html")


    # return jsonify({'result': final})


def main():
    app.run()

if __name__ == '__main__':
    main()
