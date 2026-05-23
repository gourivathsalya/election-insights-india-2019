
import os
from datacleaning      import load_and_clean
from partyanalysis     import party_analysis
from candidateanalysis import candidate_analysis
from voterturnout      import voter_turnout_analysis
from criminalanalysis  import criminal_wealth_analysis

def main():
    print("\n" + "=" * 50)
    print("  INDIAN ELECTION 2019 — DATA ANALYSIS")
    print("  By: Gouri Vathsalya")
    print("=" * 50 + "\n")

    # Create folders if not exists
    os.makedirs('graphs', exist_ok=True)
    os.makedirs('data', exist_ok=True)

    # Run all analyses in order
    load_and_clean()
    print("\n")
    party_analysis()
    print("\n")
    candidate_analysis()
    print("\n")
    voter_turnout_analysis()
    print("\n")
    criminal_wealth_analysis()

    print("\n" + "=" * 50)
    print("  ALL ANALYSIS COMPLETE!")
    print("  10 graphs saved in /graphs folder")
    print("=" * 50 + "\n")

if __name__ == '__main__':
    main()