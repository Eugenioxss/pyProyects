from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Estrategia básica
basic_strategy = {
    "pair_splitting": {
        "A,A": "Y", "T,T": "N", "9,9": "Y/N", "8,8": "Y", "7,7": "Y/N", 
        "6,6": "Y/N", "5,5": "N", "4,4": "N", "3,3": "Y/N", "2,2": "Y/N"
    },
    "soft_totals": {
        "A,9": "S", "A,8": "S", "A,7": "Ds", "A,6": "H", 
        "A,5": "H", "A,4": "H", "A,3": "H", "A,2": "H"
    },
    "hard_totals": {
        17: "S", 16: "S", 15: "S", 14: "S", 13: "S", 12: "H/S",
        11: "D", 10: "D", 9:  "H/D", 8:  "H"
    },
    "late_surrender": {
        16: ["SUR"], 15: ["SUR"], 14: ["SUR"]
    }
}

# Valores de conteo Hi-Lo
card_values = {
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
    '7': 0, '8': 0, '9': 0,
    '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

# Inicializar el conteo
running_count = 0

def update_count(card):
    global running_count
    if card in card_values:
        running_count += card_values[card]
    return running_count

def basic_strategy_decision(player_hand, dealer_card):
    # Verificar pair splitting
    if player_hand in basic_strategy["pair_splitting"]:
        return basic_strategy["pair_splitting"][player_hand]
    
    # Verificar soft totals
    if player_hand in basic_strategy["soft_totals"]:
        return basic_strategy["soft_totals"][player_hand]
    
    # Verificar hard totals
    if player_hand in basic_strategy["hard_totals"]:
        return basic_strategy["hard_totals"][player_hand]
    
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    decision = None
    count = None
    min_bet = None
    max_bet = None
    if request.method == 'POST':
        min_bet = request.form['min_bet']
        max_bet = request.form['max_bet']
        card = request.form['card']
        player_hand = request.form['player_hand']
        dealer_card = request.form['dealer_card']
        count = update_count(card)
        decision = basic_strategy_decision(player_hand, dealer_card)
    return render_template('index.html', decision=decision, count=count, min_bet=min_bet, max_bet=max_bet)

if __name__ == '__main__':
    app.run(debug=True)