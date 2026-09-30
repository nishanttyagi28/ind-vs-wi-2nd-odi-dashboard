# IND vs WI 2nd ODI dashboard (Guwahati, 30 Sep 2026)
- dashboard.html: interactive dashboard (Plotly is embedded, so it works offline). The team slicer is at the top right.
- dashboard.png: full-page screenshot. dashboard_video.mp4: 1600x900 walkthrough, about 47 s.
- data/*.csv: clean data. POWERBI_STEPS.md: how to rebuild it in Power BI Desktop.
- assets/players/: square 300px headshots (kohli.jpg, gill.jpg, rohit.jpg), Commons originals in original/, and credits.json.
- build_data.py / make_headshots.py / build_dashboard.py / template.html / capture.py: scripts that regenerate everything (headshots are embedded in dashboard.html as base64).
Sources: Indian Express live scorecard + commentary (final, "as on 30 Sep 2026 10:54 PM IST"):
https://indianexpress.com/section/sports/cricket/live-score/india-vs-west-indies-2nd-odi-live-score-full-scorecard-highlights-west-indies-in-india-3-odi-series-2026-inwi09302026270271/
PTI scoreboard (WI extras): https://www.news18.com/agency-feeds/scoreboard-india-vs-west-indies-2nd-odi-10361356.html
IANS report: https://ianslive.in/2nd-odi-gills-unbeaten-223-rohits-century-sets-up-indias-record-chase-of-406--20260930223210
ESPNcricinfo (blocked the fetch, 403): https://www.espncricinfo.com/series/west-indies-in-india-2026-27-1529215/india-vs-west-indies-2nd-odi-1529228/full-scorecard

## Photo credits
All player photos come from Wikimedia Commons. Each was cropped and resized to a 300×300 headshot. They are from earlier events, not from this match.
| Player | Commons file | Author | License |
|---|---|---|---|
| Shubman Gill | [File:Shubman_Gill.jpg](https://commons.wikimedia.org/wiki/File:Shubman_Gill.jpg) | CRICKETNEXT (via YouTube) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0) |
| Rohit Sharma | [File:Rohit_Sharma_November_2016_(cropped).jpg](https://commons.wikimedia.org/wiki/File:Rohit_Sharma_November_2016_(cropped).jpg) | Bollywood Hungama | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0) |
| Virat Kohli | [File:Virat_Kohli_portrait.jpg](https://commons.wikimedia.org/wiki/File:Virat_Kohli_portrait.jpg) | Anand Anil | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |

The derived Kohli headshot (`assets/players/kohli.jpg`) is shared under CC BY-SA 4.0, the same license as its source.
