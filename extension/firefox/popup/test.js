function listenClicks(){
	document.addEventListener("click", (e) => {
		function getSelection(tabs){
			browser.tabs.sendMessage(tabs[0].id, "click");
		}

		function eventErr(e){
			console.error(e.message);
		}

		if (e.target.classList.contains("check")){
			console.log("clicked");
			browser.tabs.query({active: true, currentWindow: true})
				.then(getSelection);
		}
	});
}

function executeErr(e){
	console.error(e.message);
}

browser.tabs.executeScript({file: "/content_scripts/readselection.js"})
.then(listenClicks)
.catch(executeErr);
