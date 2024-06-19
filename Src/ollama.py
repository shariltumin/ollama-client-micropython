
use=__import__
socket = use('socket')
sleep = use('time').sleep

bytes_type = type(b'abc')

class screen():
    def __init__(my):
        my.put=use('sys').stdout.write
        my.cn,my.cc,my.dr=5,0,'r' # r/l/s
    def clear_screen(my):
        my.put('\033[2J\033[H')  # Clear screen and 
                                 # move cursor to top-left corner
    def llp(my,c,t):
        my.put(c); sleep(t)
        my.cc+=1

    def rrp(my,c,t):
        my.put('\033[1D')
        my.put(c); sleep(t)
        my.put('\033[1D')
        my.cc-=1

    def animt(my):
        if my.cc<my.cn and my.dr=='r': my.llp('>',0.01); return
        else: my.dr = 'l'
        if my.cc>0 and my.dr=='l': my.rrp('<',0.01); return
        else: my.dr='r'; return

class _Response:
    def __init__(my, f):
        my.raw = f
        my.encoding = "utf-8"
        my._cached = None

    def close(my):
        if my.raw:
           my.raw.close()
           my.raw = None
           my._cached = None

def request(
    method,
    url,
    data=None,
    headers={},
    stream=None,
    timeout=None,
    parse_headers=True,
):
    redirect = None  # redirection url, None means no redirection
    chunked_data = data and getattr(data, "__next__", None) and not getattr(data, "__len__", None)

    try:
        proto, dummy, host, path = url.split("/", 3)
    except ValueError:
        proto, dummy, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
    elif proto == "https:":
        try:
           ssl = use('tls') # for ESP32
        except:
           ssl = use('ssl') # for unix port
        port = 443
    else:
        raise ValueError("Unsupported protocol: " + proto)

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)

    ai = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)
    ai = ai[0]

    resp_d = None
    if parse_headers is not False:
        resp_d = {}

    s = socket.socket(ai[0], socket.SOCK_STREAM, ai[2])

    if timeout is not None:
        s.settimeout(timeout)

    try:
        s.connect(ai[-1])
        if proto == "https:":
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.verify_mode = ssl.CERT_NONE
            s = context.wrap_socket(s, server_hostname=host)
        s.write(b"%s /%s HTTP/1.0\r\n" % (method, path))
        if "Host" not in headers:
            s.write(b"Host: %s\r\n" % host)
        # Iterate over keys to avoid tuple alloc
        for k in headers:
            s.write(k)
            s.write(b": ")
            s.write(headers[k])
            s.write(b"\r\n")
        if data:
            if chunked_data:
                s.write(b"Transfer-Encoding: chunked\r\n")
            else:
                s.write(b"Content-Length: %d\r\n" % len(data))
        s.write(b"Connection: close\r\n\r\n")
        if data:
            if chunked_data:
                for chunk in data:
                    s.write(b"%x\r\n" % len(chunk))
                    s.write(chunk)
                    s.write(b"\r\n")
                s.write("0\r\n\r\n")
            else:
                s.write(data)

        l = s.readline()
        l = l.split(None, 2)
        if len(l) < 2:
            # Invalid response
            raise ValueError("HTTP error: BadStatusLine:\n%s" % l)
        status = int(l[1])
        reason = ""
        if len(l) > 2:
            reason = l[2].rstrip()
        while True:
            l = s.readline()
            if not l or l == b"\r\n":
                break
            if l.startswith(b"Transfer-Encoding:"):
                if b"chunked" in l:
                    raise ValueError("Unsupported " + str(l, "utf-8"))
            elif l.startswith(b"Location:") and not 200 <= status <= 299:
                if status in [301, 302, 303, 307, 308]:
                    redirect = str(l[10:-2], "utf-8")
                else:
                    raise NotImplementedError("Redirect %d not yet supported" % status)
            if parse_headers is False:
                pass
            elif parse_headers is True:
                l = str(l, "utf-8")
                k, v = l.split(":", 1)
                resp_d[k] = v.strip()
            else:
                parse_headers(l, resp_d)
    except OSError:
        s.close()
        raise

    if redirect:
        s.close()
        if status in [301, 302, 303]:
            return request("GET", redirect, None, None, headers, stream)
        else:
            return request(method, redirect, data, json, headers, stream)
    else:
        resp = _Response(s)
        resp.status_code = status
        resp.reason = reason
        if resp_d is not None:
            resp.headers = resp_d
        return resp

def parse_g(s):
   r='response'
   c='context'
   # Remove leading and trailing curly braces
   if type(s)==bytes_type: s=s.decode('ascii').strip('{}')
   s=s.strip('{}')
   ps=s.split(',"')

   rs=cs= ''
   for pa in ps:
      v = pa.split(':') # key:v[0], value:v[1]
      k = v[0].strip().strip('"')
      if k==c: cs=v[1]
      if k==r: rs=v[1].strip('"')
      if cs!='': return ('c', cs)
      elif rs!='': return ('r', rs.replace('\\n','\n'))
   return ('', '')

