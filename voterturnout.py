

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def voter_turnout_analysis():
    print("=" * 50)
    print("  STEP 4: VOTER TURNOUT ANALYSIS")
    print("=" * 50)

    df = pd.read_csv('data/cleaned_election_data.csv')

    
    turnout_col = [c for c in df.columns if 'TOTAL ELECTORS' in c and 'OVER' in c][0]

    
    state_turnout = df.groupby('STATE')[turnout_col].mean().sort_values(ascending=False)

    
    print("\nGenerating Graph 6 - Voter turnout by state...")
    plt.figure(figsize=(14, 10))
    colors = ['#2ecc71' if v >= state_turnout.mean() else '#e74c3c' for v in state_turnout.values]
    bars = plt.barh(state_turnout.index, state_turnout.values, color=colors)
    plt.axvline(x=state_turnout.mean(), color='navy', linestyle='--', linewidth=1.5, label=f'National Avg: {round(state_turnout.mean(),1)}%')
    plt.title('Average Voter Turnout by State — 2019 Indian Election', fontsize=14, fontweight='bold')
    plt.xlabel('Average Turnout (%)')
    plt.ylabel('State')
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphs/06voterturnout.png', dpi=150)
    plt.show()
    print(" Graph 6 saved → graphs/06voterturnout.png")

    
    print("\nGenerating Graph 7 - Turnout extremes...")
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    top5 = state_turnout.head(5)
    sns.barplot(x=top5.values, y=top5.index, palette='Greens_r', ax=axes[0])
    axes[0].set_title('Top 5 Highest Turnout States', fontweight='bold')
    axes[0].set_xlabel('Average Turnout (%)')
    for i, v in enumerate(top5.values):
        axes[0].text(v - 2, i, f'{round(v,1)}%', va='center', color='white', fontweight='bold')

    bottom5 = state_turnout.tail(5)
    sns.barplot(x=bottom5.values, y=bottom5.index, palette='Reds_r', ax=axes[1])
    axes[1].set_title('Top 5 Lowest Turnout States', fontweight='bold')
    axes[1].set_xlabel('Average Turnout (%)')
    for i, v in enumerate(bottom5.values):
        axes[1].text(v - 2, i, f'{round(v,1)}%', va='center', color='white', fontweight='bold')

    plt.suptitle('Voter Turnout Extremes by State', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('graphs/07turnoutextremes.png', dpi=150)
    plt.show()
    print(" Graph 7 saved → graphs/07turnoutextremes.png")

    
    print("\n── VOTER TURNOUT INSIGHTS ──")
    print(f"Highest turnout state  : {state_turnout.index[0]} ({round(state_turnout.values[0], 1)}%)")
    print(f"Lowest turnout state   : {state_turnout.index[-1]} ({round(state_turnout.values[-1], 1)}%)")
    print(f"National average       : {round(state_turnout.mean(), 1)}%")
    above_avg = (state_turnout >= state_turnout.mean()).sum()
    print(f"States above average   : {above_avg}")
    print("\nVoter turnout analysis complete!")

if __name__ == '__main__':
    voter_turnout_analysis()