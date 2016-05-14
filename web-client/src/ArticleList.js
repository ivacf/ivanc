var React = require('react');
var ArticleCard = require('./ArticleCard.js');
var FetchUtils = require('./FetchUtils');

var ArticleList = React.createClass({

  loadArticlesFromServer: function() {

    function parseStringDates(articles) {
      articles.forEach(function(article) {
        article.publish_date = new Date(article.publish_date);
      });
      return articles;
    }

    fetch(FetchUtils.buildServerURL('articles/'))
      .then(FetchUtils.checkStatus)
      .then(FetchUtils.parseJSON)
      .then(parseStringDates)
      .then(function(articlesJson) {
        this.setState({articles: articlesJson});
      }.bind(this))
      .catch(function(error) {
        console.log('Error retrieving articles', error);
      });
  },

  getInitialState: function() {
    return {articles: []};
  },

  componentDidMount: function() {
    this.loadArticlesFromServer();
  },

  render: function() {
    var articleNodes = this.state.articles.map(function(article) {
      return (
        <div className="cardContainer" key={article.id} >
          <ArticleCard data={article} />
        </div>
      );
    });

    return (
      <div className="articleList">
        {articleNodes}
      </div>
    );
  }

});

module.exports=ArticleList
