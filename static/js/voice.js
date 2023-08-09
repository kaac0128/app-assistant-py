var i = 0;
var mode = false;
var speak = false;
var dataMessage = "";

$(document).ready(function () {
    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.lang = "es-ES";
        recognition.continuous = true;
        recognition.interimResults = true;

        document.getElementById('canvasOne').addEventListener('click', function () {
            console.log("escuchando...");
            recognition.start();
        });

        recognition.onresult = function(event) {
            const result = event.results[event.results.length - 1];
            const text = result[0].transcript;
            sendYouChat(text);
          };

        recognition.onend = function() {
            console.log("termino")
        }
    }
    else {
        console.log('API de reconocimiento de voz no soportada');
    }
});

async function speakMessageIA(message){
    if ('speechSynthesis' in window) {
        const synth = window.speechSynthesis;
        let messageResponse = new SpeechSynthesisUtterance();
        messageResponse.text = message;
        messageResponse.lang = 'es-ES';
        messageResponse.rate = 1; 
        messageResponse.voice = speechSynthesis.getVoices().filter(x => x.lang.includes("es"))[0]; // se usará la primera voz disponible
        synth.speak(messageResponse);

    } else {
        console.log('SpeechSynthesis no es compatible con este navegador.');
    }
}
