import sys
import os
import pandas as pd
sys.path.append(os.path.dirname(__file__))

from cleaning import load_datasets, clean_matches_data, clean_deliveries_data, merge_datasets
from analysis import team_analysis, player_analysis, match_insights
from visualization import (
    plot_team_wins, plot_win_percentage, plot_player_runs, 
    plot_bowling_stats, plot_venue_performance, plot_batting_vs_chasing
)
from insights import generate_team_insights, generate_player_insights, generate_match_insights

def main():
    print("Welcome to IPL Cricket Data Analyzer!")
    
    try:
        # Load and clean data
        matches, deliveries = load_datasets()
        matches = clean_matches_data(matches)
        deliveries = clean_deliveries_data(deliveries)
        merged = merge_datasets(matches, deliveries)
        
        print("Data loaded and cleaned successfully.")
        
        while True:
            print("\nMenu:")
            print("1. Team Analysis")
            print("2. Player Analysis")
            print("3. Match Insights")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                print("\n--- Team Analysis ---")
                team_data = team_analysis(matches)
                
                # Display insights
                insights = generate_team_insights(team_data)
                for insight in insights:
                    print(insight)
                
                # Plots
                plot_team_wins(team_data['wins'])
                plot_win_percentage(team_data['win_percentage'])
                
                # Optional: Venue for a team
                team = input("Enter a team name to see venue performance (or press Enter to skip): ").strip()
                if team:
                    plot_venue_performance(team_data.get('venue_performance', pd.DataFrame()), team)
                
            elif choice == '2':
                print("\n--- Player Analysis ---")
                player_data = player_analysis(deliveries, matches)
                
                # Display insights
                insights = generate_player_insights(player_data)
                for insight in insights:
                    print(insight)
                
                # Plots
                plot_player_runs(player_data['batting'])
                plot_bowling_stats(player_data['bowling'])
                
            elif choice == '3':
                print("\n--- Match Insights ---")
                match_data = match_insights(matches, deliveries)
                
                # Display insights
                insights = generate_match_insights(match_data)
                for insight in insights:
                    print(insight)
                
                # Plots
                plot_batting_vs_chasing(match_data['batting_first_win_pct'], match_data['chasing_win_pct'])
                
            elif choice == '4':
                print("Exiting... Thank you for using IPL Cricket Data Analyzer!")
                break
            else:
                print("Invalid choice. Please try again.")
                
    except Exception as e:
        print(f"Error: {e}")
        print("Please ensure the datasets are in the 'data' folder.")

if __name__ == "__main__":
    main()