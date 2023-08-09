var SaveMessageInNotion = {};

function obtainInfoFormNotion(){
    SaveMessageInNotion = {
        title: document.getElementById('title-notion').value,
        content: document.getElementById('message-notion').value,
    }
    exportDataNotion();
}

function exportDataNotion(){
    fetch(location.href + '/api/createPageNotion', {
        method: "POST",
        body: JSON.stringify({data: SaveMessageInNotion}),
        headers: { "Content-type": "application/json; charset=UTF-8" }
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            SaveMessageInNotion = data;
        });
}