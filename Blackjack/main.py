from Blackjack.logo_and_deck import logo, deck
from random import choices


def winner(user_deck_sum, dealer_deck_sum):
    if user_deck_sum == dealer_deck_sum:
        return "That's a draw"
    if user_deck_sum <= 21 < dealer_deck_sum or dealer_deck_sum < user_deck_sum:
        return "You win"
    return "You lose"


def check_for_aces(user_deck):
    if 11 in user_deck and sum(user_deck) > 21:
        index_to_replace = user_deck.index(11)
        user_deck[index_to_replace] = 1


def check_bust(user_deck):
    if sum(user_deck) > 21:
        print("You busted")


def draw_card(deck, role):
    if role == "dealer":
        deck.extend(choices(deck, k=1))
        if sum(deck) <= 16:
            deck.extend(choices(deck, k=1))
    elif role == "user":
        deck.extend(choices(deck, k=1))


start = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
if start == 'y':
    print(logo)
    user_deck = choices(deck, k=2)
    dealer_deck = choices(deck, k=1)
    print(f"Your cards are: {user_deck}, current score: {sum(user_deck)}")
    print(f"Dealer's first card: {dealer_deck[0]}")
    one_more_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while one_more_card == 'y':
        draw_card(user_deck, "user")
        check_for_aces(user_deck)
        print(user_deck, dealer_deck)
        check_bust(user_deck)
        one_more_card = input("Type 'y' to get another card, type 'n' to pass: ")
    draw_card(dealer_deck, "dealer")
    print(user_deck, dealer_deck)
    print(winner(sum(user_deck), sum(dealer_deck)))