def parse_c(s):
   lm = len('"message":')
   lw = len('"content":"')
   if type(s)==bytes_type: s=s.decode('ascii').strip('{}')
   try:
      m1 = s.find('"message":')
      m2 = s.find(',"done":')
      dat = s[m1+lm:m2]
      w1 = dat.find('"content":')
      w2 = dat.find('"}')
      what = dat[w1+lw:w2]
   except Exception as e:
      print(e)
      return ''
   else:
      return what

class Generate():
   def __init__(my, protocol, host, model='llama2', stream=False):
       my.url = f"{protocol}://{host}/api/generate"
       my.protocol = protocol
       my.model = model
       my.blk = 200
       if stream:
          my.stream = "true"
          my.sc=screen()
       else:
          my.stream = "false"
          my.sc=None
       my.cntx = None
       if my.protocol=='https':
          my.stream = "false" # TLS can't take stream data in MP
          my.sc=None
       # Set the headers
       my.headers = {
          "Content-Type": "application/json"
       }
   def clear(my):
       my.cntx = None
       if my.sc != None:
          my.sc.clear_screen()
   def chat(my, prom):
       if my.cntx == None:
          what = f'''{{
  "model": "{my.model}",
  "prompt":"{prom}",
  "stream":{my.stream} }}'''
       else:
          what = f'''{{
  "model": "{my.model}",
  "prompt":"{prom}",
  "context": {my.cntx},
  "stream":{my.stream} }}'''

       response =  request('POST', my.url, headers=my.headers, data=what)

       # Handle the response
       if response.status_code != 200:
          print('Web request error:', response.status_code)
          return ''

       MSG = b''
       res=''
       if my.stream=='true':
          while True:
             while True:
                msg = response.raw.recv(my.blk)
                # print('MMM:', msg)
                MSG += msg
                if len(msg)<my.blk: break
             if len(msg)==0: break
             if my.sc != None: my.sc.animt()
             k,w = parse_g(MSG)
             if w:
                if k=='r': res += w
                elif k=='c': my.cntx = w.strip().strip('"')
             MSG = b''
          return res
       else: # https
          msg = response.raw.read()
          #print('MMM:', msg)
          for ms in msg.decode().split('{"model":'):
              k,w = parse_g(ms)
              if w:
                 if k=='r': res += w
                 elif k=='c': my.cntx = w.strip().strip('"')
          return res

class Chat():
   def __init__(my, protocol, host, model='llama2', ctx_cnt=4, stream=False):
       my.url = f"{protocol}://{host}/api/chat"
       my.protocol = protocol
       my.model = model
       my.blk = 200
       if stream:
          my.stream = "true"
          my.sc=screen()
       else:
          my.stream = "false"
          my.sc=None
       my.ctx_cnt = ctx_cnt
       my.ctx = [] # context history
       if my.protocol=='https':
          my.stream = "false" # TLS can't take stream data in MP
          my.sc=None
       # Set the headers
       my.headers = {
          "Content-Type": "application/json"
       }
   def clear(my):
       my.ctx = []
       if my.sc != None:
          my.sc.clear_screen()
   def chat(my, prom):
       uprom = f'{{"role":"user", "content":"{prom}"}}'
       my.ctx.append(uprom)
       what = f'{{ "model":"{my.model}", "messages":[{','.join(s for s in my.ctx)}], "stream": {my.stream} }}'

       response = request('POST', my.url, headers=my.headers, data=what)

       # Handle the response
       if response.status_code != 200: 
          print('Web request error:', response.status_code)
          print(what)
          return ''

       MSG = b''
       res = ''
       if my.stream=='true':
          while True:
             while True:
                msg = response.raw.recv(my.blk)
                MSG += msg
                if len(msg)<my.blk: break
             if len(msg)==0: break
             if my.sc != None: my.sc.animt()
             what = parse_c(MSG)
             if what:
                res += what
             else:
                break
             MSG = b''
       else: # https
          while True:
             while True:
                msg = response.raw.read()
                MSG += msg
                if len(msg)==0: break
             what = parse_c(MSG)
             if what:
                res += what
             else:
                break
             MSG = b''
       if len(my.ctx)>my.ctx_cnt: my.ctx = my.ctx[2:]
       bot = f'{{"role": "assistant", "content": "{res.replace('\\n',' ')}'
       if len(bot)>=100:
          bot=bot[:100]
       if bot: bot+='"}'
       my.ctx.append(bot)   
       return (res.replace('\\n','\n'))

