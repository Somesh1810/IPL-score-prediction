# Rock–Paper–Scissors–Plus AI Referee Bot

## Overview

This project implements a minimal **AI Game Referee** for a Rock–Paper–Scissors–Plus game. The bot runs a short, best-of-3 conversational game between a user and the system, enforcing rules, tracking state, and responding intelligently to user input.

The solution is designed to evaluate **logical reasoning, agent design, state modeling, and tool-based architecture**, aligned with the expectations of an AI Product Engineer (Conversational Agents) role.

---

## Game Rules

* The game is **best of 3 rounds**
* Valid moves:

  * rock
  * paper
  * scissors
  * bomb (can be used **once per player per game**)
* Bomb beats all other moves
* Bomb vs bomb results in a draw
* Invalid input **wastes the round**
* The game ends automatically after 3 rounds

---

## Architecture Overview

The system follows a clean **agent–tool–state separation**, inspired by Google ADK design principles.

### 1. State Model

Game state is stored explicitly in a Python data structure and persists across turns.

Tracked state includes:

* Current round number
* User score
* Bot score
* Bomb usage for user and bot
* Round history

State is maintained **in memory only** and never reconstructed from prompt text.

---

### 2. Tool Layer (Deterministic Logic)

All game rules and validations are enforced via explicit tools:

* `validate_move` – Validates user input and bomb usage
* `resolve_round` – Determines bot move and round winner
* `update_game_state` – Mutates game state after each round

These tools return structured outputs and ensure deterministic behavior, preventing invalid states such as bomb reuse or extra rounds.

---

### 3. Agent Layer

The agent is responsible for:

* Interpreting user intent
* Calling tools for validation and state mutation
* Generating user-facing responses

No game logic is embedded in prompts or response text.

---

## Interaction Modes

### CLI Mode (Primary)

The core implementation runs as a **simple conversational loop**, fully satisfying the assignment constraints.

Run:

```bash
python main.py
```

---

### Optional Streamlit UI

A lightweight Streamlit interface is included **only as a presentation layer**. It does not affect game logic, state handling, or tool usage.

Run:

```bash
streamlit run app.py
```

The CLI version remains the authoritative implementation.

---
**The core implementation runs as a CLI-based conversational loop; the Streamlit UI is optional and not required for compliance.**

---
## Constraints Compliance

This solution strictly follows the assignment constraints:

* No databases
* No external APIs
* No long-running backend servers
* No prompt-only state

All state is maintained in-memory, and all logic is local and deterministic.

---

## Design Tradeoffs

* A simple random strategy is used for the bot to keep focus on correctness
* CLI interaction is prioritized over UI polish
* Single-agent design is used due to limited problem scope

---

## Possible Improvements

With more time, the following could be added:

* Smarter bot strategy
* Structured JSON responses for all turns
* Replay or extended match support
* Unit tests for tools and state transitions

---

## How to Run

### Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

### Run CLI

```bash
python main.py
```

### Run UI (Optional)

```bash
streamlit run app.py
```

---

## Summary

This project prioritizes **correctness, clarity, and safe state handling** over UI polish. The design cleanly separates intent understanding, game logic, and response generation, making it suitable for conversational agent systems and easily adaptable to Google ADK environments.
