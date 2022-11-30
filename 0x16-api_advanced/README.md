# API advanced

Python scripts interpretted on [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) using [Python 3.4.3](https://www.python.org/downloads/release/python-343/) and must conform to [PEP 8 (v1.7.x)](https://pep8.readthedocs.io/en/release-1.7.x/intro.html) style.


### Focus
Learn how to perform queries with Reddit's [API](https://www.reddit.com/dev/api/) using the `Request` Python library.

### Example Usages

[0-subs.py](0-subs.py)
```
0x16-api_advanced:$ cat 0-main.py
#!/usr/bin/python3
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
0x16-api_advanced:$ python3 0-main.py programming
756024
0x16-api_advanced:$ python3 0-main.py this_is_a_fake_subreddit
0
```
[1-top_ten.py](1-top_ten.py)
```
0x16-api_advanced:$ cat 1-main.py
#!/usr/bin/python3
import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
0x16-api_advanced:$ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
0x16-api_advanced:$ python3 1-main.py this_is_a_fake_subreddit
None
0x16-api_advanced:$
```
[2-recurse.py](2-recurse.py)
```
0x16-api_advanced:$ cat 2-main.py
#!/usr/bin/python3
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
0x16-api_advanced:$ python3 2-main.py programming
932
0x16-api_advanced:$ python3 2-main.py this_is_a_fake_subreddit
None
```
[100-count.py](100-count.py)
```
0x16-api_advanced:$ cat 100-main.py 
#!/usr/bin/python3
import sys

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
0x16-api_advanced:$ python3 100-main.py programming 'python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
scala: 4
0x16-api_advanced:$ python3 100-main.py not_a_valid_subreddit 'python java javascript scala no_results_for_this_one'
0x16-api_advanced:$ python3 100-main.py not_a_valid_subreddit 'python java'
0x16-api_advanced:$ 
```
### Author
- [Alex Yu](https://github.com/AlexYu01)
### Acknowledgments
- [Holberton](https://www.holbertonschool.com/)
- [Reddit's API](https://www.reddit.com/dev/api/)
