
Please download the latest version of the Ollama application from ollama.com by following the instructions below:

```sh
$ cd ~/bin
$ curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama
$ chmod +x ollama
```

The Ollama application shown here is for Linux. For complete documentation, please visit: [Ollama Documentation](https://github.com/ollama/ollama/tree/main/docs).

The official Ollama documentation provides instructions on how to install Ollama and configure it to start at boot time. However, we will start Ollama manually each time we want to use it.

Now that you have Ollama in your bin directory and have made it executable, you can manually start Ollama in a terminal window.

```sh
$ export OLLAMA_HOST=0.0.0.0:11434
$ export OLLAMA_FLASH_ATTENTION=1
$ ollama serve
```

We set `OLLAMA_HOST` so that we can connect to it from any machine in our local network. The `OLLAMA_FLASH_ATTENTION` setting is necessary if we plan to run the Qwen2 model. 

To start the Ollama server, open a terminal window and execute the command. You will see logging information being printed out. Keep the terminal open, as the Ollama program is bound to it. To stop the running Ollama, press `<Ctrl>+C`.

If this is the first time the program is running, there are no models connected to your Ollama server yet. You need to "pull" models in order to use them.

Open a new terminal window on the same PC where your Ollama server is running. Then, to download the models "llama2," "llama3," and "qwen2," use the following commands:

```sh
ollama pull llama2
ollama pull llama3
ollama pull qwen2
$ ollama list
```

The last command will list all the models currently available to our Ollama server.

But if we have several machines and want to run 'chat' from a different PC, let's assume your Ollama server is running on a PC with IP "192.168.4.27". You need to have the Ollama program on that machine as well. Assuming it's a Linux PC, you can copy Ollama from the server to that machine (using `scp`, for example). Then, in a terminal window on that PC, you would do the following:

```sh
$ export OLLAMA_HOST=192.168.4.27:11434
$ ollama list
$ ollama run llama2
```

By default, when Ollama runs a command, such as `ollama list`, an API call is made to the localhost. The log will show this action.

```
[GIN] 2024/06/19 - 16:50:31 | 200 |    5.091091ms |       127.0.0.1 | GET      "/api/tags"
```

The `ollama serve` command will start a web server listening on port 11434. The Ollama server has well-defined API endpoints, with '/api/tags' being one of them.

There is no way the Ollama program can be installed on an MCU due to resource constraints. From an MCU running MicroPython, we will make web requests to 'api/generate' and 'api/chat' using a module called 'ollama.py'.

Below is a transcript of a session running the test script on an ESP8266.

```
$ mpremote mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyUSB0
Use Ctrl-] or Ctrl-x to exit this shell
>
MicroPython v1.22.2 on 2024-02-22; ESP module with ESP8266
Type "help()" for more information.
>>> import test_client
wifi connected? True

===========================
>> Please give short and concise answers to the following questions
><<<<

Of course! Ill do my best to provide brief responses. Please go ahead and ask your questions:
===========================
>> Where is the hotest place on earth, what was recorded
<<<<<
The hottest place on Earth is Al 'Aziziyah, Saudi Arabia, which reached a recorded temperature of 134°F (56.7°C) on June 21, 2010.
===========================
>> the coldest
>>>><
Antarctica is the coldest continent on Earth, with an avera
===========================
>> how about the driest
<<<<<
The Atacama Desert in Chile is considered one of the driest p
===========================
>> wettest?
>><<<
The wettest place on Earth is Mawsynram, India, which averages ove
===========================
>> make a summary of our conversation
><<<<
We discussed various locations around the world and their climatic conditions. Here are the summaries of each location:

Hottest place on Earth: Al 'Aziziyah, Saudi Arabia (recorded temperature of 134°F or 56.7°C)
Coldest continent: Antarctica
Driest desert: Atacama Desert in Chile
Wettest place: Mawsynram, India (averages over 400 inches or 10,000 mm of rainfall per year)

===========================
>> Tell me a joke
><<<<
Sure! Here's one:

Why don't scientists trust atoms? Because they make up everything!

I hope you found that amusing! Do you want to hear another one?
===========================
>> another one
>>>><
Of course! Here's another one:

Why don't lobsters share? Because they're shellfish.
===========================
>> another one with monkey in it
><<<<
Haha, okay! Here's one with a monkey:  Why did the monkey get kicked out of the library? Because he was caught monkeying around!
===========================
>> very funny, ok last one
>>><<
Okay, no problem! Here's another one:  Why don't eggs tell jokes? They'd crack each other up!
>>> 
```

To summarize:
1. The Ollama server runs a web server.
2. It listens on port 11434.
3. A client can send requests to its API endpoints.
4. A formatted response is sent back to the client.
5. The client needs to parse and consume the response.
