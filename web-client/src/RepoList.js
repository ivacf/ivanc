var React = require('react');
var RepoCard = require('./RepoCard.js');
var FetchUtils = require('./FetchUtils');

var RepoList = React.createClass({

  loadReposFromServer: function() {
    function parseStringDates(repos) {
      repos.forEach(function(repo) {
        repo.start_date = new Date(repo.start_date);
        if (repo.end_date) {
          repo.end_date = new Date(repo.end_date);
        }
      });
      return repos;
    }

    fetch(FetchUtils.buildServerURL('repos/'))
      .then(FetchUtils.checkStatus)
      .then(FetchUtils.parseJSON)
      .then(parseStringDates)
      .then(function(reposJson) {
        this.setState({repos: reposJson});
      }.bind(this))
      .catch(function(error) {
        console.log('Error retrieving repos', error);
      });
  },

  getInitialState: function() {
    return {repos: []};
  },

  componentDidMount: function() {
    this.loadReposFromServer();
  },

  render: function() {
    var repoNodes = this.state.repos.map(function(repo) {
      return (
        <div className="cardContainer" key={repo.id} >
          <RepoCard data={repo} />
        </div>
      );
    });

    return (
      <div className="repoList">
        {repoNodes}
      </div>
    );
  }

});

module.exports=RepoList
