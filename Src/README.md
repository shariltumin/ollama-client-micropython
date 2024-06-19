
Here is where you can find the source code for "ollama.py".

# screen
This class implements screen functions used to display the process of collecting streaming data from the server. It's nice to see activity while waiting for a reply.

# \_Response
This class implements the data structures needed by the request function.

# request
Shamelessly copied from the official MicroPython requests library, slightly modified to work with the Ollama server.

# parse_g
A utility function to parse data received from the server for the 'api/generate' call, without using the json library to save memory.

# parse_c
A utility function to parse data received from the server for the 'api/chat' call, without using the json library to save memory.

# Generate
The class implements the client for the 'api/generate' call.

# Chat
The class implements the client for the 'api/chat' call.

To use ollama.py, you'll need a config file. The config_1LC.py provides an example configuration for a locally hosted Ollama server. Meanwhile, the config_1RR.py serves as an example for configuring a cloud-hosted Ollama server, specifically running on the jarvislabs.net virtual server in this instance.
