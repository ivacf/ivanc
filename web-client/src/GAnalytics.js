exports.trackPageView = function() {

  // Injected with webpack depending on the environment
  // This will be set to null during development
  var trackingCode = GA_TRACKING_CODE;

  if (trackingCode == null) return;

  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', trackingCode, 'auto');
  ga('send', 'pageview');

};
