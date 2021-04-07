import requests
import notification
import dialogs

"""
Python + Iphone

Ações Brasileiras: Este programa tem a intenção de retornar a variacao diaria de acoes assim como a variação acumulada,
 usando como vetores a sigla da ação, posição e valor de compra. 

"""

stocks=[['CIEL3',600,10.91],['MGLU3',200,25.27],['PETR4',100,22.05],['LAME4',100,34.78],['PETR4',200,27.30]]



stocksf,stocksd=[],[]
stocksd.append("Variação Diaria:\n")
stocksf.append("Valores Finais:\n")


for stock in stocks:
	r = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+stock[0]+'.SA&apikey=YourApiKeyHere')
	data = r.json()
	r1=data['Global Quote']
	diaria = r1['01. symbol'] + " " + r1['05. price'] + " " + r1['10. change percent']
	stocksd.append(diaria)
	vlrfinal=( float(r1['05. price']) - stock[2])
	final =r1['01. symbol']+ " " + str(round(stock[2]*stock[1],0))+ " " + str(round(stock[1]* vlrfinal,2))
	stocksf.append(final)



listaf='\n'.join(stocksd)+'\n\n' + '\n'.join(stocksf)


noti=notification.schedule(message=listaf,  title="Lista de Ações \U0001F428")
alerta=dialogs.alert("Lista de Ações \U0001F428",listaf,"\U0001F428 OK \U0001F428",hide_cancel_button=True)


