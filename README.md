# IND vs WI 2nd ODI dashboard (Guwahati, 30 Sep 2026)
- dashboard.html: interactive dashboard (Plotly is embedded, so it works offline). The team slicer is at the top right.
- dashboard.png: full-page screenshot. dashboard_video.mp4: 1600x900 walkthrough, about 47 s.
- data/*.csv: clean data. POWERBI_STEPS.md: how to rebuild it in Power BI Desktop.
- build_data.py / build_dashboard.py / template.html / capture.py: scripts that regenerate everything.
Sources: Indian Express live scorecard + commentary (final, "as on 30 Sep 2026 10:54 PM IST"):
https://indianexpress.com/section/sports/cricket/live-score/india-vs-west-indies-2nd-odi-live-score-full-scorecard-highlights-west-indies-in-india-3-odi-series-2026-inwi09302026270271/
PTI scoreboard (WI extras): https://www.news18.com/agency-feeds/scoreboard-india-vs-west-indies-2nd-odi-10361356.html
IANS report: https://ianslive.in/2nd-odi-gills-unbeaten-223-rohits-century-sets-up-indias-record-chase-of-406--20260930223210
ESPNcricinfo (blocked the fetch, 403): https://www.espncricinfo.com/series/west-indies-in-india-2026-27-1529215/india-vs-west-indies-2nd-odi-1529228/full-scorecard
