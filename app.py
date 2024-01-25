from flask import Flask, render_template, request, url_for
app=Flask(__name__)

@app.route('/')
def basic():
    return '<h1> Hello there, welcome to my "profile" home page. </h1>'


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/user/<username>')
def user(username):
    return render_template('user.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        #for data processing 
        return render_template('thankyou.html', name=name, email=email)
    return render_template('form.html')
if __name__=='__main__':
    app.run(debug=True)
    


"""from flask import Flask, render_template, request
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # Handle the POST request data if needed
        return render_template('about.html', message='POST request received!')
    return render_template('about.html', message='Welcome to the About page!') """