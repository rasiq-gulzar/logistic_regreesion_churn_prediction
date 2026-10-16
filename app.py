from flask import Flask, render_template, request
import pickle as pkl

with open('model.pkl','rb') as f:
    model=pkl.load(f)
    
with open('le1.pkl','rb') as f:
    le1=pkl.load(f)
    
with open('le2.pkl','rb') as f:
    le2=pkl.load(f)
    
app=Flask(__name__)

#credit_score	country	gender	age	tenure	balance	
# products_number	credit_card	active_member	estimated_salary
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        cs=int(request.form['credit_score'])
        country=request.form['country']
        gender=request.form['gender']
        age=float(request.form['age'])
        t=float(request.form['tenure'])
        bal=float(request.form['balance'])
        pm=float(request.form['products_number'])
        cc=float(request.form['credit_card'])
        am=float(request.form['active_member'])
        e_sal=float(request.form['estimated_salary'])
        input_data=[[cs,country,gender,age,t,bal,pm,cc,am,e_sal]]
        input_data[0][1]=le1.transform([input_data[0][1]])[0]
        input_data[0][2]=le2.transform([input_data[0][2]])[0]
        
        result=model.predict(input_data)
        return render_template('index.html',prediction=result)
    else:
        return render_template('index.html')
    
if __name__=='__main__':
    app.run(debug=True)