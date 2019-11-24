# TripBook

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://img.shields.io/badge/licence-Apache-blue)](https://img.shields.io/badge/licence-Apache-blue)
[![Build Status](https://img.shields.io/badge/TripBook-v1.0-blue)](https://img.shields.io/badge/TripBook-v1.0-blue)

# Description
TripBook is a facebook plugin that uses modern AI to recommend travel destinations and their alternatives for people on a budget. Whether you know where to look you have an image in mind or you want to write down some keywords, TripBook will know what you want with accurate similarities. 
Using Facebook's cryptocurrency "Libra" for all the transactions, TripBook aims to unify the payment methods of accommodations and facilities to make it easier safer and more secure. Introducing LibraBand, a Cashless payment bracelet connected to your Libra credit and can be blocked at any time for minimum risk. With Libra currency you don't have to carry your wallet in the streets of an unfamiliar city anymore, your phone or your LibraBand is all you need to pay.

#  Features

  - View our top destinations and suggestions based on calculated reviews from thousands of tourists. 
  - Select some keywords or upload a picture you want to locate or have a list of similar places.
  - Select your destination 
  - Pay with Libra currency and enjoy our Cashless bracelet Libraband



### Technologies

TripBook uses a number of open source projects to work properly:
* Python 3.7+
* [Node.js] 10.6+

### Installation

TripBook requires [Node.js](https://nodejs.org/) v10.6+ to run.
>BackEnd
Install the dependencies and devDependencies and start the server.

```sh
$ cd Server
$ pip install requirements.txt
```

>FrontEnd

```sh
$ cd tripbook
$ npm install 
```

### Workflow
1. User opens TripBook UI and views the top destinations
2. Picture Identification
    2.1 User uploads an image using our VueJs builtin UI 
    2.2 Image is preprocessed and ran through a DeepLearning CNN model
    2.3 Model identifies similar pictures in the database
    2.4 Our sentimentAnalysis algorithms calculate the top destinations based on recent reviews and comments 
    2.5 Server returns the top destinations found
3. Keyword search
    3.1 User writes picks a location
    3.2 Server identifies the selected location
    3.3 Our sentimentAnalysis algorithms calculate the top destinations based on recent reviews and comments 
    3.4 Server returns the top destinations found


### Todos
- Builtin NLP model that looks into the database to identify the places that match the description keyworkds input by users
- LibraBand and Libra Credit 
- Multi-payment 
   

License
----

Apache

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
