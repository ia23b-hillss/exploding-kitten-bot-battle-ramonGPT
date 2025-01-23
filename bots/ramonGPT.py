import random
from typing import List, Optional

from bot import Bot
from card import Card, CardType
from game_handling.game_state import GameState


class RamonGPT(Bot):
    def play(self, state: GameState) -> Optional[Card]:
        """
        Strategic decision-making for playing cards

        Strategy:
        1. If have 'See the Future', play it if near end of deck
        2. Avoid playing normal cards unless strategic
        3. Prefer to play Skip or other defensive cards
        4. Keep at least one defensive card in hand
        """

        priority_cards = [CardType.SKIP, CardType.SEE_THE_FUTURE]

        if state.cards_left_to_draw <= 3 and any(card.card_type == CardType.SEE_THE_FUTURE for card in self.hand):
            return next(card for card in self.hand if card.card_type == CardType.SEE_THE_FUTURE)

        priority_playable = [card for card in self.hand if card.card_type in priority_cards]
        if priority_playable:

            return random.choice(priority_playable)

        if random.random() < 0.4:

            playable_cards = [card for card in self.hand if card.card_type != CardType.DEFUSE]
            return random.choice(playable_cards) if playable_cards else None

        return None

    def handle_exploding_kitten(self, state: GameState) -> int:
        """
        Strategic placement of exploding kitten

        Strategy:
        1. If possible, place near the end of the deck
        2. If near end, place at a random earlier position
        3. Avoid placing at very top of deck
        """

        if state.cards_left_to_draw <= 3:
            return random.randint(1, max(1, state.cards_left_to_draw))


        max_placement = max(1, state.cards_left_to_draw - 2)
        return random.randint(max_placement // 2, max_placement)

    def see_the_future(self, state: GameState, top_three: List[Card]) -> None:
        """
        Strategic insight into future cards

        Strategy:
        1. Remember if an Exploding Kitten is in top 3
        2. Potentially adjust deck ordering in future plays
        """

        exploding_kittens = [card for card in top_three if card.card_type == CardType.EXPLODING_KITTEN]



        if exploding_kittens:

            pass