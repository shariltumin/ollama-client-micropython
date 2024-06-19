
# wifi? 
# wifi = {} # no wifi
# need wifi
wifi = {'SSID':"your-ssid",'PWD':"your-pwd" }

# ollama
srv = {
  'protocol': 'http',
  'server'  : '192.168.4.134:11434', # OLLAMA_HOST=0.0.0.0 ollama serve
#  'server'  : '192.168.4.27:11434', # OLLAMA_HOST=0.0.0.0 ollama serve
#  'server'  : '192.168.4.141:11434', # OLLAMA_HOST=0.0.0.0 ollama serve
  'model'   : 'llama3',
  'api'     : 'gent' # 'gent'|'chat' API end-point
#  'api'     : 'chat' # 
}
# client
cln = {
  'ctx_cnt': 10,
#  'stream': False
  'stream': True
}

