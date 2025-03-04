from flask import Flask, render_template, request, redirect, url_for, session
import math

app = Flask(__name__)
app.secret_key = 'Penesote04.'  # Cambia esto por una clave segura

# Funciones de utilidad

def card_value(card):
    """Devuelve el valor numérico de la carta para el cálculo del total.
       'J','Q','K','10' valen 10, la A se cuenta inicialmente como 11.
    """
    if card in ['J', 'Q', 'K', '10']:
        return 10
    elif card == 'A':
        return 11
    else:
        try:
            return int(card)
        except:
            return 0

def count_value(card):
    """Devuelve el valor del contador (sistema Hi-Lo):
       - Cartas 2-6: +1
       - Cartas 7-9: 0
       - Cartas 10, J, Q, K, A: -1
    """
    if card in ['2', '3', '4', '5', '6']:
        return 1
    elif card in ['7', '8', '9']:
        return 0
    elif card in ['10', 'J', 'Q', 'K', 'A']:
        return -1
    else:
        return 0

def calculate_total(cards):
    """Calcula el total óptimo de la mano considerando Aces como 11 o 1."""
    total = 0
    aces = 0
    for card in cards:
        if card == 'A':
            aces += 1
            total += 11
        else:
            total += card_value(card)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def is_soft(cards):
    """Determina si la mano es 'suave' (soft), es decir, contiene una A que se puede contar como 11."""
    total = sum(11 if card == 'A' else card_value(card) for card in cards)
    return ('A' in cards) and total <= 21

def basic_strategy(dealer_card, player_cards):
    """
    Devuelve una sugerencia ("Hit", "Stand", "Double", "Split", "Surrender")
    basada en la estrategia básica de blackjack (versión simplificada).

    Se utiliza la primera carta del dealer como la carta visible (upcard).
    Si el jugador tiene pareja (dos cartas iguales) se sugiere Split en casos simples.
    Luego se distingue entre manos duras y suaves.
    """
    # Caso de pareja (solo con dos cartas)
    if len(player_cards) == 2 and player_cards[0] == player_cards[1]:
        pair = player_cards[0]
        if pair in ['A', '8']:
            return "Split"
        elif pair in ['10', 'J', 'Q', 'K']:
            return "Stand"
        # Aquí se puede agregar más lógica para otras parejas

    total = calculate_total(player_cards)
    soft = ('A' in player_cards) and total <= 21
    dealer_val = card_value(dealer_card)
    
    if not soft:
        # Estrategia simplificada para manos duras
        if total >= 17:
            return "Stand"
        elif total >= 13 and dealer_val in range(2, 7):
            return "Stand"
        elif total == 12 and dealer_val in range(4, 7):
            return "Stand"
        elif total == 11:
            return "Double" if len(player_cards) == 2 else "Hit"
        elif total == 10 and dealer_val < 10:
            return "Double" if len(player_cards) == 2 else "Hit"
        elif total == 9 and dealer_val in range(3, 7):
            return "Double" if len(player_cards) == 2 else "Hit"
        else:
            return "Hit"
    else:
        # Estrategia simplificada para manos suaves
        if total >= 19:
            return "Stand"
        elif total == 18:
            if dealer_val in [2, 7, 8]:
                return "Stand"
            elif dealer_val in range(3, 7):
                return "Double" if len(player_cards) == 2 else "Stand"
            else:
                return "Hit"
        else:
            return "Hit"

def calculate_true_count(running_count, decks, cards_dealt):
    """Calcula el True Count en función del running count, número de mazos y cartas ya jugadas."""
    cards_remaining = decks * 52 - cards_dealt
    decks_remaining = cards_remaining / 52
    if decks_remaining == 0:
        return 0
    return running_count / decks_remaining

def bet_amount(true_count, min_bet, max_bet):
    """
    Calcula la apuesta sugerida según el true count y un bet spread de 1 a 5 unidades:
      - Para true count < 2: apuesta 1 unidad (min_bet)
      - Para true count entre 2 y menos de 3: apuesta 2 unidades (2 * min_bet)
      - Para true count entre 3 y menos de 4: apuesta 3 unidades (3 * min_bet)
      - Para true count entre 4 y menos de 5: apuesta 4 unidades (4 * min_bet)
      - Para true count >= 5: apuesta 5 unidades (max_bet)
    """
    if true_count < 2:
        multiplier = 1
    elif true_count < 3:
        multiplier = 2
    elif true_count < 4:
        multiplier = 3
    elif true_count < 5:
        multiplier = 4
    else:
        multiplier = 5
    bet = multiplier * min_bet
    return min(bet, max_bet)


# Rutas de la aplicación

