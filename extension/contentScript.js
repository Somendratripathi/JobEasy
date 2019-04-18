console.log("content script being executed")

var rid = null
var data = document.documentElement.innerHTML;
var xhr = new XMLHttpRequest();

xhr.open("POST", "http://localhost:8080", true);
xhr.setRequestHeader("Content-type", "text/plain");
xhr.onreadystatechange = function() {
  if (this.readyState == 4) {
    if (this.status == 200) {
      var response = this.response;
      rid = response;
      chrome.runtime.sendMessage(rid)
    } else {
      chrome.runtime.sendMessage("Error")
    }
  }
}

var getResourceStatus = function() {
  xhr2.open("GET", "http://localhost:8080/" + rid, true);
  xhr2.onreadystatechange = function() {
    var response = ""
    if (this.readyState === 4) {
      if (this.status == 200) {
        var response = this.response
        rid = response.rid
      } else {
        error = true  
      }
    }
  }
  xhr2.send()
}

xhr.send(data);
