import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Set non-interactive backend
plt.switch_backend('Agg')

# Create plots directory if it doesn't exist
plots_dir = os.path.join(os.path.dirname(__file__), 'plots')
os.makedirs(plots_dir, exist_ok=True)

# Set style
sns.set_style('whitegrid')

def plot_team_wins(team_wins, title='Team Wins'):
    """
    Bar chart for team wins.
    """
    plt.figure(figsize=(10, 6))
    team_wins.head(10).plot(kind='bar', color='skyblue')
    plt.title(title)
    plt.xlabel('Team')
    plt.ylabel('Number of Wins')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'team_wins.png'))
    plt.close()
    print(f"Team wins chart saved as plots/team_wins.png")

def plot_win_percentage(win_pct, title='Win Percentage by Team'):
    """
    Bar chart for win percentages.
    """
    plt.figure(figsize=(10, 6))
    win_pct.head(10).plot(kind='bar', color='lightgreen')
    plt.title(title)
    plt.xlabel('Team')
    plt.ylabel('Win Percentage (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'win_percentage.png'))
    plt.close()
    print(f"Win percentage chart saved as plots/win_percentage.png")

def plot_player_runs(batsman_stats, title='Top Batsmen by Runs'):
    """
    Bar chart for top batsmen runs.
    """
    plt.figure(figsize=(10, 6))
    batsman_stats.head(10)['runs'].plot(kind='bar', color='orange')
    plt.title(title)
    plt.xlabel('Batsman')
    plt.ylabel('Total Runs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'player_runs.png'))
    plt.close()
    print(f"Player runs chart saved as plots/player_runs.png")

def plot_bowling_stats(bowler_stats, title='Top Bowlers by Wickets'):
    """
    Bar chart for top bowlers wickets.
    """
    plt.figure(figsize=(10, 6))
    bowler_stats.head(10)['wickets'].plot(kind='bar', color='red')
    plt.title(title)
    plt.xlabel('Bowler')
    plt.ylabel('Total Wickets')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'bowling_stats.png'))
    plt.close()
    print(f"Bowling stats chart saved as plots/bowling_stats.png")

def plot_venue_performance(venue_wins, team, title='Venue Performance for Team'):
    """
    Bar chart for venue wins for a specific team.
    """
    if team in venue_wins.columns:
        plt.figure(figsize=(10, 6))
        venue_wins[team].head(10).plot(kind='bar', color='purple')
        plt.title(f'{title} - {team}')
        plt.xlabel('Venue')
        plt.ylabel('Wins')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, f'venue_performance_{team.replace(" ", "_")}.png'))
        plt.close()
        print(f"Venue performance chart for {team} saved as plots/venue_performance_{team.replace(' ', '_')}.png")
    else:
        print(f"No data for team {team}")

def plot_batting_vs_chasing(batting_pct, chasing_pct, title='Batting First vs Chasing Wins'):
    """
    Pie chart for batting first vs chasing wins.
    """
    labels = ['Batting First', 'Chasing']
    sizes = [batting_pct, chasing_pct]
    colors = ['gold', 'lightcoral']
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.savefig(os.path.join(plots_dir, 'batting_vs_chasing.png'))
    plt.close()
    print(f"Batting vs chasing chart saved as plots/batting_vs_chasing.png")