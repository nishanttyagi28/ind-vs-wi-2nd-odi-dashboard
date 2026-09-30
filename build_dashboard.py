import pandas as pd, json, os, plotly
B='/workspace/ind-wi-dashboard'; D=B+'/data'
bat=pd.read_csv(D+'/batting.csv'); bowl=pd.read_csv(D+'/bowling.csv'); fow=pd.read_csv(D+'/fall_of_wickets.csv')
ov=pd.read_csv(D+'/overs.csv'); mi=pd.read_csv(D+'/match_info.csv').iloc[0]; dnb=pd.read_csv(D+'/did_not_bat.csv')
data=dict(bat=bat.to_dict('records'),bowl=bowl.to_dict('records'),fow=fow.to_dict('records'),ov=ov.to_dict('records'),
          mi={k:(v.item() if hasattr(v,'item') else v) for k,v in mi.items()},dnb=dnb.to_dict('records'))
pjs=open(os.path.join(os.path.dirname(plotly.__file__),'package_data','plotly.min.js')).read()
html=open(B+'/template.html').read().replace('/*PLOTLYJS*/',pjs).replace('/*DATA*/',json.dumps(data))
open(B+'/dashboard.html','w').write(html); print('ok',len(html))
