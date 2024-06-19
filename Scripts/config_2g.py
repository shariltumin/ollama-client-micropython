
# wifi? 
# wifi = {} # no wifi
# need wifi
wifi = {'SSID':"dlink-3530",'PWD':"cabbp73520" }

# ollama 
#srv = {
#  'protocol': 'https', 
#  'server'  : '4faf36c87d401.notebooksb.jarvislabs.net', # ollama instance
#  'model'   : 'llama3:8b',
#  'api'     : 'chat' # 'gent'|'chat' API end-point
##  'api'     : 'gent' # 'gent'|'chat' API end-point
#}

# ollama
srv = {
  'protocol': 'http',
  'server'  : '192.168.4.134:11434', # OLLAMA_HOST=0.0.0.0 ollama serve
#  'server'  : '192.168.4.27:11434', # OLLAMA_HOST=0.0.0.0 ollama serve
#  'server'  : '192.168.4.141:11434', # OLLAMA_HOST=0.0.0.0 ollama serve
  'model'   : 'llama2',
  'api'     : 'gent' # 'gent'|'chat' API end-point
#  'api'     : 'chat' # 
}
# client
cln = {
  'ctx_cnt': 10,
#  'stream': False
  'stream': True
}

