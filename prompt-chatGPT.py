!pip install openai

import openai
openai.api_key = "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"

brief = "Riscrivi questo testo con tono professionale espandendo i concetti che vengono trattati: La presentazione di una richiesta di capitali agli investitori è un processo fondamentale per qualsiasi impresa che desidera finanziare la propria crescita interna. Questa opzione offre una prospettiva intrigante per le aziende, in quanto è possibile ottenere un finanziamento tailor made in termini di struttura, durata e modalità di rimborso. Per presentare una richiesta di capitali, è necessario preparare una serie di documenti che attestino la solidità dell'azienda e le prospettive future che si vogliono aprire. Tra questi, i bilanci realizzati fino al più recente, la visura camerale, l'estratto della Centrale Rischi Italia e il business plan sono tutti elementi importanti. Inoltre, presentare un Information Memorandum può essere di grande utilità per gli investitori.Questo documento può esporre la storia dell'azienda, il mercato di riferimento e l'attuale posizionamento, presentare il team di management ed esporre il business model, in riferimento al know-how aziendale. È importante sottolineare che il processo di presentazione della richiesta di capitali può essere complesso e richiedere competenze specifiche. Per questo motivo, è consigliabile affidarsi a professionisti del settore, come Azimut Direct, che offre soluzioni personalizzate per connettere il mondo delle imprese a quello degli investitori. Grazie alla loro esperienza, è possibile presentare una richiesta di capitali completa e accurata, migliorando le possibilità di ottenere un finanziamento per sviluppare il proprio business al meglio e sostenere lo sviluppo economico interno."

model_engine = "text-davinci-003"
while True:
  prompt = brief
  completion = openai.Completion.create(engine = model_engine, 
                                        prompt = prompt, 
                                        max_tokens = 2500, 
                                        temperature = 0.8)
  message = completion.choices[0].text
  print(message)
