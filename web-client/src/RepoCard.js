var React = require('react');
var StarsBox = require('./StarsBox.js');

var RepoCard = React.createClass({

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
            <div className="cardRepoFooterFirstLine">
              <h1 className="cardTitle">
                {data.title}
              </h1>
              <div className="cardStarsBox">
                {data.stars != null ? <StarsBox stars={data.stars} /> : null}
              </div>
            </div>
            <p className="cardText">
              {data.subtitle}
            </p>
            <img className="cardIcon" src={data.platform.icon} alt={data.platform.name} />
          </div>
        </a>
      </div>
    );
  }

});

module.exports = RepoCard;
