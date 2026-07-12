"""
Snake Water Gun Game
--------------------
A console-based game where the player competes against the computer.
Inspired by Rock-Paper-Scissors with Snake, Water, and Gun as choices.
"""

import random
from typing import Optional

CHOICES = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun",
}

WINNING_MOVES = {
    ("s", "w"),  # Snake drinks Water
    ("w", "g"),  # Water rusts Gun
    ("g", "s"),  # Gun kills Snake
}


def display_rules() -> None:
    """Display game rules and controls."""
    print("\n=== Snake • Water • Gun ===")
    print("\nRules:")
    print("  • Snake drinks Water  → Snake wins")
    print("  • Water rusts Gun     → Water wins")
    print("  • Gun kills Snake     → Gun wins")
    print("\nControls:")
    print("  [s] Snake   [w] Water   [g] Gun   [q] Quit")


def get_player_choice() -> Optional[str]:
    """Prompt the player until they enter a valid choice or quit."""
    while True:
        choice = input("\nYour choice: ").strip().lower()

        if choice == "q":
            return None

        if choice in CHOICES:
            return choice

        print("Invalid input. Enter 's', 'w', 'g', or 'q' to quit.")


def get_computer_choice() -> str:
    """Return a random choice for the computer."""
    return random.choice(list(CHOICES.keys()))


def determine_winner(player: str, computer: str) -> str:
    """Determine the winner of a round."""
    if player == computer:
        return "draw"

    if (player, computer) in WINNING_MOVES:
        return "player"

    return "computer"


def display_round_result(player: str, computer: str, outcome: str) -> None:
    """Display the choices and result of the current round."""
    result_messages = {
        "draw": "It's a Draw!",
        "player": "You Win!",
        "computer": "Computer Wins!",
    }

    print("\n" + "-" * 28)
    print(f"You       : {CHOICES[player]}")
    print(f"Computer  : {CHOICES[computer]}")
    print("-" * 28)
    print(f"Result    : {result_messages[outcome]}")


def display_score(score: dict[str, int]) -> None:
    """Display the current scoreboard."""
    print(
        "\nScoreboard → "
        f"You: {score['player']} | "
        f"Computer: {score['computer']} | "
        f"Draws: {score['draw']}"
    )


def play_round(score: dict[str, int]) -> bool:
    """
    Play one round of the game.

    Returns False if the player chooses to quit, otherwise True.
    """
    player = get_player_choice()

    if player is None:
        return False

    computer = get_computer_choice()
    outcome = determine_winner(player, computer)

    display_round_result(player, computer, outcome)
    score[outcome] += 1
    display_score(score)

    return True


def main() -> None:
    """Run the Snake Water Gun game."""
    score = {"player": 0, "computer": 0, "draw": 0}

    display_rules()

    while play_round(score):
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            break

    print("\nThanks for playing! Final score:")
    display_score(score)


if __name__ == "__main__":
    main()
