# Sunderland v Sheffield Prediction
### This project analyses Sunderland AFC and Sheffield United's performance over the full 2024/25 Championship Season
The data used predicts:
- General outcome (Win/Draw/Loss) based on percentages of outcomes for both teams during the season
- Exact score prediction using H2H data from the season

## The Dataset
The dataset used for this project can be found in the [cleanData.csv](cleanData.csv) file, each row represents a match played by either team (specified in the Team column) and information about each match, such as goals for and against, and result.

The data used has been taken from [https://fbref.com](https://fbref.com) and edited in Microsoft Excel to contain certain information.

## How It Works
1. General Outcome Prediction

This part loads all Sunderland AFC and Sheffield United results from the CSV file. It calculates win, loss, and draw percentages for the two teams and combines the stats to predict which team is more likely to win or if it will be a draw.
2. Head-to-Head Score prediction

This looks at the H2H matches between the two teams in the CSV file and averages the goals scored by them to predict a scoreline.

## Contact
For questions or feedback, please contact [jessica.23.nicol@gmail.com](mailto:jessica.23.nicol@gmail.com).
