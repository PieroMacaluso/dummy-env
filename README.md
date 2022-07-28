# Dummy Environment

This is a dummy environment to examine the problem related to [this issue](https://github.com/Farama-Foundation/SuperSuit/issues/169).

## Requirements
```toml
python = "^3.8,<3.11"
gym = "0.25"
PettingZoo = "^1.19.0"
SuperSuit = "^3.5.0"
stable-baselines3 = {git = "https://github.com/carlosluis/stable-baselines3.git", rev = "fix_tests"}
```

## How to setup

### Option 1: Poetry and PyEnv

1. Clone the repo and `cd` inside it.
2. `pyenv install 3.8.10`
3. `poetry env use 3.8.10`
4. `poetry install`
5. `poetry shell`
6. `python main_dummy.py`

### Option 2: `requirements.txt`

1. `python3.8 -m venv ./.venv`
2. `source ./.venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python main_dummy.py`


