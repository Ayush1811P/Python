import pandas as pd

def team_analysis(matches):
    """
    Perform team analysis: total matches, wins, losses, win percentage, toss impact.
    """
    # Total matches played by each team
    team_matches = matches['team1'].value_counts() + matches['team2'].value_counts()
    team_matches = team_matches.sort_values(ascending=False)
    
    # Wins
    team_wins = matches['winner'].value_counts()
    
    # Win percentage
    win_percentage = (team_wins / team_matches * 100).round(2)
    
    # Toss impact: wins when winning toss
    toss_wins = matches[matches['toss_winner'] == matches['winner']].groupby('winner').size()
    toss_win_percentage = (toss_wins / team_wins * 100).round(2).fillna(0)
    
    return {
        'total_matches': team_matches,
        'wins': team_wins,
        'win_percentage': win_percentage,
        'toss_win_percentage': toss_win_percentage
    }

def player_analysis(deliveries, matches):
    """
    Player analysis: runs, strike rate, wickets, economy.
    """
    # Batting stats
    batsman_stats = deliveries.groupby('batsman').agg({
        'batsman_runs': 'sum',
        'ball': 'count'
    }).rename(columns={'batsman_runs': 'runs', 'ball': 'balls_faced'})
    batsman_stats['strike_rate'] = (batsman_stats['runs'] / batsman_stats['balls_faced'] * 100).round(2)
    
    # Bowling stats
    bowler_stats = deliveries[deliveries['is_super_over'] == 0].groupby('bowler').agg({
        'total_runs': 'sum',
        'ball': 'count',
        'player_dismissed': lambda x: (x != 'Not Out').sum()
    }).rename(columns={'total_runs': 'runs_conceded', 'ball': 'balls_bowled', 'player_dismissed': 'wickets'})
    bowler_stats['overs'] = (bowler_stats['balls_bowled'] / 6).round(1)
    bowler_stats['economy'] = (bowler_stats['runs_conceded'] / bowler_stats['overs']).round(2)
    
    return {
        'batting': batsman_stats.sort_values('runs', ascending=False),
        'bowling': bowler_stats.sort_values('wickets', ascending=False)
    }

def match_insights(matches, deliveries):
    """
    Match-level insights: batting first vs chasing, venue performance, high-scoring matches.
    """
    # Batting first vs chasing
    batting_first_wins = matches[matches['win_by_runs'] > 0].shape[0]
    chasing_wins = matches[matches['win_by_wickets'] > 0].shape[0]
    total_matches = matches.shape[0]
    
    batting_first_win_pct = (batting_first_wins / total_matches * 100).round(2)
    chasing_win_pct = (chasing_wins / total_matches * 100).round(2)
    
    # Venue-based performance
    venue_wins = matches.groupby('venue')['winner'].value_counts().unstack().fillna(0)
    
    # High-scoring matches (total runs > 300)
    merged = pd.merge(deliveries, matches, left_on='match_id', right_on='id')
    match_scores = merged.groupby('match_id')['total_runs'].sum()
    high_scoring = match_scores[match_scores > 300].count()
    
    return {
        'batting_first_win_pct': batting_first_win_pct,
        'chasing_win_pct': chasing_win_pct,
        'venue_performance': venue_wins,
        'high_scoring_matches': high_scoring
    }