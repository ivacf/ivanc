var React = require('react');
var AppList = require('./AppList.js');
var RepoList = require('./RepoList.js');
var ArticleList = require('./ArticleList.js');

var Content = React.createClass({

  render: function() {
    return (
      <div className="content">
        <div className="sectionContainer">
          <h1 className="contentTitle">Some projects I've worked on</h1>
          <AppList />
        </div>
        <div className="sectionContainer">
          <h1 className="contentTitle">My articles</h1>
          <ArticleList />
        </div>
        <div className="sectionContainer">
          <h1 className="contentTitle">Open source work</h1>
          <RepoList />
        </div>
      </div>
    );
  }

});

module.exports = Content;
