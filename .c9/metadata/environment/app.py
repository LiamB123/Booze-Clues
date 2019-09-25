{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os \nfrom flask import Flask, render_template , redirect , request , url_for\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\n\napp = Flask(__name__)\n\napp.config[\"MONGO_DBNAME\"] = 'drinks'\napp.config[\"MONGO_URI\"] = os.environ.get('MONGO_URI')\n\nmongo = PyMongo(app)\n\n\n@app.route('/')\n\n@app.route('/home')\ndef home():\n    return render_template(\"home.html\")\n\n\n@app.route('/get_recipes')\ndef get_recipes():\n    return render_template(\"recipes.html\", drinks_list=mongo.db.drinks_list.find())\n    \n    \n@app.route('/add_recipe')\ndef add_recipe():\n    return render_template('add_recipe.html', spirits=mongo.db.spirits.find())\n    \n@app.route('/insert_recipe', methods=['POST'])\ndef insert_recipe():\n    drinks_list=mongo.db.drinks_list\n    drinks_list.insert_one(request.form.to_dict())\n    return redirect(url_for('get_recipes'))\n    \n    \n@app.route('/edit_recipe/<recipe_id>')\ndef edit_recipe(recipe_id):\n    the_recipe =  mongo.db.drinks_list.find_one({\"_id\": ObjectId(recipe_id)})\n    all_spirits =  mongo.db.spirits.find()\n    return render_template('edit_recipe.html', drinks_list=the_recipe,\n                           spirit=all_spirits)\n                           \n                         \n@app.route('/update_recipe/<recipe_id>', methods=['POST'])\ndef update_recipe(recipe_id):\n    drinks_list=mongo.db.drinks_list\n    drinks_list.update({'_id':ObjectId(recipe_id)},\n    {\n        'name':request.form.get('name'),\n        'base_spirit':request.form.get('base_spirit'),\n        'equipment': request.form.get('equipment'),\n        'ingredients': request.form.get('ingredients'),\n        'method':request.form.get('method')\n    })\n    return redirect (url_for('get_recipes'))\n    \n@app.route('/about')\ndef about():\n    return render_template('about.html')\n\n    \nif __name__ == '__main__':\n    app.run(host=os.environ.get('IP'),\n            port=int(os.environ.get('PORT')),\n            debug=True)","undoManager":{"mark":98,"position":100,"stack":[[{"start":{"row":45,"column":28},"end":{"row":45,"column":35},"action":"remove","lines":["recipe_"],"id":501},{"start":{"row":45,"column":28},"end":{"row":45,"column":37},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":45,"column":40},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":502},{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"insert","lines":["d"]},{"start":{"row":46,"column":1},"end":{"row":46,"column":2},"action":"insert","lines":["e"]},{"start":{"row":46,"column":2},"end":{"row":46,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":46,"column":3},"end":{"row":46,"column":4},"action":"insert","lines":[" "],"id":503},{"start":{"row":46,"column":4},"end":{"row":46,"column":5},"action":"insert","lines":["u"]},{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"insert","lines":["p"]},{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"insert","lines":["d"]},{"start":{"row":46,"column":7},"end":{"row":46,"column":8},"action":"insert","lines":["a"]}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"remove","lines":["upda"],"id":504},{"start":{"row":46,"column":4},"end":{"row":46,"column":17},"action":"insert","lines":["update_recipe"]}],[{"start":{"row":46,"column":17},"end":{"row":46,"column":19},"action":"insert","lines":["()"],"id":505}],[{"start":{"row":46,"column":19},"end":{"row":46,"column":20},"action":"insert","lines":[":"],"id":506}],[{"start":{"row":46,"column":20},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":507},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":["r"],"id":508},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["e"]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["t"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["u"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":9},"action":"remove","lines":["retur"],"id":509},{"start":{"row":47,"column":4},"end":{"row":47,"column":10},"action":"insert","lines":["return"]}],[{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":[" "],"id":510},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["r"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["e"]},{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["n"]},{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":15},"action":"remove","lines":["rend"],"id":511},{"start":{"row":47,"column":11},"end":{"row":47,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":47,"column":26},"end":{"row":47,"column":28},"action":"insert","lines":["()"],"id":512}],[{"start":{"row":45,"column":39},"end":{"row":45,"column":40},"action":"insert","lines":[" "],"id":513},{"start":{"row":45,"column":40},"end":{"row":45,"column":41},"action":"insert","lines":["m"]},{"start":{"row":45,"column":41},"end":{"row":45,"column":42},"action":"insert","lines":["e"]},{"start":{"row":45,"column":42},"end":{"row":45,"column":43},"action":"insert","lines":["t"]},{"start":{"row":45,"column":43},"end":{"row":45,"column":44},"action":"insert","lines":["h"]},{"start":{"row":45,"column":44},"end":{"row":45,"column":45},"action":"insert","lines":["o"]},{"start":{"row":45,"column":45},"end":{"row":45,"column":46},"action":"insert","lines":["d"]}],[{"start":{"row":45,"column":40},"end":{"row":45,"column":46},"action":"remove","lines":["method"],"id":514},{"start":{"row":45,"column":40},"end":{"row":45,"column":47},"action":"insert","lines":["methods"]}],[{"start":{"row":45,"column":47},"end":{"row":45,"column":48},"action":"insert","lines":["="],"id":515}],[{"start":{"row":45,"column":48},"end":{"row":45,"column":50},"action":"insert","lines":["[]"],"id":516}],[{"start":{"row":45,"column":49},"end":{"row":45,"column":51},"action":"insert","lines":["''"],"id":517}],[{"start":{"row":45,"column":50},"end":{"row":45,"column":51},"action":"insert","lines":["P"],"id":518},{"start":{"row":45,"column":51},"end":{"row":45,"column":52},"action":"insert","lines":["O"]},{"start":{"row":45,"column":52},"end":{"row":45,"column":53},"action":"insert","lines":["S"]},{"start":{"row":45,"column":53},"end":{"row":45,"column":54},"action":"insert","lines":["T"]}],[{"start":{"row":46,"column":18},"end":{"row":46,"column":19},"action":"insert","lines":["r"],"id":519},{"start":{"row":46,"column":19},"end":{"row":46,"column":20},"action":"insert","lines":["e"]},{"start":{"row":46,"column":20},"end":{"row":46,"column":21},"action":"insert","lines":["c"]},{"start":{"row":46,"column":21},"end":{"row":46,"column":22},"action":"insert","lines":["i"]},{"start":{"row":46,"column":22},"end":{"row":46,"column":23},"action":"insert","lines":["p"]},{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":46,"column":18},"end":{"row":46,"column":24},"action":"remove","lines":["recipe"],"id":520},{"start":{"row":46,"column":18},"end":{"row":46,"column":27},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":46,"column":29},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":521},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":29},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":522},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":36},"action":"insert","lines":["drinks_list=mongo.db.drinks_list"],"id":523}],[{"start":{"row":47,"column":36},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":524},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":4},"end":{"row":48,"column":5},"action":"insert","lines":["d"]},{"start":{"row":48,"column":5},"end":{"row":48,"column":6},"action":"insert","lines":["r"]},{"start":{"row":48,"column":6},"end":{"row":48,"column":7},"action":"insert","lines":["i"]},{"start":{"row":48,"column":7},"end":{"row":48,"column":8},"action":"insert","lines":["n"]},{"start":{"row":48,"column":8},"end":{"row":48,"column":9},"action":"insert","lines":["k"]},{"start":{"row":48,"column":9},"end":{"row":48,"column":10},"action":"insert","lines":["s"]}],[{"start":{"row":48,"column":4},"end":{"row":48,"column":10},"action":"remove","lines":["drinks"],"id":525},{"start":{"row":48,"column":4},"end":{"row":48,"column":15},"action":"insert","lines":["drinks_list"]}],[{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"insert","lines":["."],"id":526},{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"insert","lines":["u"]},{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"insert","lines":["p"]},{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"insert","lines":["d"]},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"insert","lines":["a"]},{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":["t"]},{"start":{"row":48,"column":21},"end":{"row":48,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":22},"end":{"row":48,"column":24},"action":"insert","lines":["()"],"id":527}],[{"start":{"row":48,"column":23},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":528},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":48,"column":23},"end":{"row":48,"column":25},"action":"insert","lines":["[]"],"id":529}],[{"start":{"row":48,"column":24},"end":{"row":48,"column":26},"action":"insert","lines":["''"],"id":530}],[{"start":{"row":48,"column":25},"end":{"row":48,"column":26},"action":"insert","lines":["_"],"id":531},{"start":{"row":48,"column":26},"end":{"row":48,"column":27},"action":"insert","lines":["i"]},{"start":{"row":48,"column":27},"end":{"row":48,"column":28},"action":"insert","lines":["d"]}],[{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"insert","lines":[":"],"id":532},{"start":{"row":48,"column":30},"end":{"row":48,"column":31},"action":"insert","lines":["O"]},{"start":{"row":48,"column":31},"end":{"row":48,"column":32},"action":"insert","lines":["b"]}],[{"start":{"row":48,"column":30},"end":{"row":48,"column":32},"action":"remove","lines":["Ob"],"id":533},{"start":{"row":48,"column":30},"end":{"row":48,"column":38},"action":"insert","lines":["ObjectId"]}],[{"start":{"row":48,"column":38},"end":{"row":48,"column":40},"action":"insert","lines":["()"],"id":534}],[{"start":{"row":48,"column":39},"end":{"row":48,"column":40},"action":"insert","lines":["r"],"id":535},{"start":{"row":48,"column":40},"end":{"row":48,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":39},"end":{"row":48,"column":41},"action":"remove","lines":["re"],"id":536},{"start":{"row":48,"column":39},"end":{"row":48,"column":48},"action":"insert","lines":["recipe_id"]}],[{"start":{"row":48,"column":49},"end":{"row":48,"column":50},"action":"remove","lines":["]"],"id":537}],[{"start":{"row":48,"column":49},"end":{"row":48,"column":50},"action":"insert","lines":["}"],"id":538}],[{"start":{"row":48,"column":23},"end":{"row":48,"column":24},"action":"remove","lines":["["],"id":539}],[{"start":{"row":48,"column":23},"end":{"row":48,"column":24},"action":"insert","lines":["{"],"id":540}],[{"start":{"row":48,"column":50},"end":{"row":48,"column":51},"action":"insert","lines":[","],"id":541}],[{"start":{"row":48,"column":51},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":542},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":49,"column":4},"end":{"row":49,"column":5},"action":"insert","lines":["{"],"id":543},{"start":{"row":49,"column":5},"end":{"row":49,"column":6},"action":"insert","lines":["}"]}],[{"start":{"row":49,"column":5},"end":{"row":51,"column":4},"action":"insert","lines":["","        ","    "],"id":544}],[{"start":{"row":50,"column":8},"end":{"row":50,"column":9},"action":"insert","lines":["t"],"id":545},{"start":{"row":50,"column":9},"end":{"row":50,"column":10},"action":"insert","lines":["a"]},{"start":{"row":50,"column":10},"end":{"row":50,"column":11},"action":"insert","lines":["k"]},{"start":{"row":50,"column":11},"end":{"row":50,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":50,"column":11},"end":{"row":50,"column":12},"action":"remove","lines":["s"],"id":546},{"start":{"row":50,"column":10},"end":{"row":50,"column":11},"action":"remove","lines":["k"]}],[{"start":{"row":50,"column":10},"end":{"row":50,"column":11},"action":"insert","lines":["s"],"id":547},{"start":{"row":50,"column":11},"end":{"row":50,"column":12},"action":"insert","lines":["k"]}],[{"start":{"row":50,"column":11},"end":{"row":50,"column":12},"action":"remove","lines":["k"],"id":548},{"start":{"row":50,"column":10},"end":{"row":50,"column":11},"action":"remove","lines":["s"]},{"start":{"row":50,"column":9},"end":{"row":50,"column":10},"action":"remove","lines":["a"]},{"start":{"row":50,"column":8},"end":{"row":50,"column":9},"action":"remove","lines":["t"]}],[{"start":{"row":50,"column":8},"end":{"row":54,"column":49},"action":"insert","lines":["'task_name':request.form.get('task_name'),","        'category_name':request.form.get('category_name'),","        'task_description': request.form.get('task_description'),","        'due_date': request.form.get('due_date'),","        'is_urgent':request.form.get('is_urgent')"],"id":549}],[{"start":{"row":50,"column":13},"end":{"row":50,"column":14},"action":"remove","lines":["_"],"id":550},{"start":{"row":50,"column":12},"end":{"row":50,"column":13},"action":"remove","lines":["k"]},{"start":{"row":50,"column":11},"end":{"row":50,"column":12},"action":"remove","lines":["s"]},{"start":{"row":50,"column":10},"end":{"row":50,"column":11},"action":"remove","lines":["a"]},{"start":{"row":50,"column":9},"end":{"row":50,"column":10},"action":"remove","lines":["t"]}],[{"start":{"row":50,"column":37},"end":{"row":50,"column":38},"action":"remove","lines":["_"],"id":551},{"start":{"row":50,"column":36},"end":{"row":50,"column":37},"action":"remove","lines":["k"]},{"start":{"row":50,"column":35},"end":{"row":50,"column":36},"action":"remove","lines":["s"]},{"start":{"row":50,"column":34},"end":{"row":50,"column":35},"action":"remove","lines":["a"]},{"start":{"row":50,"column":33},"end":{"row":50,"column":34},"action":"remove","lines":["t"]}],[{"start":{"row":51,"column":10},"end":{"row":51,"column":23},"action":"remove","lines":["ategory_name'"],"id":552},{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"remove","lines":["c"]}],[{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"insert","lines":["m"],"id":553},{"start":{"row":51,"column":10},"end":{"row":51,"column":11},"action":"insert","lines":["e"]},{"start":{"row":51,"column":11},"end":{"row":51,"column":12},"action":"insert","lines":["t"]},{"start":{"row":51,"column":12},"end":{"row":51,"column":13},"action":"insert","lines":["h"]},{"start":{"row":51,"column":13},"end":{"row":51,"column":14},"action":"insert","lines":["j"]}],[{"start":{"row":51,"column":13},"end":{"row":51,"column":14},"action":"remove","lines":["j"],"id":554},{"start":{"row":51,"column":12},"end":{"row":51,"column":13},"action":"remove","lines":["h"]},{"start":{"row":51,"column":11},"end":{"row":51,"column":12},"action":"remove","lines":["t"]},{"start":{"row":51,"column":10},"end":{"row":51,"column":11},"action":"remove","lines":["e"]},{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"remove","lines":["m"]}],[{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"insert","lines":["b"],"id":555},{"start":{"row":51,"column":10},"end":{"row":51,"column":11},"action":"insert","lines":["a"]},{"start":{"row":51,"column":11},"end":{"row":51,"column":12},"action":"insert","lines":["s"]},{"start":{"row":51,"column":12},"end":{"row":51,"column":13},"action":"insert","lines":["e"]},{"start":{"row":51,"column":13},"end":{"row":51,"column":14},"action":"insert","lines":["_"]},{"start":{"row":51,"column":14},"end":{"row":51,"column":15},"action":"insert","lines":["s"]},{"start":{"row":51,"column":15},"end":{"row":51,"column":16},"action":"insert","lines":["p"]}],[{"start":{"row":51,"column":16},"end":{"row":51,"column":17},"action":"insert","lines":["i"],"id":556},{"start":{"row":51,"column":17},"end":{"row":51,"column":18},"action":"insert","lines":["r"]},{"start":{"row":51,"column":18},"end":{"row":51,"column":19},"action":"insert","lines":["i"]},{"start":{"row":51,"column":19},"end":{"row":51,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":51,"column":20},"end":{"row":51,"column":21},"action":"insert","lines":[";"],"id":557}],[{"start":{"row":51,"column":20},"end":{"row":51,"column":21},"action":"remove","lines":[";"],"id":558}],[{"start":{"row":51,"column":20},"end":{"row":51,"column":21},"action":"insert","lines":["'"],"id":559}],[{"start":{"row":51,"column":40},"end":{"row":51,"column":53},"action":"remove","lines":["category_name"],"id":560},{"start":{"row":51,"column":40},"end":{"row":51,"column":41},"action":"insert","lines":["b"]},{"start":{"row":51,"column":41},"end":{"row":51,"column":42},"action":"insert","lines":["a"]},{"start":{"row":51,"column":42},"end":{"row":51,"column":43},"action":"insert","lines":["e"]}],[{"start":{"row":51,"column":42},"end":{"row":51,"column":43},"action":"remove","lines":["e"],"id":561}],[{"start":{"row":51,"column":42},"end":{"row":51,"column":43},"action":"insert","lines":["s"],"id":562},{"start":{"row":51,"column":43},"end":{"row":51,"column":44},"action":"insert","lines":["e"]},{"start":{"row":51,"column":44},"end":{"row":51,"column":45},"action":"insert","lines":[")"]},{"start":{"row":51,"column":45},"end":{"row":51,"column":46},"action":"insert","lines":["_"]}],[{"start":{"row":51,"column":45},"end":{"row":51,"column":46},"action":"remove","lines":["_"],"id":563},{"start":{"row":51,"column":44},"end":{"row":51,"column":45},"action":"remove","lines":[")"]}],[{"start":{"row":51,"column":44},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":564},{"start":{"row":52,"column":0},"end":{"row":52,"column":8},"action":"insert","lines":["        "]},{"start":{"row":52,"column":8},"end":{"row":52,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":52,"column":8},"end":{"row":52,"column":9},"action":"remove","lines":["_"],"id":565},{"start":{"row":52,"column":4},"end":{"row":52,"column":8},"action":"remove","lines":["    "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":4},"action":"remove","lines":["    "]},{"start":{"row":51,"column":44},"end":{"row":52,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":51,"column":44},"end":{"row":51,"column":45},"action":"insert","lines":["_"],"id":566},{"start":{"row":51,"column":45},"end":{"row":51,"column":46},"action":"insert","lines":["s"]},{"start":{"row":51,"column":46},"end":{"row":51,"column":47},"action":"insert","lines":["p"]},{"start":{"row":51,"column":47},"end":{"row":51,"column":48},"action":"insert","lines":["i"]},{"start":{"row":51,"column":48},"end":{"row":51,"column":49},"action":"insert","lines":["r"]},{"start":{"row":51,"column":49},"end":{"row":51,"column":50},"action":"insert","lines":["i"]},{"start":{"row":51,"column":50},"end":{"row":51,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":52,"column":9},"end":{"row":52,"column":25},"action":"remove","lines":["task_description"],"id":567},{"start":{"row":52,"column":9},"end":{"row":52,"column":10},"action":"insert","lines":["e"]},{"start":{"row":52,"column":10},"end":{"row":52,"column":11},"action":"insert","lines":["q"]},{"start":{"row":52,"column":11},"end":{"row":52,"column":12},"action":"insert","lines":["u"]},{"start":{"row":52,"column":12},"end":{"row":52,"column":13},"action":"insert","lines":["i"]},{"start":{"row":52,"column":13},"end":{"row":52,"column":14},"action":"insert","lines":["p"]},{"start":{"row":52,"column":14},"end":{"row":52,"column":15},"action":"insert","lines":["m"]},{"start":{"row":52,"column":15},"end":{"row":52,"column":16},"action":"insert","lines":["e"]},{"start":{"row":52,"column":16},"end":{"row":52,"column":17},"action":"insert","lines":["n"]},{"start":{"row":52,"column":17},"end":{"row":52,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":53,"column":9},"end":{"row":53,"column":17},"action":"remove","lines":["due_date"],"id":568},{"start":{"row":53,"column":9},"end":{"row":53,"column":10},"action":"insert","lines":["i"]},{"start":{"row":53,"column":10},"end":{"row":53,"column":11},"action":"insert","lines":["n"]},{"start":{"row":53,"column":11},"end":{"row":53,"column":12},"action":"insert","lines":["c"]}],[{"start":{"row":53,"column":11},"end":{"row":53,"column":12},"action":"remove","lines":["c"],"id":569}],[{"start":{"row":53,"column":11},"end":{"row":53,"column":12},"action":"insert","lines":["g"],"id":570},{"start":{"row":53,"column":12},"end":{"row":53,"column":13},"action":"insert","lines":["r"]},{"start":{"row":53,"column":13},"end":{"row":53,"column":14},"action":"insert","lines":["e"]},{"start":{"row":53,"column":14},"end":{"row":53,"column":15},"action":"insert","lines":["d"]},{"start":{"row":53,"column":15},"end":{"row":53,"column":16},"action":"insert","lines":["i"]},{"start":{"row":53,"column":16},"end":{"row":53,"column":17},"action":"insert","lines":["e"]},{"start":{"row":53,"column":17},"end":{"row":53,"column":18},"action":"insert","lines":["n"]},{"start":{"row":53,"column":18},"end":{"row":53,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":54,"column":9},"end":{"row":54,"column":18},"action":"remove","lines":["is_urgent"],"id":571},{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"insert","lines":["m"]},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["e"]},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"insert","lines":["t"]},{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":["h"]},{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"insert","lines":["o"]},{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":52,"column":39},"end":{"row":52,"column":55},"action":"remove","lines":["task_description"],"id":572},{"start":{"row":52,"column":39},"end":{"row":52,"column":47},"action":"insert","lines":["quipment"]}],[{"start":{"row":52,"column":39},"end":{"row":52,"column":40},"action":"insert","lines":["w"],"id":573}],[{"start":{"row":52,"column":39},"end":{"row":52,"column":40},"action":"remove","lines":["w"],"id":574}],[{"start":{"row":52,"column":39},"end":{"row":52,"column":40},"action":"insert","lines":["e"],"id":575}],[{"start":{"row":53,"column":40},"end":{"row":53,"column":48},"action":"remove","lines":["due_date"],"id":576},{"start":{"row":53,"column":40},"end":{"row":53,"column":50},"action":"insert","lines":["ingredient"]}],[{"start":{"row":53,"column":50},"end":{"row":53,"column":51},"action":"insert","lines":["s"],"id":577}],[{"start":{"row":53,"column":19},"end":{"row":53,"column":20},"action":"insert","lines":["s"],"id":578}],[{"start":{"row":54,"column":35},"end":{"row":54,"column":44},"action":"remove","lines":["is_urgent"],"id":579},{"start":{"row":54,"column":35},"end":{"row":54,"column":36},"action":"insert","lines":["n"]},{"start":{"row":54,"column":36},"end":{"row":54,"column":37},"action":"insert","lines":["e"]},{"start":{"row":54,"column":37},"end":{"row":54,"column":38},"action":"insert","lines":["t"]},{"start":{"row":54,"column":38},"end":{"row":54,"column":39},"action":"insert","lines":["h"]},{"start":{"row":54,"column":39},"end":{"row":54,"column":40},"action":"insert","lines":["i"]},{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"insert","lines":["d"]}],[{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"remove","lines":["d"],"id":580},{"start":{"row":54,"column":39},"end":{"row":54,"column":40},"action":"remove","lines":["i"]},{"start":{"row":54,"column":38},"end":{"row":54,"column":39},"action":"remove","lines":["h"]},{"start":{"row":54,"column":37},"end":{"row":54,"column":38},"action":"remove","lines":["t"]},{"start":{"row":54,"column":36},"end":{"row":54,"column":37},"action":"remove","lines":["e"]},{"start":{"row":54,"column":35},"end":{"row":54,"column":36},"action":"remove","lines":["n"]}],[{"start":{"row":54,"column":35},"end":{"row":54,"column":36},"action":"insert","lines":["m"],"id":581},{"start":{"row":54,"column":36},"end":{"row":54,"column":37},"action":"insert","lines":["e"]},{"start":{"row":54,"column":37},"end":{"row":54,"column":38},"action":"insert","lines":["t"]},{"start":{"row":54,"column":38},"end":{"row":54,"column":39},"action":"insert","lines":["h"]},{"start":{"row":54,"column":39},"end":{"row":54,"column":40},"action":"insert","lines":["o"]},{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"insert","lines":["d"]}],[{"start":{"row":56,"column":4},"end":{"row":56,"column":8},"action":"remove","lines":["    "],"id":582},{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"remove","lines":["    "]},{"start":{"row":55,"column":5},"end":{"row":56,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":57,"column":12},"end":{"row":57,"column":28},"action":"remove","lines":["ender_template()"],"id":583},{"start":{"row":57,"column":12},"end":{"row":57,"column":13},"action":"insert","lines":["r"]},{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"insert","lines":["e"]},{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"insert","lines":["d"]},{"start":{"row":57,"column":15},"end":{"row":57,"column":16},"action":"insert","lines":["i"]},{"start":{"row":57,"column":16},"end":{"row":57,"column":17},"action":"insert","lines":["r"]},{"start":{"row":57,"column":17},"end":{"row":57,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":57,"column":17},"end":{"row":57,"column":18},"action":"remove","lines":["e"],"id":584},{"start":{"row":57,"column":16},"end":{"row":57,"column":17},"action":"remove","lines":["r"]},{"start":{"row":57,"column":15},"end":{"row":57,"column":16},"action":"remove","lines":["i"]},{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"remove","lines":["d"]},{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"remove","lines":["e"]},{"start":{"row":57,"column":12},"end":{"row":57,"column":13},"action":"remove","lines":["r"]}],[{"start":{"row":57,"column":12},"end":{"row":57,"column":13},"action":"insert","lines":["e"],"id":585},{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":57,"column":11},"end":{"row":57,"column":14},"action":"remove","lines":["red"],"id":586},{"start":{"row":57,"column":11},"end":{"row":57,"column":19},"action":"insert","lines":["redirect"]}],[{"start":{"row":57,"column":19},"end":{"row":57,"column":21},"action":"insert","lines":["()"],"id":587}],[{"start":{"row":57,"column":20},"end":{"row":57,"column":22},"action":"insert","lines":["''"],"id":588}],[{"start":{"row":57,"column":21},"end":{"row":57,"column":22},"action":"insert","lines":["g"],"id":589},{"start":{"row":57,"column":22},"end":{"row":57,"column":23},"action":"insert","lines":["e"]},{"start":{"row":57,"column":23},"end":{"row":57,"column":24},"action":"insert","lines":["t"]},{"start":{"row":57,"column":24},"end":{"row":57,"column":25},"action":"insert","lines":["_"]},{"start":{"row":57,"column":25},"end":{"row":57,"column":26},"action":"insert","lines":["r"]},{"start":{"row":57,"column":26},"end":{"row":57,"column":27},"action":"insert","lines":["e"]},{"start":{"row":57,"column":27},"end":{"row":57,"column":28},"action":"insert","lines":["c"]},{"start":{"row":57,"column":28},"end":{"row":57,"column":29},"action":"insert","lines":["i"]}],[{"start":{"row":57,"column":29},"end":{"row":57,"column":30},"action":"insert","lines":["p"],"id":590},{"start":{"row":57,"column":30},"end":{"row":57,"column":31},"action":"insert","lines":["e"]},{"start":{"row":57,"column":31},"end":{"row":57,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":57,"column":19},"end":{"row":57,"column":20},"action":"insert","lines":[" "],"id":591},{"start":{"row":57,"column":20},"end":{"row":57,"column":21},"action":"insert","lines":["u"]},{"start":{"row":57,"column":21},"end":{"row":57,"column":22},"action":"insert","lines":["r"]},{"start":{"row":57,"column":22},"end":{"row":57,"column":23},"action":"insert","lines":["l"]},{"start":{"row":57,"column":23},"end":{"row":57,"column":24},"action":"insert","lines":["_"]},{"start":{"row":57,"column":24},"end":{"row":57,"column":25},"action":"insert","lines":["f"]}],[{"start":{"row":57,"column":25},"end":{"row":57,"column":26},"action":"insert","lines":["o"],"id":592},{"start":{"row":57,"column":26},"end":{"row":57,"column":27},"action":"insert","lines":["r"]},{"start":{"row":57,"column":27},"end":{"row":57,"column":28},"action":"insert","lines":[")"]}],[{"start":{"row":57,"column":27},"end":{"row":57,"column":28},"action":"remove","lines":[")"],"id":593}],[{"start":{"row":57,"column":20},"end":{"row":57,"column":21},"action":"insert","lines":["("],"id":594}],[{"start":{"row":57,"column":43},"end":{"row":58,"column":0},"action":"insert","lines":["",""],"id":595},{"start":{"row":58,"column":0},"end":{"row":58,"column":4},"action":"insert","lines":["    "]},{"start":{"row":58,"column":4},"end":{"row":59,"column":0},"action":"insert","lines":["",""]},{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"insert","lines":["    "]},{"start":{"row":59,"column":4},"end":{"row":59,"column":5},"action":"insert","lines":["0"]}],[{"start":{"row":59,"column":4},"end":{"row":59,"column":5},"action":"remove","lines":["0"],"id":596},{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"remove","lines":["    "]},{"start":{"row":58,"column":4},"end":{"row":59,"column":0},"action":"remove","lines":["",""]},{"start":{"row":58,"column":0},"end":{"row":58,"column":4},"action":"remove","lines":["    "]},{"start":{"row":57,"column":43},"end":{"row":58,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":57,"column":43},"end":{"row":57,"column":44},"action":"insert","lines":[")"],"id":597}],[{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"remove","lines":["    "],"id":598},{"start":{"row":55,"column":6},"end":{"row":56,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":45,"column":39},"end":{"row":45,"column":40},"action":"insert","lines":[","],"id":599}],[{"start":{"row":44,"column":25},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":600},{"start":{"row":45,"column":0},"end":{"row":45,"column":25},"action":"insert","lines":["                         "]}],[{"start":{"row":45,"column":24},"end":{"row":45,"column":25},"action":"remove","lines":[" "],"id":601},{"start":{"row":45,"column":20},"end":{"row":45,"column":24},"action":"remove","lines":["    "]},{"start":{"row":45,"column":16},"end":{"row":45,"column":20},"action":"remove","lines":["    "]},{"start":{"row":45,"column":12},"end":{"row":45,"column":16},"action":"remove","lines":["    "]},{"start":{"row":45,"column":8},"end":{"row":45,"column":12},"action":"remove","lines":["    "]},{"start":{"row":45,"column":4},"end":{"row":45,"column":8},"action":"remove","lines":["    "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"remove","lines":["    "]},{"start":{"row":44,"column":25},"end":{"row":45,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":398.5,"scrollleft":0,"selection":{"start":{"row":44,"column":25},"end":{"row":44,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":23,"state":"start","mode":"ace/mode/python"}},"timestamp":1569417507011}