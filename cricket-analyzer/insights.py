def generate_team_insights(team_data):
    """
    Generate insights for team analysis.
    """
    insights = []
    
    # Top team by wins
    top_team = team_data['wins'].idxmax()
    top_wins = team_data['wins'].max()
    insights.append(f"{top_team} has the most wins with {top_wins} victories.")
    
    # Highest win percentage
    high_win_pct_team = team_data['win_percentage'].idxmax()
    high_win_pct = team_data['win_percentage'].max()
    insights.append(f"{high_win_pct_team} has the highest win percentage at {high_win_pct}%.")
    
    # Toss impact
    toss_impact_team = team_data['toss_win_percentage'].idxmax()
    toss_impact_pct = team_data['toss_win_percentage'].max()
    insights.append(f"{toss_impact_team} wins {toss_impact_pct}% of matches when they win the toss.")
    
    return insights

def generate_player_insights(player_data):
    """
    Generate insights for player analysis.
    """
    insights = []
    
    # Top batsman
    top_batsman = player_data['batting'].index[0]
    top_runs = player_data['batting'].iloc[0]['runs']
    insights.append(f"{top_batsman} is the leading run-scorer with {top_runs} runs.")
    
    # Top bowler
    top_bowler = player_data['bowling'].index[0]
    top_wickets = player_data['bowling'].iloc[0]['wickets']
    insights.append(f"{top_bowler} has taken the most wickets with {top_wickets}.")
    
    # High strike rate
    high_sr_batsman = player_data['batting']['strike_rate'].idxmax()
    high_sr = player_data['batting']['strike_rate'].max()
    insights.append(f"{high_sr_batsman} has the highest strike rate at {high_sr}.")
    
    return insights

def generate_match_insights(match_data):
    """
    Generate insights for match analysis.
    """
    insights = []
    
    batting_pct = match_data['batting_first_win_pct']
    chasing_pct = match_data['chasing_win_pct']
    
    if batting_pct > chasing_pct:
        insights.append(f"Teams batting first have a higher win rate ({batting_pct}%) compared to chasing ({chasing_pct}%).")
    else:
        insights.append(f"Teams chasing have a higher win rate ({chasing_pct}%) compared to batting first ({batting_pct}%).")
    
    high_scoring = match_data['high_scoring_matches']
    insights.append(f"There are {high_scoring} matches where teams scored over 300 runs.")
    
    return insights