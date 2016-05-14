var React = require('react');
var Header = require('./Header.js');
var Content = require('./Content.js');
var Footer = require('./Footer.js');

var WebApp = React.createClass({

  render: function() {
    return (
      <div className="webApp">
        <Header />
        <Content />
        <Footer />
      </div>
    );
  }

});

module.exports=WebApp
