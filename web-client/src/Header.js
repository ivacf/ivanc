var React = require('react');
var SocialBar = require('./SocialBar.js');

var Header = React.createClass({

  //TODO this should probably come from the API as well
  getProfile: function() {
    return {
      name: 'Iván Carballo',
      avatar: 'http://ivanc.uk/images/ivan-circle.png',
      summary: 'I’m a software engineer passionate about creating meaningful products by writing elegant code. I currently work at Monzo building a new type of bank. You can check out some of my work below.',
      social: [
        {id: 1, name: 'GitHub', url: 'https://github.com/ivacf', icon:'images/github.svg'},
        {id: 4, name: 'Medium', url: 'https://medium.com/@ivanc', icon:'images/medium.svg'},
        {id: 2, name: 'Twitter', url: 'https://twitter.com/ivacf', icon:'images/twitter.svg'},
        {id: 3, name: 'LinkedIn', url: 'https://uk.linkedin.com/in/ivacf', icon:'images/linkedin.svg'}
      ]
    };
  },

  render: function() {
    var profile = this.getProfile();
    return (
      <div className="header">
        <img src={profile.avatar} alt="Ivan's avatar" className="avatar"/>
        <h1>
          {profile.name}
        </h1>
        <p className="summary">
          {profile.summary}
        </p>
        <div className="socialBarContainer">
          <SocialBar data={profile.social} />
        </div>
      </div>
    );
  }

});

module.exports=Header
