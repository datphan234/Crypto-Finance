import re
import requests
import pandas as pd
import plotly.express as px

df=pd.read_csv('metcalfe.csv')
subs=list(df['reddit'])
subredditsize=[]
mktcap=[]


for x in subs:
	data=requests.get('https://frontpagemetrics.com/r/'+x).text
	data=re.findall('h2 class=.*',data)[0]
	data=re.findall('>[0-9,]*<',data)[0]
	data=data.replace('>','').replace('<','').replace(',','')
	subredditsize.append(int(data))
	
df['subredditsize']=subredditsize



for x in list(df['gecko-name']):
	data=requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids='+x+'&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()[0]['market_cap']
	mktcap.append(int(data))

df['mktcap']=mktcap
df['k-value']=df['mktcap']/(df['subredditsize']**2)

fig=px.scatter(df,x='subredditsize',y='mktcap',size='k-value',
				hover_name='gecko-name',text='gecko-name',
				log_x=True,log_y=True,size_max=200,
				template="plotly_dark")

fig.update_xaxes(title_text='Reddit Subscriber',showgrid=False,title_font={'size':30})
fig.update_yaxes(title_text='Market Cap',showgrid=False,title_font={'size':30})
fig.update_layout(title_text="Relative Valuation by Metcalfe's Law on Reddit",
					title_font_size=45,
					title_yanchor='top',
					title_pad_t=30,
					title_pad_b=30,)


fig.show()
