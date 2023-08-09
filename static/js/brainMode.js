
function sendYouChat(data) {

    fetch(location.href + 'api/chatBrain', {
        method: "POST",
        body: JSON.stringify({ question: data }),
        headers: { "Content-type": "application/json; charset=UTF-8" }
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            speakMessageIA(data.message)
        });


}