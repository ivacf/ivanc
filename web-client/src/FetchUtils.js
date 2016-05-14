exports.baseUrl = API_BASE_URL; // var injected with webpack

exports.buildServerURL = function(endpoint) {
  return API_BASE_URL + endpoint;
}

exports.parseJSON = function(response) {
  return response.json();
}

exports.checkStatus = function(response) {
  if (response.status >= 200 && response.status < 300) {
    return response
  } else {
    var error = new Error(response.statusText)
    error.response = response
    throw error
  }
}
