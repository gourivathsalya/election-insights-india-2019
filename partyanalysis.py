
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def party_analysis():
    print("=" * 50)
    print("  STEP 2: PARTY & WINNING ANALYSIS")
    print("=" * 50)

    df = pd.read_csv('data/cleaned_election_data.csv')
    winners = df[df['WINNER'] == 1]

    # ── GRAPH 1: Top 10 parties by seats won
    print("\nGenerating Graph 1 - Top 10 parties by seats won...")
    top_parties = winners['PARTY'].value_counts().head(10)

    plt.figure(figsize=(12, 6))
    bars = sns.barplot(x=top_parties.values, y=top_parties.index, palette='Blues_r')
    for i, v in enumerate(top_parties.values):
        bars.text(v + 0.3, i, str(v), va='center', fontsize=11)
    plt.title('Top 10 Parties by Seats Won — 2019 Indian General Election', fontsize=14, fontweight='bold')
    plt.xlabel('Seats Won')
    plt.ylabel('Party')
    plt.tight_layout()
    plt.savefig('graphs/01_top_parties.png', dpi=150)
    plt.show()
    print(" Graph 1 saved → graphs/01_top_parties.png")

    
    print("\nGenerating Graph 2 - Win rate by party...")
    top_contested = df['PARTY'].value_counts().head(10).index
    party_stats = df[df['PARTY'].isin(top_contested)].groupby('PARTY').agg(
        Total=('WINNER', 'count'),
        Wins=('WINNER', 'sum')
    )
    party_stats['Win Rate (%)'] = round((party_stats['Wins'] / party_stats['Total']) * 100, 1)
    party_stats = party_stats.sort_values('Win Rate (%)', ascending=False)

    plt.figure(figsize=(12, 6))
    bars = sns.barplot(x=party_stats['Win Rate (%)'], y=party_stats.index, palette='Oranges_r')
    for i, v in enumerate(party_stats['Win Rate (%)']):
        bars.text(v + 0.3, i, f'{v}%', va='center', fontsize=11)
    plt.title('Win Rate by Party (Top 10 Most Contested)', fontsize=14, fontweight='bold')
    plt.xlabel('Win Rate (%)')
    plt.ylabel('Party')
    plt.tight_layout()
    plt.savefig('graphs/02_win_rate_by_party.png', dpi=150)
    plt.show()
    print(" Graph 2 saved → graphs/02_win_rate_by_party.png")

   
    print("\n── PARTY INSIGHTS ──")
    print(f"Top party by seats won  : {top_parties.index[0]} ({top_parties.values[0]} seats)")
    print(f"Highest win rate party  : {party_stats.index[0]} ({party_stats['Win Rate (%)'].iloc[0]}%)")
    print(f"Total parties contested : {df['PARTY'].nunique()}")
    print("\n Party analysis complete!")

if __name__ == '__main__':
    party_analysis()