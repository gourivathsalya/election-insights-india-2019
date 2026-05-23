import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def criminal_wealth_analysis():
    print("=" * 50)
    print("  STEP 5: CRIMINAL CASES & WEALTH ANALYSIS")
    print("=" * 50)

    df = pd.read_csv('data/cleaned_election_data.csv')

    # Fix ASSETS column — remove text and convert to number
    df['ASSETS'] = (
        df['ASSETS'].astype(str)
        .str.replace('Rs ', '', regex=False)
        .str.replace(',', '', regex=False)
        .str.strip()
    )
    df['ASSETS'] = pd.to_numeric(df['ASSETS'], errors='coerce')

    winners = df[df['WINNER'] == 1].copy()
    losers  = df[df['WINNER'] == 0].copy()

    
    print("\nGenerating Graph 8 - Criminal cases comparison...")
    win_cases  = (winners['CRIMINAL CASES'] > 0).sum()
    win_clean  = (winners['CRIMINAL CASES'] == 0).sum()
    lose_cases = (losers['CRIMINAL CASES'] > 0).sum()
    lose_clean = (losers['CRIMINAL CASES'] == 0).sum()

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].pie([win_cases, win_clean],
                labels=['Has Cases', 'No Cases'],
                autopct='%1.1f%%', colors=['#e74c3c', '#2ecc71'],
                startangle=90, textprops={'fontsize': 12})
    axes[0].set_title('Criminal Cases — Winners', fontweight='bold')

    axes[1].pie([lose_cases, lose_clean],
                labels=['Has Cases', 'No Cases'],
                autopct='%1.1f%%', colors=['#e74c3c', '#2ecc71'],
                startangle=90, textprops={'fontsize': 12})
    axes[1].set_title('Criminal Cases — Losers', fontweight='bold')

    plt.suptitle('Criminal Cases: Winners vs Losers', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('graphs/08criminalcases.png', dpi=150)
    plt.show()
    print(" Graph 8 saved → graphs/08criminalcases.png")

    # ── GRAPH 9: Wealth (Assets) — Winners vs Losers
    print("\nGenerating Graph 9 - Wealth comparison...")
    df_valid = df.dropna(subset=['ASSETS'])

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='WINNER', y='ASSETS', data=df_valid,
                hue='WINNER', palette={0: '#e74c3c', 1: '#2ecc71'}, legend=False)
    plt.xticks([0, 1], ['Losers', 'Winners'])
    plt.title('Asset Distribution — Winners vs Losers', fontsize=14, fontweight='bold')
    plt.xlabel('Result')
    plt.ylabel('Assets (Rs)')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('graphs/09wealthcomparison.png', dpi=150)
    plt.show()
    print(" Graph 9 saved → graphs/09wealthcomparison.png")

   
    print("\nGenerating Graph 10 - Top 10 wealthiest winners...")
    winners_valid = winners.dropna(subset=['ASSETS'])
    top_wealthy = winners_valid.nlargest(10, 'ASSETS')[['NAME', 'PARTY', 'ASSETS']].copy()
    top_wealthy['ASSETS_CR'] = (top_wealthy['ASSETS'] / 1e7).round(1)

    plt.figure(figsize=(12, 6))
    bars = sns.barplot(x=top_wealthy['ASSETS_CR'], y=top_wealthy['NAME'],
                       hue=top_wealthy['NAME'], palette='YlOrRd_r', legend=False)
    for i, v in enumerate(top_wealthy['ASSETS_CR']):
        bars.text(v + 0.5, i, f'₹{v} Cr', va='center', fontsize=10)
    plt.title('Top 10 Wealthiest Winners — 2019 Election', fontsize=14, fontweight='bold')
    plt.xlabel('Assets (in Crores ₹)')
    plt.ylabel('Candidate')
    plt.tight_layout()
    plt.savefig('graphs/10wealthiestwinners.png', dpi=150)
    plt.show()
    print(" Graph 10 saved → graphs/10wealthiestwinners.png")

    
    print("\n── CRIMINAL & WEALTH INSIGHTS ──")
    print(f"Winners with criminal cases  : {win_cases} ({round(win_cases/len(winners)*100,1)}%)")
    print(f"Losers with criminal cases   : {lose_cases} ({round(lose_cases/len(losers)*100,1)}%)")
    avg_win  = winners['ASSETS'].mean()
    avg_lose = losers['ASSETS'].mean()
    print(f"Average assets (winners)     : ₹{round(avg_win/1e7, 1)} Cr")
    print(f"Average assets (losers)      : ₹{round(avg_lose/1e7, 1)} Cr")
    print("\n Criminal & wealth analysis complete!")

if __name__ == '__main__':
    criminal_wealth_analysis()