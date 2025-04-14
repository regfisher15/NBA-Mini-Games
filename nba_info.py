from balldontlie import BalldontlieAPI

# Initialize the API client
api = BalldontlieAPI(api_key="0b969460-2671-40c4-a635-07eca51f66dc")

# Get player information by ID
response = api.nba.players.get(19)  # Fetch player details using their ID

# Access the response's data attribute
if response.data:  # Properly access the 'data' attribute
    player = response.data
    print(f"ID: {player.id}, Name: {player.first_name} {player.last_name}, Team: {player.team.full_name}")
else:
    print("Player not found.")
