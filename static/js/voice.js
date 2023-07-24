
var i = 0;
var mode = false;
var speak = false;
var dataMessage = "";

$(document).ready(function () {
    // Verificamos si el navegador soporta la API de reconocimiento de voz
    if ('webkitSpeechRecognition' in window) {
        // Creamos un nuevo objeto para el reconocimiento de voz
        var recognition = new webkitSpeechRecognition();

        // Configuramos el idioma
        recognition.lang = 'es-ES';

        // Configuramos la duración máxima de la grabación
        recognition.maxDuration = 10;

        // Iniciamos el reconocimiento al clic en un botón
        document.getElementById('icon-microphone').addEventListener('click', function () {
            recognition.start();
        });

        // Evento que se dispara cuando el reconocimiento de voz termina
        recognition.onresult = function (event) {
            // Obemos el resultado como texto y lo mostramos en la consola
            document.getElementById('search').value = event.results[0][0].transcript;
        };

        recognition.onend = function() {
            // Agrega aquí el código que quieres ejecutar cuando deje de escuchar
            initSpeak();
          }

    }
    else {
        console.log('API de reconocimiento de voz no soportada');
    }
});

async function IAWritingMessage() {
    if (i < dataMessage.length) {
        document.getElementById('response-ia').value += dataMessage.charAt(i);
        i++;
        setTimeout(IAWritingMessage, 80);
    }
}

async function speakMessageIA(message){
    dataMessage = message;
    IAWritingMessage();
    if ('speechSynthesis' in window) {

        // Crear mensaje de voz
        let messageResponse = new SpeechSynthesisUtterance();

        // Establecer texto del mensaje
        messageResponse.text = message;

        // Establecer idioma del mensaje
        messageResponse.lang = 'es-ES';

        // Establecer velocidad del mensaje
        messageResponse.rate = 1; // 1 = velocidad normal

        // Establecer voz del mensaje
        messageResponse.voice = speechSynthesis.getVoices().filter(x => x.lang.includes("es"))[0]; // se usará la primera voz disponible

        // Reproducir mensaje de voz
        window.speechSynthesis.speak(messageResponse);

    } else {
        console.log('SpeechSynthesis no es compatible con este navegador.');
    }
}

function initSpeak(){
    if(speak == false){
        speak = true;
        var elemento = document.getElementById("icon-microphone");
        elemento.classList.remove('animate__bounceIn');
        elemento.classList.add('animate__bounceOut');
        setTimeout(() => {
            elemento.style.display = 'none';
            elemento = document.getElementById("loading");
            elemento.classList.remove('animate__bounceOut');
            elemento.classList.add('animate__bounceIn');
            elemento.style.display = 'flex'
          }, 700);
    }else{
        speak = false;
        var elemento = document.getElementById("loading");
        elemento.classList.remove('animate__bounceIn');
        elemento.classList.add('animate__bounceOut');
        setTimeout(() => {
            elemento.style.display = 'none';
            elemento = document.getElementById("icon-microphone");
            elemento.classList.remove('animate__bounceOut');
            elemento.classList.add('animate__bounceIn');
            elemento.style.display = 'inline-block'
        }, 700);
        
    }
}
