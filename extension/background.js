'use strict';

console.log("sanity check in background.js")

var result = "placeholder"
chrome.runtime.onMessage.addListener(
  function(message, sender, sendResponse) {
    console.log("receiving message" + message)
    if (message === "Match") {
      chrome.tabs.executeScript({file: 'contentScript.js'})
    } else if (message === "GetResponse"){
      sendResponse(result); 
    } else if (message === "ResetResponse") {
      result = "placeholder"
    } else if (message === "Status Error" ||  message === "Creation Error" ) {
      result = "server error" 
    } else if (message === "FAILED") {
      result = "client error (website not supported)"
    } else {
      result = message
    }
  }
);

