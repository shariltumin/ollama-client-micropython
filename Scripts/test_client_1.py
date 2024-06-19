
use=__import__
sleep = use('time').sleep
#config = use('config_2c') # Chat
config = use('config_1g') # Generate -- good for these type of prompts

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
promps = ['If Top is 3 inches taller then Dick, and Dick is 2 inches taller than Harry, how much taller is Tom than Harry', 'Can Tom be taller than himself', 'Can a sister be taller than her brother', 'Can two siblings each be taller than the other']

oc.clear()
for prom in promps:
   print('===========================')
   print('>>', prom)
   res = oc.chat(prom)
   print()
   print(res)
   sleep(1)

# 2.
promps = ['On a map, which compass direction is usually left?', 'Can fish run?', 'If the door is locked, whatmust you do first before opening it', 'Which was invented first, cars, ships, or planes']

oc.clear()
for prom in promps:
   print('===========================')
   print('>>', prom)
   res = oc.chat(prom)
   print()
   print(res)
   sleep(1)

