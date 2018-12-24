# Wikipedia Importance Analyzer

[![GitHub Issues](https://img.shields.io/github/issues/David-Bauman/Wikipedia-Importance.svg)](https://github.com/David-Bauman/Wikipedia-Importance/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-green.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## What is it?

The analyzer combs through Wikipedia from a given start page. On a page it collects links to other Wikipedia pages, logs some data, and then visits each link it found to repeat the process.

### Importance

Currently the analyzer determines how important each page is by finding how many other Wikipedia pages link to it. The information is stored in a plain text file. make_importance_usable.py translates that file into some human readable information.

### Pausable

Visiting each and every of the ~5.5 million English Wikipedia articles is not a fast task: the analyzer crunches ~4 pages per second meaning that a complete run through Wikipedia could take 13 days of continuous running. To help alleviate issues that arise from this, the analyzer is "pausable": a keyboard interrupt (`^C` while the program is running) will save the current data and quit. When the analyzer is next run, the data will be loaded in and immediately pick up where it left off. (Note: speed issues can be mitigated by moving to a [lower level language and using threading](https://github.com/David-Bauman/Multi-Threaded-Wikipiedia-Importance).) 


## How do I use it?

1. Clone the repo to your local machine.
2. Ensure that packages "bs4" and "lxml" are installed.

#### creating_importance


1. Run `$ python3 creating_importance.py`
2. (Optional) "Pause" the program by exiting (`^C`). 

This function creates files called `importance` and `url_list` whenever it quits, either by being paused or when it finishes the entirety of Wikipedia. If paused, restarting the program (same command as step 1) will pick back up right where it left off.

#### make_importance_usable

0. The `importance` file, created by running [creating_importance](#creating_importance), must be in the directory.
1. Run `$ python3 make_importance_usable.py`

Use this function to get a sense of what the influential stats are at the moment. This will change often for the first 100,000 or so   pages. Afterwards, a clear top group emerges.

## Contributing

If you like the project, I'd love to have your help improving it. Contributions don't have to just be code though. It could also take the form of

- Opening issues on bugs you find or new features you'd like to see
- Joining discussion on issues and pull requests
- Discussing cool extensions of the data the current program gathers or interesting new ways to analyze it

#### Workflow

0. (Optional) Open an issue and describe what you will be trying to fix: a specific bug or a new feature.
1. Clone the repo to your local machine.
2. Create a new branch for your feature, commit changes to it, and push it to origin.
3. Open a pull request with a clear description of the changes.

## To Do

- Package manager for easier installation (pipenv? setup.py?)
- Switch to Wikipedia API if doing so boosts per page speed

