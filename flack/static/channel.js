document.addEventListener('DOMContentLoaded', function(event){
    const textField = document.querySelector("#textArea");
    const sendButton = document.querySelector('#sendButton');
    const messageBox = document.querySelector("#messageBox");
    console.log(location.protocol + '//' + document.domain + ':' + location.port);
    const socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        console.log('socket connected');
        socket.emit('user connect', {'user': user});
        console.log(user + user);
        sendButton.onclick = () => {
                const content = textField.value;
                // console.log("Message is going to be sent " + content);
                textField.value = '';
                socket.emit('send message', {'content': content, 'sender': user});
            };
        });

    socket.on('user connect', data => {
        const div = document.createElement('div');
        div.classList.add('text-center');
        div.classList.add('float-left');
        div.innerHTML = data.message;
        console.log(data.message);
        messageBox.append(div);
    });
        

    socket.on('recieve message', data => {
        console.log("Message has come " + data.content);
        const div = document.createElement('div');
        div.innerHTML = data.content;
        div.classList.add('message-div');
        
        if(data.sender === user){
            div.classList.add('float-right');
        } else {
            div.classList.add('float-left');
        }
        messageBox.append(div);
    });
    
});
    
