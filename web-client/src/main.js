var React = require('react');
var ReactDOM = require('react-dom');
var WebApp = require('./WebApp.js');
var GAnalytics = require('./GAnalytics.js');
//Include styles using webpack
require("../styles/main.css");

ReactDOM.render(
  <WebApp />,
  document.getElementById('root')
);

GAnalytics.trackPageView();
