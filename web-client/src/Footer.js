var React = require('react');
var FetchUtils = require('./FetchUtils');

var Footer = React.createClass({

  render: function() {
      return (
        <div className="footer">
          <p>
            Built with <a target="_blank" href="https://facebook.github.io/react/">React</a> and <a target="_blank" href="http://www.django-rest-framework.org/">Django REST framework</a>.
          </p>
          <p>
            Check out the REST API <a target="_blank" href={FetchUtils.baseUrl}>here</a>.
          </p>
          <p className="footerCopyRight">© 2016 Ivan Carballo </p>
        </div>
      );
  }

});

module.exports=Footer
