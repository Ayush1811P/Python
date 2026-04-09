# IPL Cricket Data Analyzer

A comprehensive Python-based data analytics project for analyzing IPL (Indian Premier League) cricket datasets. This project provides insights into team performance, player statistics, and match trends through interactive command-line interface with visualizations.

## Features

- **Team Analysis**: Total matches played, wins/losses, win percentage, toss impact, and venue-based performance
- **Player Analysis**: Batting statistics (runs, strike rate) and bowling statistics (wickets, economy)
- **Match Insights**: Batting first vs chasing success rates, venue performance, and high-scoring matches
- **Interactive CLI**: User-friendly menu system for exploring different analyses
- **Visualizations**: Clear charts and graphs using Matplotlib and Seaborn
- **Modular Design**: Well-structured code with separate modules for cleaning, analysis, visualization, and insights

## Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Basic plotting
- **Seaborn**: Advanced statistical visualizations

## Project Structure

```
cricket-analyzer/
│
├── data/
│   ├── matches.csv          # IPL matches dataset
│   └── deliveries.csv       # Ball-by-ball deliveries dataset
├── main.py                  # Main CLI application
├── cleaning.py              # Data loading and cleaning functions
├── analysis.py              # Data analysis functions
├── visualization.py         # Plotting and visualization functions
├── insights.py              # Insight generation functions
└── README.md                # Project documentation
```

## Installation and Setup

1. **Clone or Download** the project to your local machine.

2. **Install Dependencies**:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

3. **Prepare Data**:
   - Download IPL datasets (matches.csv and deliveries.csv)
   - Place the CSV files in the `data/` directory
   - You can find these datasets on Kaggle or other data sources

4. **Run the Application**:
   ```bash
   python cricket-analyzer/main.py
   ```
   Or from within the cricket-analyzer directory:
   ```bash
   cd cricket-analyzer
   python main.py
   ```

## How to Use

1. Launch the application by running `python main.py`
2. Choose from the menu options:
   - **1. Team Analysis**: View team performance statistics and visualizations
   - **2. Player Analysis**: Explore player batting and bowling statistics
   - **3. Match Insights**: Discover match-level trends and patterns
   - **4. Exit**: Close the application

3. Follow the on-screen prompts for additional inputs (e.g., specific team names)

## Sample Outputs

### Team Analysis
- "Gujarat Titans has the most wins with 3 victories."
- "Kolkata Knight Riders has the highest win percentage at 66.67%."
- "Royal Challengers Bengaluru wins 50.0% of matches when they win the toss."
- Charts saved: `plots/team_wins.png`, `plots/win_percentage.png`

### Player Analysis
- "Phil Salt is the leading run-scorer with 20.0 runs."
- "AR Patel has taken the most wickets with 0.0."
- "Phil Salt has the highest strike rate at 222.22."
- Charts saved: `plots/player_runs.png`, `plots/bowling_stats.png`

### Match Insights
- "Teams batting first have a higher win rate (60.0%) compared to chasing (40.0%)."
- Chart saved: `plots/batting_vs_chasing.png`

## Generated Charts

The application saves visualization files in the `plots/` directory:
- `team_wins.png` - Bar chart showing team victories
- `win_percentage.png` - Bar chart showing win percentages  
- `player_runs.png` - Bar chart showing top batsmen by runs
- `bowling_stats.png` - Bar chart showing top bowlers by wickets
- `venue_performance_[team].png` - Venue-specific performance charts
- `batting_vs_chasing.png` - Pie chart comparing batting strategies

## Data Sources

The project includes sample IPL 2025 datasets with realistic match and delivery data:
- **matches.csv**: Contains information about IPL 2025 matches (teams, winners, venues, etc.)
- **deliveries.csv**: Ball-by-ball data for IPL 2025 matches (batsmen, bowlers, runs, wickets, etc.)

The sample data includes all current IPL teams:
- Chennai Super Kings
- Delhi Capitals
- Gujarat Titans
- Kolkata Knight Riders
- Lucknow Super Giants
- Mumbai Indians
- Punjab Kings
- Rajasthan Royals
- Royal Challengers Bengaluru
- Sunrisers Hyderabad

For real historical data, you can download actual IPL datasets from Kaggle or other sources and replace the sample files.

## Future Enhancements

- Filter analysis by specific seasons
- Compare performance between two teams
- Add machine learning predictions for match outcomes
- Web-based interface using Flask or Streamlit
- More advanced visualizations (heatmaps, scatter plots)

## Contributing

Feel free to fork this project and add your own features or improvements!

## License

This project is open-source and available under the MIT License.