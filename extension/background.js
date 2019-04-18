'use strict';

console.log("sanity check in background.js")

var result = "placeholder"
chrome.runtime.onMessage.addListener(
  function(message, sender, sendResponse) {
    if (message === "Match") {
      chrome.tabs.executeScript({file: 'contentScript.js'})
    } else if (message === "GetResponse"){
      sendResponse(result); 
    } else if (message === "ResetResponse") {
      result = "placeholder"
    } else if (message === "Error" ) {
      result = "server error" 
    } else {
      result = message
    }
  }
);

