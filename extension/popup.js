chrome.extension.getBackgroundPage().console.log("sanity check in popup.js");
let submitButton = document.getElementById('submitButton');

submitButton.onclick = function(element) {
  chrome.runtime.sendMessage("Match", function(pass) {
    result = poll();
  });
};


async function poll() {
  while (true) {
    let promise = new Promise((resolve, reject) => {
      setTimeout(() => {
        chrome.runtime.sendMessage("GetResponse", function (response) {
          resolve(response);
        })
      }, 20)
    });
    let result = await promise; // wait till the promise resolves (*)
    if (result !== "placeholder") {
      chrome.runtime.sendMessage("ResetResponse")
      break
    }
  }
  chrome.extension.getBackgroundPage().console.log("polling done!"); // "done!"
  return result
}




/*
function getResponse() {
  chrome.extension.getBackgroundPage().console.log("in getResponse");
  return new Promise(function(resolve, reject) {
    chrome.extension.getBackgroundPage().console.log("In promise")
    setTimeout(function() {
      chrome.runtime.sendMessage("GetResponse", function (response) {
        chrome.extension.getBackgroundPage().console.log("in GetResponse callback");
        resolve(response);
      })
    }, 20);       
  });
}

async function poll() {
  chrome.extension.getBackgroundPage().console.log("in poll()")
  var response;
  var counter = 0
  while true {
    response = await getResponse()
    chrome.extension.getBackgroundPage().console.log("polling number" + counter)
    if (response !== "placeholder") {
      break
    }
  }  

  chrome.extension.getBackgroundPage().console.log("I've broken out of the loop")
  var responseDiv = document.getElementById('response');
  var textNode = document.createTextNode(response);
  responseDiv.appendChild(textNode);
  chrome.extension.getBackgroundPage().console.log("I got this response: " + response);
}

*/
