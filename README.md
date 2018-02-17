# Wikipedia-Importance
Using Beautiful Soup 4, this program combs through Wikipedia from a predefined start page, collecting the links to other pages, and creates a file which contains the amount of times each Wikipedia page is referenced by other pages. The program is "pausable" in that it can be shut down and restarted from the same spot it left off at (with a few second delay on exiting). The current results can be viewed at https://bauman.zapto.org/~david/Wikipedia/, which will continue to be fed updated results.

The program crunches on average between 3 and 4 pages per second, depending on system usage and other factors. My computer did about 3.7 pages/sec for the majority of the time. It took a little over 17 days of continuous running to finish. Speed is the largest problem.

"makeimportanceusable.py" is the precursor to the website and can be used after "pausing" the program to get a sense of what the influential stats are at the moment. This will change often for the first 100,000 or so pages. Afterwards, a clear top group emerges.
