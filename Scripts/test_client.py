
use=__import__
sleep = use('time').sleep
config = use('config_2c') # Chat
#config = use('config_2g') # Generate

if config.wifi:
   network=use('network')
   # setup Wifi
   network.WLAN(network.AP_IF).active(False)
   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)
   wlan.connect(config.wifi['SSID'], config.wifi['PWD'])
   cnt = 0
   while not wlan.isconnected():
      print('waiting for wifi...')
      if cnt>5:
         machine=use('machine')
         print("No Wifi, can't continue, reset in 5 sec")
         sleep(5)
         machine.soft_reset()
      sleep(5)
      cnt+=1
   print('wifi connected?', wlan.isconnected())

if config.srv['api'] == 'gent':
   Generate=use('ollama').Generate
   protocol = config.srv['protocol']
   server = config.srv['server']
   model = config.srv['model']
   oc = Generate(
        # server
        config.srv['protocol'], 
        config.srv['server'], 
        config.srv['model'], 
        # client
        config.cln['stream'])
elif config.srv['api'] == 'chat':
   Chat=use('ollama').Chat
   oc = Chat(
        # server
        config.srv['protocol'], 
        config.srv['server'], 
        config.srv['model'], 
        # client
        config.cln['ctx_cnt'], # number of promps x 2
        config.cln['stream'] ) 
else:
   print(f"Api end-point {config.srv['api']} not supported")
   oc = None

# 1.
promps = ['Please give short and concise answers to the following questions', 'Where is the hotest place on earth, what was recorded', 'the coldest', 'how about the driest', 'wettest?', 'make a summary of our conversation']

oc.clear()
for prom in promps:
   print('===========================')
   print('>>', prom)
   res = oc.chat(prom)
   print()
   print(res)
   sleep(1)

# 2.
promps = ['Tell me a joke', 'another one', 'another one with monkey in it', 'very funny, ok last one']

oc.clear()
for prom in promps:
   print('===========================')
   print('>>', prom)
   res = oc.chat(prom)
   print()
   print(res)
   sleep(1)

