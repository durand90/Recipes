from flask_app import app, bcrypt
from flask import render_template, redirect, request, session
from flask_app.models import model_recipes

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/recipes/new') # create a person route
def new_recipes():
    return render_template('/new_user.html') # create a person html page

@app.route('/success')
def success_login():

    if 'uuid' not in session:
        return redirect('/')
    
    
    
    id = session['uuid']
    user = model_recipes.Recipe.get_one({'id': id})

        


    return render_template('/success.html', user = user)

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/recipes/login', methods=['post'])
def recipes_login():

    is_valid = model_recipes.Recipe.validator_login(request.form)     

    if not is_valid:
        return redirect('/')

    return redirect('/')

@app.route('/recipes/create', methods=['post'])
def create_recipes():        # "new person" or "id" is equal(=) to recipes(class name) dot(".") create function with(request.form)



    is_valid = model_recipes.Recipe.validator(request.form)

    if is_valid == False:
        return redirect('/')

    #hash the incoming password

    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    #hash_confirm_pw = bcrypt.generate_password_hash(request.form['confirm_pw'])
    print(hash_pw)
    #print(hash_confirm_pw)

    data = {
        **request.form,
        'pw': hash_pw
    }

    new_user = model_recipes.Recipe.create(data)
    print(new_user)
    session['uuid'] = new_user


    return redirect('/success')

@app.route('/recipes/<int:id>')
def show_recipes(id):
    pass

@app.route('/recipes/<int:id>/edit')
def edit_recipes(id):
    pass

@app.route('/recipes/<int:id>/update', methods=['post'])
def update_recipes(id):
    pass

@app.route('/recipes/<int:id>/delete')
def delete_recipes(id):
    pass
