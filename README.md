# ivanc

This repository contains two applications: 

1. A [React app](/web-client) that displays information about the author and his/her work as a software developer.
See deployed at http://ivanc.uk
2. A [Django server app](/server) that assists the React app by providing data via a REST API.
See deployed at https://api.ivanc.uk

## React app

Source code located under `/web-client`. This React app is set up with [Webpack](https://webpack.github.io/) and
[Express](http://expressjs.com/) so that the React components are rendered in the server side. 

### Get started
1. `npm install`: install app dependencies.
2. `npm start`: start the dev server at http://localhost:3000/
3. Modify any of the components under [`/src`](web-client/src) and see the changes in real time thanks to
[React Hot loader](https://github.com/gaearon/react-hot-loader)

### Deployment
This app should be deployed as a Node application on Heroku or Dokku.
There is a `heroku-postbuild` script in [`package.json`](web-client/package.json) so every time the app is pushed to Heroku,
Webpack compiles the JavaScript code in production mode. Webpack outputs the result into `public/bundle.js` that is loaded
from [`index.html`](web-client/index.html). This `index.html` file is then served with Express when the root endpoint is
requested. See [`server.js`](web-client/server.js) for more details. 

There are a couple of **environment variables** that need setting up before deploying:
* `API_BASE_URL`: The URL where the Django server app is deployed. e.g. https://api.ivanc.uk/
* `GA_TRACKING_CODE`: Your Google Analytics tracking code.


## Django server app

Coming soon..

## License

```
  Copyright 2016 Ivan Carballo.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
```
