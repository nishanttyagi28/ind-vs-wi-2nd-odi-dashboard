import re, csv, os
D='/workspace/ind-wi-dashboard/data'
def w(name, header, rows):
    with open(os.path.join(D,name),'w',newline='') as f:
        c=csv.writer(f); c.writerow(header); c.writerows(rows)

w('match_info.csv',
 ['match_id','match','series','format','gender','date','venue','city','toss','team1','team1_score','team1_wickets','team1_overs','team1_extras','team1_extras_detail','team2','team2_score','team2_wickets','team2_overs','team2_extras','team2_extras_detail','result','series_status','top_scorer','best_bowler','source_scorecard','source_report'],
 [[1529228,'India vs West Indies, 2nd ODI','West Indies tour of India 2026/27 (3-match ODI series)','ODI (Day/Night)','Men','2026-09-30','Barsapara Cricket Stadium (ACA Stadium)','Guwahati',
   'West Indies sent in to bat (India fielded first)',
   'West Indies',405,7,'50.0',23,'b 1, nb 1, w 20 (PTI)',
   'India',406,2,'43.3',22,'breakdown not published in sources (derived: total minus batter runs)',
   'India won by 8 wickets (39 balls remaining)','India lead 3-match series 2-0',
   'Shubman Gill 223* (133)','Kuldeep Yadav 2/65 (10 ov)',
   'https://indianexpress.com/section/sports/cricket/live-score/india-vs-west-indies-2nd-odi-live-score-full-scorecard-highlights-west-indies-in-india-3-odi-series-2026-inwi09302026270271/',
   'https://www.news18.com/agency-feeds/scoreboard-india-vs-west-indies-2nd-odi-10361356.html']])

bat=[ # team, innings, pos, batter, dismissal, runs, balls, 4s, 6s, not_out
('West Indies',1,1,'John Campbell','c Naman Dhir b Gurnoor Brar',101,68,9,5,0),
('West Indies',1,2,'Keacy Carty','c Naman Dhir b Prasidh Krishna',9,10,2,0,0),
('West Indies',1,3,'Shai Hope','c Auqib Nabi b Kuldeep Yadav',104,94,8,3,0),
('West Indies',1,4,'Amir Jangoo','c Ruturaj Gaikwad b Ravindra Jadeja',114,77,13,3,0),
('West Indies',1,5,'Sherfane Rutherford','c sub (Yashasvi Jaiswal) b Gurnoor Brar',0,1,0,0,0),
('West Indies',1,6,'Roston Chase','not out',29,25,4,0,1),
('West Indies',1,7,'Keemo Paul','c Virat Kohli b Kuldeep Yadav',3,8,0,0,0),
('West Indies',1,8,'Alzarri Joseph','c Rohit Sharma b Ravindra Jadeja',8,10,1,0,0),
('West Indies',1,9,'Shamar Joseph','not out',14,8,1,1,1),
('India',2,1,'Rohit Sharma','lbw b Jayden Seales',101,75,10,6,0),
('India',2,2,'Shubman Gill','not out',223,133,26,8,1),
('India',2,3,'Virat Kohli','c Sherfane Rutherford b Shamar Joseph',29,19,3,1,0),
('India',2,4,'Ruturaj Gaikwad','not out',31,37,2,0,1),
]
rows=[]
for t,i,p,n,d,r,b,f,s,no in bat:
    rows.append([1529228,i,t,p,n,d,r,b,f,s,no,round(r*100/b,2),f*4+s*6])
w('batting.csv',['match_id','innings','team','bat_pos','batter','dismissal','runs','balls','fours','sixes','not_out','strike_rate','boundary_runs'],rows)
w('did_not_bat.csv',['match_id','team','batter'],[[1529228,'West Indies',x] for x in ['Jayden Seales','Vitel Lawes']]+[[1529228,'India',x] for x in ['Ravindra Jadeja','KL Rahul','Naman Dhir','Auqib Nabi','Kuldeep Yadav','Gurnoor Brar','Prasidh Krishna']])

bowl=[ # bowling team, innings bowled in, bowler, overs, maidens, runs, wkts
('India',1,'Prasidh Krishna','5',0,45,1),('India',1,'Auqib Nabi','8.5',0,84,0),('India',1,'Gurnoor Brar','10',0,96,2),
('India',1,'Naman Dhir','6.1',0,38,0),('India',1,'Ravindra Jadeja','10',0,75,2),('India',1,'Kuldeep Yadav','10',0,65,2),
('West Indies',2,'Jayden Seales','8',0,78,1),('West Indies',2,'Alzarri Joseph','8',0,89,0),('West Indies',2,'Shamar Joseph','6',0,52,1),
('West Indies',2,'Keemo Paul','3',0,49,0),('West Indies',2,'Roston Chase','8.3',0,63,0),('West Indies',2,'Vitel Lawes','10',0,73,0)]
rows=[]
for t,i,n,o,m,r,wk in bowl:
    ov,_,bl=o.partition('.'); balls=int(ov)*6+int(bl or 0)
    rows.append([1529228,i,t,n,o,balls,m,r,wk,round(r*6/balls,2)])
w('bowling.csv',['match_id','innings','bowling_team','bowler','overs','balls','maidens','runs_conceded','wickets','economy'],rows)

fow=[('West Indies',1,1,37,'Keacy Carty','5.0'),('West Indies',1,2,147,'John Campbell','18.1'),('West Indies',1,3,329,'Shai Hope','40.0'),
('West Indies',1,4,330,'Sherfane Rutherford','40.2'),('West Indies',1,5,348,'Amir Jangoo','42.2'),('West Indies',1,6,369,'Keemo Paul','45.1'),
('West Indies',1,7,385,'Alzarri Joseph','47.3'),('India',2,1,255,'Rohit Sharma','26.2'),('India',2,2,320,'Virat Kohli','32.1')]
w('fall_of_wickets.csv',['match_id','batting_team','innings','wicket_no','score','batter_out','over'],[[1529228,*x] for x in fow])

# over-by-over from Indian Express commentary over summaries
t=open('/tmp/ie.txt').read()
ms=re.findall(r'(\d+) over \d+ \| (\d+) Runs? \| \w+: (\d+)/(\d+)',t)
wi=ms[:50]; ind=ms[50:]
assert wi[0][2]=='405' and ind[0][2]=='400'
rows=[]
for team,inn,lst in [('West Indies',1,wi),('India',2,ind)]:
    for o,r,s,wk in sorted(lst,key=lambda x:int(x[0])):
        rows.append([1529228,inn,team,int(o),int(r),int(s),int(wk),6,'IE commentary over summary'])
# India final partial over 44 (43.1-43.3): 4,1,1 per ball-by-ball commentary -> 406/2
rows.append([1529228,2,'India',44,6,406,2,3,'partial over (3 balls) from ball-by-ball commentary'])
w('overs.csv',['match_id','innings','batting_team','over_no','runs_in_over','cumulative_runs','cumulative_wickets','legal_balls','note'],rows)
# sanity
for team,inn in [('West Indies',1),('India',2)]:
    rr=[x for x in rows if x[2]==team]; print(team,sum(x[4] for x in rr),rr[-1][5])
