document.addEventListener('DOMContentLoaded', function(event){
    const textField = document.querySelector("#textArea");
    const sendButton = document.querySelector('#sendButton');
    const messageBox = document.querySelector("#messageBox");
    console.log(location.protocol + '//' + document.domain + ':' + location.port);
    const socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        console.log('socket connected');
        socket.emit('my event', {data: 'I\'m connected!'});

        sendButton.onclick = () => {
                const content = textField.value;
                console.log("Message is going to be sent " + content);
                socket.emit('send message', {'content': content});
            };
        });

    socket.on('recieve message', data => {
        console.log("Message has come " + data.content);
        const div = document.createElement('div');
        div.innerHTML = data.content;
        div.classList.add('message-div');
        div.classList.add('float-left')
        messageBox.append(div);
    });
    
});
    
