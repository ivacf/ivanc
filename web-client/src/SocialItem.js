var React = require('react');

var SocialItem = React.createClass({

  render: function() {
    return (
      <span className="socialItem">
        <a href={this.props.url} title={this.props.name} target="_blank">
          <img src={this.props.icon} alt={this.props.name}/>
        </a>
      </span>
    );
  }

});

module.exports = SocialItem;
