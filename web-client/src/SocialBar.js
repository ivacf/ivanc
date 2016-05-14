var React = require('react');
var SocialItem = require('./SocialItem.js');

var SocialBar = React.createClass({

  render: function() {
    var socialNodes = this.props.data.map(function(platform) {
      return (
        <SocialItem
          url={platform.url}
          name={platform.name}
          icon={platform.icon}
          key={platform.id} />
      );
    });
    
    return (
      <div className="socialBar">
        {socialNodes}
      </div>
    );
  }

});

module.exports = SocialBar;
