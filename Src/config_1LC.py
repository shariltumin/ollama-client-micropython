
# wifi? 
# wifi = {} # no wifi
# need wifi
wifi = {'SSID':"Your-SSID",'PWD':"Your-PWD" }

# local ollama
srv = {
  'protocol': 'http',
  'server'  : '192.168.4.27:11434', # OLLAMA_HOST=0.0.0.0 ollama serve
  'server'  : '192.168.4.141:11434', # OLLAMA_HOST=0.0.0.0 ollama serve
  'model'   : 'llama2',
  #'api'     : 'gent' # 'gent'|'chat' API end-point
  'api'     : 'chat' # 
}
# client
cln = {
  'ctx_cnt': 10,
  'stream': False
}

