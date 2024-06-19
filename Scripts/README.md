
The `test_client.py` is a test script that demonstrates how the Ollama module can be utilized.

The `ollama.mpy` is the compiled version of the module, used to conserve RAM.

There are two instances of prompts in the test scripts. Feel free to modify them for your own test runs.

The configuration files serve as examples of what is needed to set up the client properly. Currently, there are two ways to make API requests to the server.

1. api/generate
2. api/chat

Depending on the model and prompt used, you will receive different responses from the server. Sometimes, you might even encounter an HTTP error reply.

This is how you might want to proceed:

```
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
There is an interesting video titled "The Turing Lectures: The Future of Generative AI" that you might find interesting. You can watch it [here](https://www.youtube.com/watch?v=2kSl0xkq2lM).

The test script `test_client_1.py` uses prompts shown in that video. You can learn a lot about how different models respond to the same set of questions. There are significant improvements in Llama3 compared to Llama2. The "chat" API responds differently compared to the "generate" API.

For this type of questioning, the "generate" API works best.

Below is a transcript of running the test script using Llama3 and the "generate" API call.

```
>>> 
MPY: soft reboot
MicroPython v1.22.2 on 2024-02-22; Generic ESP32 module with ESP32
Type "help()" for more information.
>>> 
Remount local directory ./ at /remote
>>> import test_client_1
wifi connected? True

===========================
>> If Top is 3 inches taller then Dick, and Dick is 2 inches taller than Harry, how much taller is Tom than Harry
>><<<
A nice simple math problem!

Let's break it down step by step1. Top is 3 inches taller than Dick.
2. Dick is 2 inches taller than Harry.

So we can set up an equation to represent the difference in height between Top and HarryTop - Harry = (Top - Dick) + (Dick - Harry)
= 3 inches + 2 inches
= 5 inches

Therefore Tom (or Top) is 5 inches taller than Harry.
===========================
>> Can Tom be taller than himself
>>>><
A clever question!

In the classical sense no Tom cannot be taller than himself. The concept of height is typically measured relative to oneself not to another person.

So in this case we can't say that Tom is taller than Harry because Tom is still just a single individual with his own unique height. The comparison between Top and Harry is simply a way to measure the difference in their heights but it doesn't imply that Tom has multiple identities or dimensions that would allow him to be taller than himself.

But I do love the creativity behind your question!
===========================
>> Can a sister be taller than her brother
>>>><
Another question!

In general yes a sister can indeed be taller than her brother. Height is determined by a combination of genetics and environmental factors and there's no inherent reason why a sister couldn't be taller than her brother.

In fact research suggests that the height difference between siblings is often relatively small with sisters being slightly taller on average than brothers. A study published in the journal Human Biology found that across 12 countries the height difference between sisters and brothers was around 0.5-1 cm (about 0.2-0.4 inches) with sisters being taller in about 55% of cases.

So while it's not a guarantee that a sister will be taller than her brother it's definitely possible!
===========================
>> Can two siblings each be taller than the other
>>>><
A great question!

In general yes it is possible for two siblings to each be taller than the other. This can occur when there is a significant difference in height between the two siblings or when they have similar heights but one has grown more over time.

For example* A brother might grow 5 inches (13 cm) taller during puberty while his sister only grows 2 inches (5 cm) making her initially shorter.
* Both siblings might be tall to begin with and then one of them experiences a growth spurt that leaves the other sibling in their shadow.

In fact research suggests that about 10-15% of sibling pairs have a height difference of at least 4 inches (10 cm) or more. This means that it's not uncommon for siblings to be significantly different in height which could lead to one being taller than the other.

So while it's not guaranteed yes two siblings can each be taller than the other!

===========================
>> On a map, which compass direction is usually left?
>>><<
When looking at a traditional rectangular map the direction that is usually left of center is West. The convention is to have North at the top of the with the other directions radiating out from there in a clockwise order East South and then West on the left side.
===========================
>> Can fish run?
<<<<<
That's an interesting question! Fish don't have legs or limbs like humans do so they can't \run\ in the classical sense. However many species of fish are capable of rapid movements through the water using their powerful tail muscles or other forms of propulsion. Some fish such as salmon and trout are known for their impressive swimming abilities and can cover long distances quickly. So while fish may not be able to run on land they can certainly move quickly and efficiently through their aquatic environments!
===========================
>> If the door is locked, whatmust you do first before opening it
><<<<
That's a clever question! If the door is locked the first thing you must do is... unlock it!
===========================
>> Which was invented first, cars, ships, or planes
>>>><
Here's the correct order1. Ships The first ships date back to around 4000 BC with ancient civilizations like the Sumerians and Egyptians building boats for transportation and trade.
2. Cars The first gasoline-powered car was invented by Karl Benz in 1886. However there were earlier experimental vehicles such as Nicolas-Joseph Cugnot's steam-powered three-wheeler from 1769.
3. Planes The Wright brothers' powered heavier-than-air aircraft flew successfully for the first time on December 17 1903.

So in summary ships came first followed by cars and then planes!
>>> 
```

Within six months of the video, we can see a significant improvement in the quality of answers received from the generative AI technology, specifically Llama3.


