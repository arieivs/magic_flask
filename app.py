from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.get('/potions/')
def potions_index():
    #TODO get information from all potions in the database
    potions = [
        {'id': 1, 'name': 'Amortentia', 'purpose': "The world's strongest Love Potion; does not create real love, just powerful obsession.", 'preparation_time': '2 hours'},
        {'id': 2, 'name': 'Draught of Living Death', 'purpose': "Brings upon its drinker a very powerful sleep that can last indefinitely.", 'preparation_time': '1 hour'},
        {'id': 3, 'name': 'Elixir of Life', 'purpose': "Immortality, if consumed on a regular basis; yet it does not prevent aging.", 'preparation_time': '3 hours'},
        {'id': 4, 'name': 'Felix Felicis', 'purpose': "Liquid luck, bottled good fortune.", 'preparation_time': '6 months'},
        {'id': 5, 'name': 'Mandrake Restorative Draught', 'purpose': "Restores an individual who has been cursed or transfigured; only known cure to petrification.", 'preparation_time': '1 hour'},
        {'id': 6, 'name': 'Polyjuice Potion', 'purpose': 'Allows the drinker to temporarily assume the physical form of someone else.', 'preparation_time': '1 month'},
        {'id': 7, 'name': 'Skele-gro', 'purpose': 'Restores and regrows bones.', 'preparation_time': '1 hour'},
        {'id': 8, 'name': 'Veritaserum', 'purpose': 'Forces the drinker to tell the truth.', 'preparation_time': '28 days'},
        {'id': 9, 'name': 'Wolfsbane', 'purpose': 'Relieves, but does not cure, the symptoms of lycanthropy, allowing the drinker to hold on to their mental faculties after transformation.', 'preparation_time': '3 hours'}
    ]
    return render_template('potions_index.html', potions=potions)

@app.get('/potions/<int:potion_id>/')
def potion_detail(potion_id):
    #TODO go get information from this potion in the database
    potions = [
        {'id': 1, 'name': 'Amortentia', 'purpose': "The world's strongest Love Potion; does not create real love, just powerful obsession.", 'preparation_time': '2 hours'},
        {'id': 2, 'name': 'Draught of Living Death', 'purpose': "Brings upon its drinker a very powerful sleep that can last indefinitely.", 'preparation_time': '1 hour'},
        {'id': 3, 'name': 'Elixir of Life', 'purpose': "Immortality, if consumed on a regular basis; yet it does not prevent aging.", 'preparation_time': '3 hours'},
        {'id': 4, 'name': 'Felix Felicis', 'purpose': "Liquid luck, bottled good fortune.", 'preparation_time': '6 months'},
        {'id': 5, 'name': 'Mandrake Restorative Draught', 'purpose': "Restores an individual who has been cursed or transfigured; only known cure to petrification.", 'preparation_time': '1 hour'},
        {'id': 6, 'name': 'Polyjuice Potion', 'purpose': 'Allows the drinker to temporarily assume the physical form of someone else.', 'preparation_time': '1 month'},
        {'id': 7, 'name': 'Skele-gro', 'purpose': 'Restores and regrows bones.', 'preparation_time': '1 hour'},
        {'id': 8, 'name': 'Veritaserum', 'purpose': 'Forces the drinker to tell the truth.', 'preparation_time': '28 days'},
        {'id': 9, 'name': 'Wolfsbane', 'purpose': 'Relieves, but does not cure, the symptoms of lycanthropy, allowing the drinker to hold on to their mental faculties after transformation.', 'preparation_time': '3 hours'}
    ]
    #try:
    potion = [candidate for candidate in potions if candidate['id'] == potion_id][0]
    #except IndexError:
    #TODO show 404
    return render_template('potion_detail.html', potion=potion)

@app.post('/potions/')
def potions_new():
    #create a new potion in the database with user input
    #no idea what I should return here
    return