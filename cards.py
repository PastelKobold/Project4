import asyncio
import random
from collections import Counter
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Tuple

class Suit(Enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

@dataclass
class Card:
    suit: Suit
    rank: Rank

    def __str__(self):
        return f"{self.rank.name.capitalize()}{self.suit.value}"

@dataclass
class GameState:
    deck: List[Card]
    players: List[List[Card]]

def create_deck() -> List[Card]:
    return [Card(suit, rank) for suit in Suit for rank in Rank]

async def shuffle_deck(deck: List[Card]) -> List[Card]:
    await asyncio.sleep(0)  # simulating asynchronous behavior
    random.shuffle(deck)
    return deck

async def deal_cards(game_state: GameState, num_cards: int) -> List[Card]:
    new_cards = []
    for _ in range(num_cards):
        card = game_state.deck.pop()
        new_cards.append(card)
    return new_cards

def rank_hand(hand: List[Card]) -> Tuple[int, List[int]]:
    ranks = sorted([card.rank.value for card in hand], reverse=True)
    suits = [card.suit for card in hand]
    rank_counts = Counter(ranks)
    is_flush = len(set(suits)) == 1
    is_straight = len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4

    # Determine hand rank based on poker hand rankings
    # ... (refer to the previous code snippets for the full rank_hand function

async def draw_cards(game_state: GameState, player_idx: int, discard_indices: List[int]) -> None:
    player_hand = game_state.players[player_idx]
    for index in sorted(discard_indices, reverse=True):
        del player_hand[index]
    new_cards = await deal_cards(game_state, len(discard_indices))
    game_state.players[player_idx] = player_hand + new_cards

async def play_game(num_players: int) -> None:
    deck = await shuffle_deck(create_deck())
    game_state = GameState(deck=deck, players=[[] for _ in range(num_players)])

    for i in range(num_players):
        game_state.players[i] = await deal_cards(game_state, 5)

    for i, player_hand in enumerate(game_state.players):
        print(f"Player {i + 1}'s hand: {', '.join(str(card) for card in player_hand)}")

    for i in range(num_players):
        discard_indices = input(f"Player {i + 1}, enter the indices of the cards to discard (0-4, separated by spaces): ")
        discard_indices = [int(index) for index in discard_indices.split()]
        await draw_cards(game_state, i, discard_indices)

    for i, player_hand in enumerate(game_state.players):
        print(f"Player {i + 1}'s final hand: {', '.join(str(card) for card in player_hand)}")

    hand_ranks = [rank_hand(hand) for hand in game_state.players]
    max_rank = max(hand_ranks)
    winner_idx = hand_ranks.index(max_rank)
    print(f"Player {winner_idx + 1} wins with a {', '.join(str(card) for card in game_state.players[winner_idx])}!")

if __name__ == "__main__":
    num_players = int(input("Enter the number of players (2-4): "))
    while not (2 <= num_players <= 4):
        num_players = int(input("Enter a valid number of players (2-4): "))
    asyncio.run(play_game(num_players))