@app.route('/', methods=['GET', 'POST'])
def menu():
    """Pantalla inicial para configurar apuesta mínima, máxima y número de mazos."""
    if request.method == 'POST':
        try:
            min_bet = int(request.form.get('min_bet', 1))
            max_bet = int(request.form.get('max_bet', 100))
            decks = int(request.form.get('decks', 1))
        except ValueError:
            return "Por favor, ingresa valores válidos."
        session['min_bet'] = min_bet
        session['max_bet'] = max_bet
        session['decks'] = decks
        session['running_count'] = 0
        session['cards_dealt'] = 0
        session['dealer_cards'] = []
        # Inicializamos las manos del jugador como una lista de manos
        session['player_hands'] = [[]]
        session['active_hand'] = 0  # Índice de la mano activa
        session['suggestion'] = ""
        return redirect(url_for('game'))
    return render_template('menu.html')

@app.route('/game', methods=['GET'])
def game():
    """Pantalla principal del juego."""
    running_count = session.get('running_count', 0)
    decks = session.get('decks', 1)
    cards_dealt = session.get('cards_dealt', 0)
    min_bet = session.get('min_bet', 1)
    max_bet = session.get('max_bet', 100)
    
    true_count = calculate_true_count(running_count, decks, cards_dealt)
    current_bet = bet_amount(true_count, min_bet, max_bet)
    
    dealer_cards = session.get('dealer_cards', [])
    player_hands = session.get('player_hands', [[]])
    active_hand = session.get('active_hand', 0)
    suggestion = session.get('suggestion', "")
    
    return render_template('game.html', 
                           dealer_cards=dealer_cards,
                           player_hands=player_hands,
                           active_hand=active_hand,
                           running_count=running_count,
                           true_count=round(true_count, 2),
                           current_bet=current_bet,
                           suggestion=suggestion)

@app.route('/add_card', methods=['POST'])
def add_card():
    """
    Ruta para agregar una carta ya sea al dealer o al jugador.
    Se actualiza el running count y el número de cartas jugadas.
    """
    role = request.form.get('role')  # 'dealer' o 'player'
    card = request.form.get('card')  # Valor de la carta: '2', 'A', etc.
    if card is None or role not in ['dealer', 'player']:
        return redirect(url_for('game'))
    
    if role == 'dealer':
        dealer_cards = session.get('dealer_cards', [])
        dealer_cards.append(card)
        session['dealer_cards'] = dealer_cards
    else:
        # Se recibe el índice de la mano; si no se proporciona se usa la mano activa
        hand_index = int(request.form.get('hand_index', session.get('active_hand', 0)))
        player_hands = session.get('player_hands', [[]])
        player_hands[hand_index].append(card)
        session['player_hands'] = player_hands
    
    # Actualizar contador y cartas jugadas
    running_count = session.get('running_count', 0) + count_value(card)
    session['running_count'] = running_count
    session['cards_dealt'] = session.get('cards_dealt', 0) + 1
    
    return redirect(url_for('game'))

@app.route('/split', methods=['POST'])
def split():
    """
    Realiza el split de la mano activa si es posible.
    Se verifica que la mano tenga 2 cartas iguales y se divide en dos manos.
    """
    player_hands = session.get('player_hands', [[]])
    active_hand = session.get('active_hand', 0)
    hand = player_hands[active_hand]
    
    if len(hand) == 2 and hand[0] == hand[1]:
        # Separamos la mano en dos manos distintas
        player_hands[active_hand] = [hand[0]]
        player_hands.insert(active_hand + 1, [hand[1]])
        session['player_hands'] = player_hands
        session['suggestion'] = "Split realizado. Ahora juega la Mano {}.".format(active_hand + 1)
    else:
        session['suggestion'] = "No es posible hacer split en esta mano."
    
    return redirect(url_for('game'))

@app.route('/confirm', methods=['POST'])
def confirm():
    """
    Al confirmar, se calcula la jugada recomendada usando la estrategia básica.
    Se toma la primera carta del dealer como upcard y se evalúa la mano activa.
    """
    dealer_cards = session.get('dealer_cards', [])
    player_hands = session.get('player_hands', [[]])
    active_hand = session.get('active_hand', 0)
    
    if not dealer_cards or not player_hands[active_hand]:
        session['suggestion'] = "Por favor, ingresa cartas para dealer y jugador."
    else:
        suggestion = basic_strategy(dealer_cards[0], player_hands[active_hand])
        session['suggestion'] = suggestion
    return redirect(url_for('game'))

@app.route('/next_hand', methods=['POST'])
def next_hand():
    """
    Cambia la mano activa a la siguiente si existe.
    """
    player_hands = session.get('player_hands', [[]])
    active_hand = session.get('active_hand', 0)
    if active_hand < len(player_hands) - 1:
        session['active_hand'] = active_hand + 1
        session['suggestion'] = "Ahora juega la Mano {}.".format(session['active_hand'] + 1)
    else:
        session['suggestion'] = "No hay más manos."
    return redirect(url_for('game'))

@app.route('/reset', methods=['POST'])
def reset():
    """Reinicia las manos y la sugerencia para comenzar una nueva mano sin perder la configuración y el contador."""
    session['dealer_cards'] = []
    session['player_hands'] = [[]]
    session['active_hand'] = 0
    session['suggestion'] = ""
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True)
