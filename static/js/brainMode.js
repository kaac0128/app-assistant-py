var brainModeOpcion = false;
var elem = document.getElementById('brain-mode');

function brainMode(){
    if(brainModeOpcion){
        elem.classList.remove('active-brain-mode'); 
        brainModeOpcion = false;
    }else{
        elem.classList.add('active-brain-mode'); 
        brainModeOpcion = true;
    }
}

function sendYouChat(){
    fetch(location.href + 'api/chatBrain', {
        method: "POST",
        body: JSON.stringify({question: document.getElementById('website-admin').value}),
        headers: { "Content-type": "application/json; charset=UTF-8" }
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}

