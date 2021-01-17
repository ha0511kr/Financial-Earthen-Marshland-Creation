browser.runtime.onMessage.addListener(sendSelection);

function sendSelection(message) {
	webSocket = new WebSocket("ws://localhost:8890");
	webSocket.onopen = function(event){
		webSocket.send(message);
	}
	webSocket.onmessage = function (event) {
		console.log(event.data);
	}
}
