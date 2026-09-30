# India vs West Indies, 2nd ODI

India chased 406 in 43.3 overs at Barsapara, Guwahati, on 30 September 2026. West Indies had posted 405 for 7. India won by 8 wickets with 39 balls left, and led the three-match series 2-0.

Shubman Gill made 223 not out off 133. Rohit Sharma made 101. West Indies had hundreds from Amir Jangoo (114), Shai Hope (104) and John Campbell (101). There was no fifty in the match. Kuldeep Yadav, Ravindra Jadeja and Gurnoor Brar each took two wickets. West Indies took two wickets in the innings.

The Power BI report is the working view of that scorecard. Every figure on it is calculated from the files in `data/`.

Photographs of Rohit Sharma, Shubman Gill and Virat Kohli are on the Player Comparison page. Credits are in [dashboards/powerbi/image-credits.md](dashboards/powerbi/image-credits.md).


[Dashboard walkthrough (42 s)](dashboards/powerbi/dashboard-walkthrough.mp4)

| | |
| --- | --- |
| **Match Overview**: West Indies 405/7 off 50 overs at 8.10 an over, India 406/2 off 43.3 at 9.33, 39 balls and 8 wickets left ![Match Overview](dashboards/powerbi/screenshots/01-match-overview.png) | **Batting**: India 384 off 264 balls at 145.45, West Indies 382 off 301 at 126.91, five hundreds, boundary share 66.1% and 58.6% of batter runs ![Batting](dashboards/powerbi/screenshots/02-batting.png) |
| **Bowling**: India 7 wickets at 8.06 an over, West Indies 2 wickets at 9.29, best figures Kuldeep Yadav 2/65, best economy Naman Dhir 6.16 ![Bowling](dashboards/powerbi/screenshots/03-bowling.png) | **Phases and Wickets**: powerplay 188 runs, middle 513, death 110, West Indies lost 4 wickets in the death overs, India finished in the 44th over ![Phases and Wickets](dashboards/powerbi/screenshots/04-phases-wickets.png) |
| **Player Comparison**: Gill 223*, four West Indies players both batted and bowled, India used four batters and left seven unused ![Player Comparison](dashboards/powerbi/screenshots/05-player-comparison.png) | |

## What the scorecard shows

- India scored faster in every phase that both sides completed. The powerplay was close (West Indies 9.60, India 9.20). Through the middle overs West Indies dropped to 7.77 while India stayed at 9.33. India only faced 21 balls in the death overs, at 9.71, because the chase ended in over 44. West Indies scored at 7.60 in the last 10 overs and lost 4 wickets there.
- The biggest over was India's 29th, 25 runs. The biggest stand of runs between wickets was West Indies moving from 147 to 329, 182 runs, before Shai Hope was out at the end of the 40th over. That is the change in the fall-of-wicket score, not a named pair. The scorecard files do not say who was at the other end.
- Gill's 223 not out is 152 runs in boundaries (26 fours and 8 sixes), 68.2% of his innings. India's batter runs were 66.1% boundaries. West Indies were 58.6%.
- India's bowlers shared the wickets. Kuldeep 2/65 in 10 overs was the best return, ahead of Jadeja 2/75 and Brar 2/96. Naman Dhir was the most economical, 6.1 overs for 38, and did not take a wicket. There were no maidens.
- Four West Indies players appear on both cards: Roston Chase 29 not out and 0/63, Shamar Joseph 14 not out and 1/52, Alzarri Joseph 8 and 0/89, Keemo Paul 3 and 0/49. India's bowlers did not bat.

## Open the report

1. Clone the repo and open `dashboards/powerbi/IndVsWi2ndOdi.pbip` in Power BI Desktop. On older Desktop builds, turn on the Power BI Project and TMDL preview features first.
2. Go to **Transform data > Edit parameters** and set `DataFolder` to the full path of your local `dashboards/powerbi/extracts` folder, for example `C:\ind-vs-wi-2nd-odi-dashboard\dashboards\powerbi\extracts`. Power Query needs an absolute path. Each table reads `DataFolder` plus `\Match.csv`, `\Innings.csv`, and the other extract names.
3. Click **Refresh**.

Pages, the measure list and the data notes are in [dashboards/powerbi/README.md](dashboards/powerbi/README.md). `POWERBI_STEPS.md` is the earlier field guide for building a single page by hand.

`dashboard.html` is the same match in a browser, with the team slicer at the top right. `dashboard.png` is that page. `dashboard_video.mp4` is the walkthrough of it.

## Sources

The scorecard and the over summaries come from the Indian Express live page, final as on 30 September 2026, 10:54 PM IST, and the PTI scoreboard for the West Indies extras line.

- [Indian Express scorecard](https://indianexpress.com/section/sports/cricket/live-score/india-vs-west-indies-2nd-odi-live-score-full-scorecard-highlights-west-indies-in-india-3-odi-series-2026-inwi09302026270271/)
- [PTI scoreboard](https://www.news18.com/agency-feeds/scoreboard-india-vs-west-indies-2nd-odi-10361356.html)
- [IANS report](https://ianslive.in/2nd-odi-gills-unbeaten-223-rohits-century-sets-up-indias-record-chase-of-406--20260930223210)

A copy of the Indian Express page is in `data/source_indianexpress_snapshot.html`. ESPNcricinfo did not return the scorecard when it was fetched.

## Layout

```
ind-vs-wi-2nd-odi-dashboard/
├── dashboards/powerbi/   Power BI project, extracts, measures, screenshots, walkthrough
├── data/                 scorecard CSVs and the source page
├── dashboard.html        the same match in the browser
├── POWERBI_STEPS.md      field guide for a single page
└── README.md
```

## Photo credits

The browser dashboard uses headshots of Shubman Gill, Rohit Sharma and Virat Kohli from Wikimedia Commons. They are from earlier events, not from this match. Each was cropped to a 300 by 300 headshot. Files are in `assets/players/`.

| Player | Commons file | Author | License |
| --- | --- | --- | --- |
| Shubman Gill | [File:Shubman_Gill.jpg](https://commons.wikimedia.org/wiki/File:Shubman_Gill.jpg) | CRICKETNEXT (via YouTube) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0) |
| Rohit Sharma | [File:Rohit_Sharma_November_2016_(cropped).jpg](https://commons.wikimedia.org/wiki/File:Rohit_Sharma_November_2016_(cropped).jpg) | Bollywood Hungama | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0) |
| Virat Kohli | [File:Virat_Kohli_portrait.jpg](https://commons.wikimedia.org/wiki/File:Virat_Kohli_portrait.jpg) | Anand Anil | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |

The Kohli headshot in `assets/players/kohli.jpg` stays under CC BY-SA 4.0, the same license as its source.
