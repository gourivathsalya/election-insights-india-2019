

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def candidate_analysis():
    print("=" * 50)
    print("  STEP 3: CANDIDATE ANALYSIS")
    print("=" * 50)

    df = pd.read_csv('data/cleaned_election_data.csv')
    winners = df[df['WINNER'] == 1]
    losers  = df[df['WINNER'] == 0]

   
    print("\nGenerating Graph 3 - Gender distribution...")
    gender_counts = df['GENDER'].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts.values, labels=gender_counts.index,
            autopct='%1.1f%%', colors=['#2196F3', '#E91E63'],
            startangle=90, textprops={'fontsize': 12})
    plt.title('Gender Distribution of All Candidates', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('graphs/03genderdistribution.png', dpi=150)
    plt.show()
    print(" Graph 3 saved → graphs/03genderdistribution.png")

   
    print("\nGenerating Graph 4 - Age distribution...")
    plt.figure(figsize=(10, 5))
    sns.histplot(df['AGE'], bins=20, color='steelblue', kde=True, label='All Candidates')
    sns.histplot(winners['AGE'], bins=20, color='green', kde=True, alpha=0.5, label='Winners')
    plt.title('Age Distribution — All Candidates vs Winners', fontsize=14, fontweight='bold')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphs/04agedistribution.png', dpi=150)
    plt.show()
    print(" Graph 4 saved → graphs/04agedistribution.png")

    
    print("\nGenerating Graph 5 - Education of winners vs losers...")
    edu_winner = winners['EDUCATION'].value_counts().head(6)
    edu_loser  = losers['EDUCATION'].value_counts().head(6)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.barplot(x=edu_winner.values, y=edu_winner.index, palette='Greens_r', ax=axes[0])
    axes[0].set_title('Education Level — Winners', fontweight='bold')
    axes[0].set_xlabel('Count')

    sns.barplot(x=edu_loser.values, y=edu_loser.index, palette='Reds_r', ax=axes[1])
    axes[1].set_title('Education Level — Losers', fontweight='bold')
    axes[1].set_xlabel('Count')

    plt.suptitle('Education Level: Winners vs Losers', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('graphs/05educationcomparison.png', dpi=150)
    plt.show()
    print("Graph 5 saved → graphs/05educationcomparison.png")

    
    print("\n── CANDIDATE INSIGHTS ──")
    print(f"Male candidates   : {gender_counts.get('MALE', 0)}")
    print(f"Female candidates : {gender_counts.get('FEMALE', 0)}")
    female_winners = winners['GENDER'].value_counts().get('FEMALE', 0)
    print(f"Female winners    : {female_winners}")
    print(f"Average age (all)     : {round(df['AGE'].mean(), 1)}")
    print(f"Average age (winners) : {round(winners['AGE'].mean(), 1)}")
    print("\n Candidate analysis complete!")

if __name__ == '__main__':
    candidate_analysis()