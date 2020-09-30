# ivanc - an amazing project

This repository contains two applications: 

1. A [React app](/web-client) that displays information about the author and his/her work as a software developer.
See deployed at http://ivanc.uk
2. A [Django server app](/server) that assists the React app by providing data via a REST API.
See deployed at https://api.ivanc.uk

## React app

Source code located under `/web-client`. This React app is set up with [Webpack](https://webpack.github.io/) and
[Express](http://expressjs.com/) so that the React components are rendered in the server side. 

#### Getting started
1. `npm install`: install app dependencies.
3. Make sure the companion API app is running at`http://localhost:8000/`  
4. `npm start`: start the dev server at `http://localhost:3000/`
5. Modify any of the components under [`/src`](web-client/src) and see the changes in real time thanks to
[React Hot loader](https://github.com/gaearon/react-hot-loader)

#### Deployment
This app can be deployed as a Node application on Heroku or Dokku.
There is a `heroku-postbuild` script in [`package.json`](web-client/package.json) so every time the app is pushed to Heroku,
Webpack compiles the JavaScript code in production mode. Webpack outputs the result into `public/bundle.js` that is loaded
from [`index.html`](web-client/index.html). This `index.html` file is then served with Express when the root endpoint is
requested. See [`server.js`](web-client/server.js) for more details. 

There are a couple of **environment variables** that need setting up before deploying:
* `API_BASE_URL`: The URL where the Django server app is deployed. e.g. https://api.ivanc.uk/
* `GA_TRACKING_CODE`: Your Google Analytics tracking code.


## Django server app

Source code located under `/server`. This Django API provides data such as a list of apps, articles and open source repositories through a REST API. It also provides an admin panel that allows adding, deleting and amending data with ease. It's implemented using [Django REST Framework](http://www.django-rest-framework.org/). 

#### Getting started
* Create a Python virtual environment under `/server`. You can follow [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
* Set up the Django settings environment variable: `export DJANGO_SETTINGS_MODULE=ivanc.dev_settings`. To avoid having to do this every time you can add this line to the `activate` script file located in your virtual environment `env/bin/activate`
* Activate the environment: `source env/bin/activate`
* Install dependencies: `pip install -r requirements-dev.txt`
* Now you're ready to run the dev server: `python manage.py runserver`

#### Testing
This Django project contains test for all endpoints. You can run them with `python manage.py test`. Some endpoints call external APIs. In order to avoid flaky tests, these external interactions are mocked using [VCR.py](https://github.com/kevin1024/vcrpy). Note the first time you run them they will perform real HTTP interactions. Consecutive executions will reuse the first response and the tests will no longer call the external API. 

#### Deployment
This app can be deployed as a Django application on Heroku or Dokku. The following **environment variables** are expected:

* `DJANGO_SETTINGS_MODULE`: This must point to the prod settings file `ivanc.prod_settings`
* `DJANGO_SECRET_KEY`: A random key used by Django. More info [here](https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-SECRET_KEY). 
* `DATABASE_URL`: Pointing to a PostgreSQL database. This variable is usually set up automatically by Heroku or Dokku after linking your app to a database.

An AWS bucket is required to store media files. You can follow [this tutorial](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/) to create an AWS bucket with the right permissions. Once that is done, you must point Django to your AWS bucket by adding these three env variables: 

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_STORAGE_BUCKET_NAME`

The `/repos` endpoint uses the GitHub API to pull data about repositories. The call doesn't require any authentication, however the GitHub API has very low [rate limits](https://developer.github.com/v3/rate_limit/) when performing non-authenticated calls. If you want to increase this limit to avoid problem you can [create a GitHub OAuth application](https://github.com/settings/applications/new) and use the generated values to set up two more variables:

* `GITHUB_CLIENT_ID`
* `GITHUB_CLIENT_SECRET`

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
