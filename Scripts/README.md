
The `test_client.py` is a test script that demonstrates how the Ollama module can be utilized.

The `ollama.mpy` is the compiled version of the module, used to conserve RAM.

There are two instances of prompts in the test scripts. Feel free to modify them for your own test runs.

The configuration files serve as examples of what is needed to set up the client properly. Currently, there are two ways to make API requests to the server.

1. api/generate
2. api/chat

Depending on the model and prompt used, you will receive different responses from the server. Sometimes, you might even encounter an HTTP error reply.

This is how you might want to proceed:

```sh
$ mpremote mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyACM0
Use Ctrl-] or Ctrl-x to exit this shell
>
MicroPython v1.24.0-preview.10.gc1a6b95bf.dirty on 2024-06-01; ESP32-C3 BlueBoard (KAKI5-NTNG) with ESP32-C3
>>> import test_client
wifi connected? True

===========================
>> Please give short and concise answers to the following questions
>><<<

Of course! I'll do my best to provide brief responses. Please go ahead and ask your questions.
===========================
>> Where is the hotest place on earth, what was recorded
>><<<
The hottest place on Earth is Death Valley National Park in California USA. The highest recorded temperature there was 134°F (56.7°C) on July 10 1913.
===========================
>> the coldest
>>>><
The coldest place on Earth is Antarctica specifically the region around the South Pole. The coldest temperature ever recorded there was -128.6°F (-89.2°C) on July 21 1983 at the Russian Vostok Station.
===========================
>> how about the driest
<<<<<
The driest place on Earth is Atacama Desert in Chile. The Atacama Desert is one of the driest places on Earth with some areas receiving less than 0.01 inches (0.25 mm) of rainfall per year. The driest location in the Atacama Desert is the Dry Valley which has not seen any significant rainfall in over 400 years.
===========================
>> wettest?
>><<<
The wettest place on Earth is Mawsynram in Meghalaya India. It receives an average of 46 meters (151 inches) of rainfall per year making it the wettest place on Earth. The village experiences a subtropical monsoon climate with heavy rainfall throughout the.
===========================
>> make a summary of our conversation
><<<<
Sure! Here's a summary of our conversation

* Hottest place on Earth Death Valley National Park California (recorded temperature of 134°F or 56.7°C)
* Coldest place on Earth Antarctica (specifically the South Pole region with a recorded temperature of -128.6°F or -89.2°C)
* Driest place on Earth Atacama Desert in Chile (some areas receive less than 0.01 inches or 0.25 mm of rainfall per year)
* Wettest place on Earth Mawsynram Meghalaya India (receives an average of 46 meters or 151 inches of rainfall per year)

===========================
>> Tell me a joke
>>>><
Sure! Here's one

Why don't scientists trust atoms?
Because they make up everything!

I hope you found that amusing. you want to hear another just let me know!
===========================
>> another one
>><<<
Of course! Here's another one

Why don't lobsters share?
Because they're shellfish!

I hope that brought a smile to your face. Do you want to hear another joke?
===========================
>> another one with monkey in it
>>>><
Sure here's one with a monkey theme

Why did the monkey get kicked out of the library?
Because he was caught monkeying!

I hope you found that one amusing. Do you want to hear another joke?
===========================
>> very funny, ok last one
>>>><
Great! Here's one more

Why don't eggs tell jokes?
They'd crack each other up!

I hope you found that one amusing. If you want to hear another joke just let me know!
```
