function simulateAIMessage() {
    const chatContainer = document.querySelector('.chat');
    const message = document.createElement('div');
    message.classList.add('message');

    const aiImage = document.createElement('img');
    aiImage.src = 'static/img/bot.png';
    aiImage.alt = 'Foto de la IA';

    const textContainer = document.createElement('div');
    textContainer.classList.add('text');
    textContainer.textContent = 'Estoy procesando tu mensaje...';

    message.appendChild(aiImage);
    message.appendChild(textContainer);

    chatContainer.appendChild(message);

    // Simulamos un tiempo de respuesta
    setTimeout(function () {
        textContainer.textContent = 'Este es un mensaje de ejemplo de la IA.';
    }, 2000); // Cambia el tiempo según la respuesta de tu IA real.
}

// Evento al hacer clic en el botón de micrófono
const microphoneBtn = document.getElementById('microphone-btn');
microphoneBtn.addEventListener('click', function () {
    simulateAIMessage();
});

// Evento al presionar Enter en el input
const userInput = document.getElementById('user-input');
userInput.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        simulateAIMessage();
    }
});
