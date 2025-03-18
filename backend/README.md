# Backend - Infinite Who

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Infinite Who (inspired by the game ["20 Questions"](https://boardgamegeek.com/boardgame/3377/20-questions)) is a project for those who like to use their imagination to guess the character/place/thing of a card.
The name infinite comes from the fact that the game is infinite, as the cards are generated automatically by the AI.

Compete with your friends to see who can guess the most cards!
In Solo mode, the game should have two rankings:
- Weekly ranking: based on the number of cards guessed in a week
- All time ranking: based on the number of cards guessed in the whole game

In Multiplayer mode, the game should have a board to compete with your friends.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to install:

- [Python](https://www.python.org/downloads/)
- [PDM](https://pdm-project.org/en/latest/#installation)
- [Make](https://www.gnu.org/software/make/)
- [Docker](https://www.docker.com/)

### Installing

A step by step series of examples that tell you how to get a development env running.

```
git clone https://github.com/davigps/infinite-who.git
cd infinite-who
cd backend
make install
```

Start the database container:

```
make db-up
```

Run the migrations:

```
make db-upgrade
```

Run the server:

```
make start
```

## Usage <a name = "usage"></a>

Run the server:

```
make start
```

To run tests:

```
make test
```
