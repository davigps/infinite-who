from typing import List


class PromptService:
    def get_create_card_prompt(self, previous_card_titles: List[str]) -> str:
        prompt = """
        You are a helpful assistant that generates content for a card game called "Profile".
        The game consists of cards containing clues about famous characters, where players need to guess who they are.

        Generate a card with the following:
        1. A title that is the name of the character
        2. A description that provides context about who this character is
        3. Generate 10 unique spoilers/clues about this character that will help players guess who it is

        The response should be in JSON format with these fields:
        {
            "title": "Character's full name",
            "description": "Brief description of who this character is",
            "spoilers": [
                {"content": "Clue 1"},
                {"content": "Clue 2"},
                ...up to 10 clues
            ]
        }

        Make the clues interesting and varied, ranging from obvious to subtle hints about the character.
        """

        previous_prompt = f"""
        The previous card titles are:
        {", ".join(previous_card_titles)}

        The new card title should be different from the previous ones.
        """

        return f"{previous_prompt}\n\n{prompt}"

    def get_verify_guess_prompt(self) -> str:
        return """
        You are a helpful assistant verifying if a user's guess matches the character from a Profile game card.

        Given the card title (correct character name) and the user's guess, determine if they are referring to the same person.
        Consider common nicknames, spelling variations, and partial names.

        Respond with a clear YES or NO, followed by a brief explanation of your reasoning.
        """
