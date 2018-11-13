Alexbench
=======
Alexbench is a web page loading time monitor.  
And this is exactly what it does.  
Like a sergeant it stands behind a web page of your interest with a stopwatch,  
measuring its loading time.  
Again. Again. And again.  
  
  
## Getting started   
**Before you try to run the app make sure:**  
* python interpreter (v.3.6 or higher) is installed on your computer;  
* all of the prerequisite python modules are installed and up-to-date:
    * pip `python -m pip install -U pip`;
    * [numpy](<http://www.numpy.org>) `python -m pip install numpy`;
    * [requests](<http://docs.python-requests.org/en/master/>) `python -m pip install requests`;
    * [matplotlib](<https://matplotlib.org/index.html>) `python -m pip install matplotlib`.  
    
Download ZIP or clone the project.  

## Run the app. Instructions.  
* Launch _run.py._ There is no GUI implemented so you will see a good old style black console window. 
* You will be sequentially asked to enter 3 parameters:  
    * a hostname - expected format is `google.com`,  
    you either may enter ip (which is not recommended but it will also work)  
    or you even could skip this step by hitting 'enter', a default hostname will be used);  
    * test duration in minutes - how long you do wish the app to monitor a web page,  
    expected integers `from 1 up to 1440`, skip with 'enter' and a default paramater will be used;  
    * measurement interval in seconds - how often you want the app to make a measurement,  
    expected integers `from 2 up to duration time*60`, skip to use a default parameter.  
     
* That's it. The app doesn't need something more to be entered, it works.  

Running monitor will be displayed on a new web page which will be popped.  
Although it shows up to 12 last measurements, all measurements are written to a .csv file.   
And it's possible to have a look at them after the app stops.  
All results (.csv, .svg, .html) will be kept in a folder titled _results_ in the app root directory locally.
