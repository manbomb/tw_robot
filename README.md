# TW Robot

A Twitter robot with timed messages. Simple and efficient. 

## How to use

* Edit in the tw_robot.py the variables consumer_key, consumer_secret, access_token, access_token_secret with your own values of your application. If you want to see more: [Click Here !](http://docs.tweepy.org/en/latest/auth_tutorial.html)
* You will need two archives: 'list.txt' and 'hashtags.txt'. Create them if necessary.
* list.txt: this is the archive of messages and times. Write like this:

    09:08:30 - Message Here
    09:09:30 - Message Here 2
    09:10:30 - Message Here 3

### Recommendations about 'list.txt':
- Do not repeat messages. This can cause an error.
- Minimum interval between two messages: 15 secs.

### Tips about 'list.txt':
- The pointer can catch only one message per time. If there is two or more messages in same time, the pointer will catch one per day.

* hashtags.txt: this is the archive of hashtags. Each message has 4 hashtags, randomly chosed here. Write like this:

    covid19
    coronavirusbrasil
    brasil
    coronavirusmaringa
    maringa
    covid2019
    washhands

### Recommendations about 'hashtags.txt':
- separate hashtags with a line break.
- do not write the #, only the words.
    
* Run the tw_robot.py
* If you update something in the hashtags.txt or list.txt, prees the R key to refresh.
* If you want to quit, press the Q key to quit.

# Contact:

If you still have questions about this, tell me:
sergiolucasavilladasilva@gmail.com
