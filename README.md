# 🗳️ Indian General Election 2019 — Data Analysis

> End-to-end exploratory data analysis of the 2019 Indian General Elections.  
> Uncovers party performance, candidate profiles, criminal records, voter turnout, and wealth trends — visualized across 10 charts.

---

## 🚀 Overview

The 2019 Indian General Elections saw **over 600 million votes** cast across 543 constituencies. This project performs a multi-angle analysis of the official election dataset across 5 focused Python modules — party results, candidate profiles, voter turnout, criminal backgrounds, and wealth comparison — all producing publication-ready charts.

---

## 📊 10 Visualizations Generated

| File | Chart | Insight |
|---|---|---|
| `01_top_parties.png` | Bar — Top parties by seats won | BJP vs INC vs others |
| `02_win_rate_by_party.png` | Bar — Win rate % by party | Which parties converted candidates to wins |
| `03genderdistribution.png` | Pie/Bar — Gender of candidates | Women representation in elections |
| `04agedistribution.png` | Histogram — Age distribution | Which age groups contested most |
| `05educationcomparison.png` | Bar — Education levels | Literate vs graduate vs postgrad winners |
| `06voterturnout.png` | Bar — Voter turnout by state | Which states voted most |
| `07turnoutextremes.png` | Chart — Highest & lowest turnout | Best vs worst participation states |
| `08criminalcases.png` | Bar — Candidates with criminal cases | How many winners had criminal records |
| `09wealthcomparison.png` | Chart — Avg asset value by party | Which party's candidates are wealthiest |
| `10wealthiestwinners.png` | Bar — Top 10 wealthiest winners | Richest elected candidates |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.10** | Core language |
| **Pandas** | Data loading, cleaning, groupby analysis |
| **Matplotlib** | All chart generation and saving |
| **Seaborn** | Statistical visualizations |

---

## 📁 Project Structure

```
electionanalysis/
├── data/
│   ├── electionanalysis.csv          # Raw dataset
│   └── cleaned_election_data.csv     # After cleaning (datacleaning.py output)
├── graphs/
│   ├── 01_top_parties.png
│   ├── 02_win_rate_by_party.png
│   ├── 03genderdistribution.png
│   ├── 04agedistribution.png
│   ├── 05educationcomparison.png
│   ├── 06voterturnout.png
│   ├── 07turnoutextremes.png
│   ├── 08criminalcases.png
│   ├── 09wealthcomparison.png
│   └── 10wealthiestwinners.png
├── datacleaning.py        # Data loading, null handling, type conversion
├── partyanalysis.py       # Charts 01, 02 — party seats and win rates
├── candidateanalysis.py   # Charts 03, 04, 05 — gender, age, education
├── voterturnout.py        # Charts 06, 07 — state-wise turnout
├── criminalanalysis.py    # Chart 08 — criminal background of candidates
├── main.py                # Runs all modules in sequence
└── README.md
```

---

## ⚙️ How to Run

```bash
# Clone the repository
git clone https://github.com/gourivathsalya/election-analysis-2019.git
cd electionanalysis

# Install dependencies
pip install pandas matplotlib seaborn

# Run full analysis (generates all 10 charts)
python main.py
```

All charts are saved to the `graphs/` folder automatically.

---

## 📦 Dataset

- **Source:** Election Commission of India / Kaggle
- **Raw file:** `electionanalysis.csv`
- **Cleaned file:** `cleaned_election_data.csv` (output of `datacleaning.py`)
- **Key columns:** Constituency, State, Candidate, Party, Votes, Total Votes, Gender, Age, Education, Assets, Criminal Cases, Winner

---

## 🧹 Data Cleaning (datacleaning.py)

```python
# Key steps performed
1. Removed rows with null candidate or party names
2. Standardized party name formats
3. Converted Assets column from string ("Rs 1,20,00,000") to numeric
4. Extracted numeric age from mixed-format column
5. Derived vote_share = (votes / total_votes) * 100
6. Saved cleaned output to cleaned_election_data.csv
```

---

## 🔍 Key Findings

- **BJP** won 303 seats; highest win rate among major parties
- **~43%** of winning candidates had at least one criminal case registered
- Average asset value of winners: **₹14.7 crore**
- **Voter turnout** was highest in Northeast India (Nagaland, Manipur ~80%+)
- Women candidates made up only **~9%** of total contestants

---

## 🔮 Future Improvements

- [ ] Interactive Streamlit dashboard with state/party filters
- [ ] Choropleth map of India showing state-wise results
- [ ] 2014 vs 2019 comparative analysis
- [ ] Sentiment analysis of election-related tweets

---

## 📄 What I Learned

- Structuring a multi-file Python data analysis project
- Pandas GroupBy, aggregation, and derived columns
- Choosing the right chart type for each insight
- Saving publication-quality charts with Matplotlib
- Real-world data cleaning (messy formats, nulls, type errors)

---

## 👩‍💻 Author

**Gouri Vathsalya**  
B.Tech CSE | RGUKT Ongole  
🔗 [LinkedIn](https://linkedin.com/in/gourivathsalya) · 🐙 [GitHub](https://github.com/gourivathsalya)

---

## 📄 License

MIT License — free to use and modify.
