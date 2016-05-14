var React = require('react');

var ArticleCard = React.createClass({

  render: function() {
    var data = this.props.data;
    var footerColorStyle = {
      background: data.color
    };
    return (
      <div className="card">
        <a target="_blank" href={data.url} title={data.title}>
          <img className="cardImage" src={data.image} />
          <div className="cardFooter" style={footerColorStyle}>
            <h1 className="cardTitle articleTitle">
              {data.title}
            </h1>
            <img className="cardIcon" src={data.platform.icon} alt={data.platform.name} />
          </div>
        </a>
      </div>
    );
  }

});

module.exports = ArticleCard;
