
# wifi? 
# wifi = {} # no wifi
# need wifi
wifi = {'SSID':"Your-SSID",'PWD':"Your-PWD" }

# cloud ollama 
srv = {
  'protocol': 'https', 
  'server'  : '4faf36c87d401.notebooksb.jarvislabs.net', # ollama instance
  'model'   : 'llama3:8b',
  #'api'     : 'chat' # 'gent'|'chat' API end-point
  'api'     : 'gent' # 
}

# client
cln = {
  'ctx_cnt': 10,
  'stream': False
}

