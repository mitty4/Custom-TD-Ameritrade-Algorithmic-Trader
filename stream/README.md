## Welcome to an exciting project

The idea was to identify if an equity would rise 0.5% more times than decreasing 0.25% so that I could make a day trade bot to essentially make guaranteed money.

Well, the analysis showed really fast and very large ROI's, however, in practice, the algo only lost money. It lost money because the analysis didn't account for the lag in sell time. For example, when I put in a sell order, the execution of that order may not happen immediately or for the exact price intended. 

So, the majority of my trades ended up selling for more than intended, which resulted in mainly losses. 

I did get lots of great practice with python, api's, pandas, numpy, sqlite and day trading knowledge so I am still overall very happy with this project and encourage anyone interested to give it a go!


The source code for the base of my project is available below. The library allowed for a fairly painless way to connect to the API, however, customization was difficult for what I wanted to do so I ended up referenecing TD Ameritrade's actual API documentation found <a href="https://developer.tdameritrade.com/apis">here</a>


Happy money hunting! 



## Source Code:


# tdameritrade-streaming

streaming order book data from TD Ameritrade API

## Video tutorial

https://youtube.com/parttimelarry

## Uses the tda-api Python Package

https://tda-api.readthedocs.io/

### Upgrading tda-api

If you already had tda-api installed, make sure you upgrade to the latest version!

```
pip3 install --upgrade tda-api
```
