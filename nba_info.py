from balldontlie import BalldontlieAPI

# Initialize the API client with your API key
api = BalldontlieAPI(api_key="0b969460-2671-40c4-a635-07eca51f66dc")

# Use the 'search' parameter to look for Michael Jordan
players = api.nba.players.list(first_name="Kobe")

# Display results
if players.data:
    print("Player(s) Found:")
    for player in players.data:
        print(f"ID: {player.id}, Name: {player.first_name} {player.last_name}, Team: {player.team.full_name}")
else:
    print("Player not found.")
