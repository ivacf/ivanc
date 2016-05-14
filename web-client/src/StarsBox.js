var React = require('react');

var StarsBox = React.createClass({

  render: function() {
    return (
      <div className="starsBox">
        <img src="images/star.svg" alt="star" />
        <p>
          {this.props.stars}
        </p>
      </div>
    )
  }

});

module.exports = StarsBox;
