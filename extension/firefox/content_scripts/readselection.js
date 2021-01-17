(function(){
	if (window.alreadyRun) {
		return;
	}
	window.alreadyRun = true;
	browser.runtime.onMessage.addListener((message) => {
		console.log("message received");
		if (message === "click") {
			selection = window.getSelection().toString();
			browser.runtime.sendMessage(selection);
		}
	});
})();
