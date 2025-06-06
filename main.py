import csv

def load_data(filename):
    players = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['matches'] = int(row['matches'])
            row['goals'] = int(row['goals'])
            row['wins'] = int(row['wins'])
            players.append(row)
    return players

def top_scorers(data):
    sorted_data = sorted(data, key=lambda player: player['goals'], reverse=True)
    print("\nTop Scorers:")
    for i, player in enumerate(sorted_data[:3], start=1):
        print(f"{i}. {player['name']} ({player['team']}) - {player['goals']} goals")

def show_player_stats(data, name):
    found = False
    for player in data:
        if player['name'].lower() == name.lower():
            found = True
            matches = player['matches']
            goals = player['goals']
            wins = player['wins']
            avg_goals = goals / matches if matches > 0 else 0
            win_rate = (wins / matches * 100) if matches > 0 else 0

            print(f"\nStats for {player['name']} ({player['team']}):")
            print(f"Matches Played: {matches}")
            print(f"Goals Scored: {goals}")
            print(f"Wins: {wins}")
            print(f"Average Goals/Match: {avg_goals:.2f}")
            print(f"Win Rate: {win_rate:.2f}%")
            break
    if not found:
        print(f"Player '{name}' not found.")

def compare_players(data, name1, name2):
    p1 = p2 = None
    for player in data:
        if player['name'].lower() == name1.lower():
            p1 = player
        if player['name'].lower() == name2.lower():
            p2 = player

    if not p1 or not p2:
        print("One or both players not found.")
        return

    def stats(p):
        avg_goals = p['goals'] / p['matches'] if p['matches'] > 0 else 0
        win_rate = (p['wins'] / p['matches']) * 100 if p['matches'] > 0 else 0
        return avg_goals, win_rate

    avg1, win1 = stats(p1)
    avg2, win2 = stats(p2)

    print(f"\nComparison: {p1['name']} vs {p2['name']}")
    print(f"{p1['name']} - Avg Goals: {avg1:.2f}, Win Rate: {win1:.2f}%")
    print(f"{p2['name']} - Avg Goals: {avg2:.2f}, Win Rate: {win2:.2f}%")

def team_win_rates(data):
    team_stats = {}
    for player in data:
        team = player['team']
        if team not in team_stats:
            team_stats[team] = {'wins': 0, 'matches': 0}
        team_stats[team]['wins'] += player['wins']
        team_stats[team]['matches'] += player['matches']

    print("\nTeam Win Rates:")
    for team, stats in team_stats.items():
        win_rate = (stats['wins'] / stats['matches']) * 100 if stats['matches'] > 0 else 0
        print(f"{team}: {win_rate:.2f}% win rate")

def main():
    data = load_data('sports_data.csv')
    while True:
        print("\nWelcome to the Sports Stats Dashboard!")
        print("1. Show Top Scorers")
        print("2. Show Player Stats")
        print("3. Compare Players")
        print("4. Show Team Win Rates")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            top_scorers(data)
        elif choice == "2":
            name = input("Enter player name: ")
            show_player_stats(data, name)
        elif choice == "3":
            name1 = input("First player: ")
            name2 = input("Second player: ")
            compare_players(data, name1, name2)
        elif choice == "4":
            team_win_rates(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
