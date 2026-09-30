# Rebuilding the IND vs WI 2nd ODI (Guwahati, 30 Sep 2026) dashboard in Power BI Desktop

Files are in `data/`: `match_info.csv`, `batting.csv`, `bowling.csv`, `fall_of_wickets.csv`, `overs.csv`, `did_not_bat.csv`.

## 1. Load the data
1. **Home > Get Data > Text/CSV**, then pick each CSV and click **Transform Data**. Don't use Load directly.
2. In Power Query, check the column types:
   - `runs, balls, fours, sixes, maidens, runs_conceded, wickets, over_no, runs_in_over, cumulative_runs, cumulative_wickets, legal_balls, score, wicket_no` → Whole Number
   - `strike_rate, economy` → Decimal
   - `overs` (bowling) and `over` (FoW) → **Text**. Values like 8.5 mean 8 overs and 5 balls, not a decimal. Use the `balls` column for any calculation.
   - `date` → Date
3. **Close & Apply**.

## 2. Model / relationships
Make a small Team dimension (**Modeling > New table**):
```DAX
Team = DATATABLE("Team", STRING, {{"India"},{"West Indies"}})
```
Relationships (Model view, single direction, one-to-many from Team):
- `Team[Team]` → `batting[team]`
- `Team[Team]` → `fall_of_wickets[batting_team]`
- `Team[Team]` → `overs[batting_team]`
- `Team[Team]` → `did_not_bat[team]`
- `Team[Team]` → `bowling[bowling_team]` (a team slicer then shows that team's bowlers; the HTML version works the same way)
- `match_info[match_id]` → `batting[match_id]`, `bowling[match_id]`, and the others (optional, since there is only one match)

## 3. DAX measures (Modeling > New measure; keep them in a `_Measures` table)
```DAX
Total Runs        = SUM(batting[runs])                       -- batter runs only (no extras)
Team Total        = MAX(overs[cumulative_runs])              -- includes extras: 405 / 406
Balls Faced       = SUM(batting[balls])
Strike Rate       = DIVIDE([Total Runs], [Balls Faced]) * 100
Fours             = SUM(batting[fours])
Sixes             = SUM(batting[sixes])
Boundary Runs     = [Fours] * 4 + [Sixes] * 6
Boundary %        = DIVIDE([Boundary Runs], [Total Runs])    -- format as %
Wickets           = SUM(bowling[wickets])
Runs Conceded     = SUM(bowling[runs_conceded])
Balls Bowled      = SUM(bowling[balls])
Economy           = DIVIDE([Runs Conceded], [Balls Bowled] / 6)
Bowling Average   = DIVIDE([Runs Conceded], [Wickets])
Run Rate          = DIVIDE([Team Total], SUM(overs[legal_balls]) / 6)
Top Scorer =
    VAR t = TOPN(1, batting, batting[runs], DESC)
    RETURN MAXX(t, batting[batter] & " " & batting[runs] & IF(batting[not_out]=1,"*",""))
Best Bowler =
    VAR t = TOPN(1, bowling, bowling[wickets], DESC, bowling[runs_conceded], ASC)
    RETURN MAXX(t, bowling[bowler] & " " & bowling[wickets] & "/" & bowling[runs_conceded])
Result            = SELECTEDVALUE(match_info[result])
```

## 4. Visuals (one page, 16:9 or custom 1600×1900)
Theme: **View > Themes > Dark**, or a custom JSON with India `#118DFF`, West Indies `#E66C37`, and accent `#F2C811`.

| Dashboard section | Power BI visual | Fields |
|---|---|---|
| Team slicer | **Slicer** (Tile style) | Team[Team] |
| KPI: WI score, IND score | **Card** ×2 | Team Total (filter each card to one team) + a `match_info` wickets/overs card |
| KPI: Result | **Card** / Multi-row card | Result, match_info[series_status] |
| KPI: Top scorer / Best bowler | **Card** | Top Scorer, Best Bowler |
| KPI: Boundaries | **Multi-row card** | Fours, Sixes, Boundary Runs |
| Runs by batter | **Clustered bar chart** | Y: batting[batter], X: Total Runs, Legend: batting[team]; sort by bat_pos; tooltips: Balls Faced, Strike Rate, Fours, Sixes |
| Wickets vs economy | **Line and clustered column chart** | X: bowling[bowler], Column: Wickets (legend bowling_team), Line (secondary axis): Economy |
| 4s / 6s breakdown | **Stacked column chart** | X: batting[batter], Values: Fours, Sixes |
| Scoring mix | **Donut chart** ×2 (or one with small multiples = team) | Boundary Runs vs (Team Total − Boundary Runs) |
| Run progression (worm) | **Line chart** | X: overs[over_no] (Continuous), Y: Max of cumulative_runs, Legend: batting_team |
| Fall of wickets on worm | Add `fall_of_wickets` as a second **Line chart** series with markers only, or use a **Scatter chart** (X: numeric over, Y: score, Legend: batting_team) laid over the worm | For a numeric over, add a column: `Over Num = INT(VALUE([over])) + MOD(VALUE([over])*10,10)/6` |
| Manhattan | **Clustered column chart** | X: overs[over_no], Y: runs_in_over, Legend: batting_team |
| Batting scorecard | **Table** | batter, dismissal, runs, balls, fours, sixes, Strike Rate (conditional formatting: data bars on runs) |
| Bowling scorecard | **Table** | bowler, bowling_team, overs (text), maidens, runs_conceded, wickets, Economy (background colour scale, green→red) |
| Fall of wickets | **Table** | batting_team, wicket_no, score, batter_out, over |

Tips: turn on **Edit interactions** so that clicking a team bar cross-filters the tables. Use conditional formatting > Field value on a `Team Colour` column (`IF([team]="India","#118DFF","#E66C37")`) to keep the team colours consistent.

## Data notes
- India's extras (22) = 406 − batter runs 384. The breakdown was not published in the sources. The India bowlers' figures add up to 403 against WI's 405, while PTI's WI extras line (b1, nb1, w20) implies 404. That leaves a 1-run gap in the source data that we did not reconcile.
- `overs.csv` over 44 for India is a partial over (3 legal balls: 4, 1, 1), taken from ball-by-ball commentary.
