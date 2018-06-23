# NewsCrawl V. 0.4
NewsCrawl is a python command-line program that utilizes HTML parsing to pull poplular post titles from the subreddit of your choice, though it was designed for news subs in particular. 

# Requirements
Newscrawl relies on a handful of common python libraries, all of which can be downloaded using pip:
  BeautifulSoup 4
  screeninfo
  urllib.request

# Use
NewsCrawl can be called from a command line. It's argument scructure is "python.exe newscrawl.py \[subreddit]",  Though the exact command to must call it is dependent on your operating system and the name of the file on your PC. The subreddit argument is optional, and only if you wish to direct the HTML request to a different subreddit than the default, which is https://www.reddit.com/r/worldnews.

The speed of the text scroll and the length each headline is displayed can be easily configured at the top of the py file, using the "delay" and "txtscrl" variables.

# Known Issues
- Occasionally, reddit's servers will reject your request with a 429 Error, even if you've only sent one request. I'm not entirely sure if this is an issue with the way urllib requests web pages, or if Reddit is detecting an automated system and autorejecting it when the servers are under a heavy load. It will try to fix this soon, but it will require some more extensive research into it.
- The display method sometimes separates a word halfway through when adding a line break, making some headlines difficult to read at a quick glance. I will develop a check system in the future that will check how long the next word is and decide to include a line break early or not.
