console.log("content script being executed")

var rid = null
var data = document.documentElement.innerHTML;
var xhr = new XMLHttpRequest();

xhr.open("POST", "http://localhost:8080", true);
xhr.setRequestHeader("Content-type", "text/plain");
xhr.onreadystatechange = function() {
  if (this.readyState == 4) {
    if (this.status == 200) {
      console.log(rid)
      rid = this.response;
      rid = rid.replace(/['"]+/g, '')
      setTimeout(() => {
        var xhr2 = new XMLHttpRequest();
        xhr2.open("GET", "http://localhost:8080/status?uid=" + rid, true);
        xhr2.onreadystatechange = function() {
          var response = ""
          if (this.readyState === 4) {
            if (this.status == 200) {
              chrome.runtime.sendMessage(this.response)
            } else {
              chrome.runtime.sendMessage("Status Error")
            }
          }
        }
        xhr2.send();
      }, 3000);
    } else {
      chrome.runtime.sendMessage("Creation Error")
    }
  }
}

xhr.send(data);
