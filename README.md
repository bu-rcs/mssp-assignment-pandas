# Assignment Pandas

This assignment is written in Python using Pandas and is tested with Pytest.

## The assignment

For this assignment you will be working with the regular season NBA player
statistics from 2022-2023. This dataset is located in the subdirectory dataset.
The assignment is to implement the following tasks.

1. Write a function that imports the dataset. The function must return a Pandas
    dataframe with the full 2022-2023 NBA regular season dataset.
2. Write a function that imports the NBA statistics dataset and returns a
    dataframe containing only players on the Boston Celtics. Sort the dataframe
    in descending order by `PTS`.  
3. Write a function grouping players by position and compute the average age of
    each position. The function must return a dataframe containing the position
    and the average age of the position.
4. There are duplicate entries for players that were traded during the season.
    Your task is to create a dataframe that contains unique player names and 
    their total season stats. The combined stats are listed for the duplicate 
    players in the row where `Tm = TOT`. You can thus remove duplicate player 
    entries by keeping only this row.

    Hint: Use groupby and the agg function `first`.

## Run command

On the SCC:

```bash
module load miniconda
module load academic-ml/spring-2024
conda activate spring-2024-pyt
cd /path/that/contains/this/repo
pytest
```
