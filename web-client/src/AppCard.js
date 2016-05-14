var React = require('react');

var AppCard = React.createClass({

  // Convert date to format -> Jun 2015
  dateToMonthYearString: function(date) {
    var monthNames = [
      "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ];
    var monthIndex = date.getMonth();
    var year = date.getFullYear();
    return monthNames[monthIndex] + ' ' + year;
  },

  // Return a period string like Jun 2012 - Oct 2013
  buildPeriodString: function() {
    var data = this.props.data;
    var startDateString = this.dateToMonthYearString(data.start_date);
    var endDateString = 'Present';
    if (data.end_date) {
      endDateString = this.dateToMonthYearString(data.end_date);
    }
    return startDateString + ' - ' + endDateString;
  },

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
            <h1 className="cardTitle">
              {data.title}
            </h1>
            <p className="cardText">
              {this.buildPeriodString()}
            </p>
            <img className="cardIcon" src={data.platform.icon} alt={data.platform.name} />
          </div>
        </a>
      </div>
    );
  }

});

module.exports = AppCard;
