var SaveMessageInNotion = {};

function chatBrainRequest() {
    fetch(location.href + 'api/chatBrain', {
        method: "POST",
        body: JSON.stringify({question: document.getElementById('search').value}),
        headers: { "Content-type": "application/json; charset=UTF-8" }
    })
        .then(response => response.json())
        .then(data => {
            speakMessageIA(data.content);
            SaveMessageInNotion = data;
        });
}
