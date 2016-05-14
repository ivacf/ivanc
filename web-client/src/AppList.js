var React = require('react');
var AppCard = require('./AppCard.js');
var FetchUtils = require('./FetchUtils');

var AppList = React.createClass({

  loadAppsFromServer: function() {
    function parseStringDates(apps) {
      apps.forEach(function(app) {
        app.start_date = new Date(app.start_date);
        if (app.end_date) {
          app.end_date = new Date(app.end_date);
        }
      });
      return apps;
    }

    fetch(FetchUtils.buildServerURL('apps/'))
      .then(FetchUtils.checkStatus)
      .then(FetchUtils.parseJSON)
      .then(parseStringDates)
      .then(function(appsJson) {
        this.setState({apps: appsJson});
      }.bind(this))
      .catch(function(error) {
        console.log('Error retrieving apps', error);
        //TODO display error to user?
      });
  },

  getInitialState: function() {
    return {apps: []};
  },

  componentDidMount: function() {
    this.loadAppsFromServer();
  },

  render: function() {
    var appNodes = this.state.apps.map(function(app) {
      return (
        <div className="cardContainer" key={app.id} >
          <AppCard data={app} />
        </div>
      );
    });

    return (
      <div className="appList">
        {appNodes}
      </div>
    );
  }

});

module.exports=AppList
