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

        The content should be generated in both English (en) and Portuguese (pt-BR).

        The response should be in JSON format with these fields:
        {
            "translations": [
                {
                    "language_id": 1,  // English
                    "title": "Character's full name in English",
                    "description": "Brief description in English"
                },
                {
                    "language_id": 2,  // Portuguese
                    "title": "Character's full name in Portuguese",
                    "description": "Brief description in Portuguese"
                }
            ],
            "spoilers": [
                {
                    "translations": [
                        {
                            "language_id": 1,
                            "content": "Clue 1 in English"
                        },
                        {
                            "language_id": 2,
                            "content": "Clue 1 in Portuguese"
                        }
                    ]
                },
                // ... up to 10 clues, each in both languages
            ]
        }

        Make the clues interesting and varied, ranging from obvious to subtle hints about the character.
        Ensure that the translations maintain the same meaning while being natural in each language.
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
