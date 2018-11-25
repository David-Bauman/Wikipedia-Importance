# Wikipedia-Importance
  Using Beautiful Soup 4, this program combs through Wikipedia from a predefined start page, collecting the links to other pages, and creates a file which contains the amount of times each Wikipedia page is referenced by other pages. The program is "pausable" in that it can be shut down and restarted from the same spot it left off at (with a few second delay on exiting). 

  The program crunches on average between 3.5 and 4.5 pages per second, depending on system usage and other factors. It takes a little over 13 days of continuous running to finish. Speed is the largest problem.

  "makeimportanceusable.py" can be used to get a sense of what the influential stats are at the moment. This will change often for the first 100,000 or so pages. Afterwards, a clear top group emerges.
