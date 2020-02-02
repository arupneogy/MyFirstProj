from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ename=db.Column(db.String(200),nullable=False)

    def __ref__(self):
        return '<Task %r>' %self.id

@app.route('/',methods=['POST','GET'])

def index():
    
    if request.method == 'POST':
        e_name=request.form['ename']
        new_ename=Todo(ename=e_name)
    
        db.session.add(new_ename)
        db.session.commit()
        return redirect('/')
    
        return 'There is some issue'

    else:
        task=Todo.query.order_by(Todo.id).all()
        return render_template('index.html',task=task)
@app.route('/delete/<int:id>')
def delete(id):
    edel=Todo.query.get_or_404(id)
    db.session.delete(edel)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    eupdate=Todo.query.get_or_404(id)
    if request.method == 'POST':
        eupdate.ename=request.form['ename']
        db.session.commit()
        return redirect('/')
    else :
        return render_template('update.html',task=eupdate)  
    

if __name__=="__main__":
    app.run(debug=True)




