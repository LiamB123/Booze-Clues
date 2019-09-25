import os 
from flask import Flask, render_template , redirect , request , url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'drinks'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", drinks_list=mongo.db.drinks_list.find())
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', spirits=mongo.db.spirits.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    drinks_list=mongo.db.drinks_list
    drinks_list.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.drinks_list.find_one({"_id": ObjectId(recipe_id)})
    all_spirits =  mongo.db.spirits.find()
    return render_template('edit_recipe.html', drinks_list=the_recipe,
                           spirits=all_spirits)
    
@app.route('/about')
def about():
    return render_template('about.html')

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)