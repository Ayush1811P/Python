import pandas as pd
import os

def load_datasets(data_dir=None):
    """
    Load matches and deliveries datasets from the data directory.
    """
    if data_dir is None:
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
    
    matches_path = os.path.join(data_dir, 'matches.csv')
    deliveries_path = os.path.join(data_dir, 'deliveries.csv')
    
    if not os.path.exists(matches_path):
        raise FileNotFoundError(f"matches.csv not found in {data_dir}")
    if not os.path.exists(deliveries_path):
        raise FileNotFoundError(f"deliveries.csv not found in {data_dir}")
    
    matches = pd.read_csv(matches_path)
    deliveries = pd.read_csv(deliveries_path)
    
    return matches, deliveries

def clean_matches_data(matches):
    """
    Clean the matches dataset: handle missing values, convert data types, remove duplicates.
    """
    # Remove duplicates
    matches = matches.drop_duplicates()
    
    # Handle missing values
    # For simplicity, fill missing values with appropriate defaults or drop if critical
    matches['city'] = matches['city'].fillna('Unknown')
    matches['winner'] = matches['winner'].fillna('No Result')
    matches['player_of_match'] = matches['player_of_match'].fillna('N/A')
    # Convert date to datetime
    matches['date'] = pd.to_datetime(matches['date'], errors='coerce')
    
    return matches

def clean_deliveries_data(deliveries):
    """
    Clean the deliveries dataset.
    """
    # Remove duplicates
    deliveries = deliveries.drop_duplicates()
    
    # Handle missing values
    deliveries['player_dismissed'] = deliveries['player_dismissed'].astype(str).fillna('Not Out')
    deliveries['dismissal_kind'] = deliveries['dismissal_kind'].fillna('Not Out')
    deliveries['fielder'] = deliveries['fielder'].fillna('N/A')
    
    return deliveries

def merge_datasets(matches, deliveries):
    """
    Merge matches and deliveries datasets on match_id for deeper analysis.
    """
    merged = pd.merge(deliveries, matches, left_on='match_id', right_on='id', how='left')
    return merged