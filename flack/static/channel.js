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
        div.classList.add('message-user-connected');
        div.innerHTML = data.message;
        console.log(data.message);
        messageBox.append(div);
    });
        

    socket.on('recieve message', data => {
        console.log("Message has come " + data.content);
        const msg = createMessage(data);
        messageBox.append(msg);
    });
    
});
   

function createMessage(data) {
    const div = document.createElement('div');
    const senderDiv = document.createElement('div');
    const contentDiv = document.createElement('div');
    const dateDiv = document.createElement('div');
    
    senderDiv.innerHTML = data.sender;
    contentDiv.innerHTML = data.content;
    dateDiv.innerHTML = data.date;

    senderDiv.classList.add('message-sender-name');
    contentDiv.classList.add('message-content');
    dateDiv.classList.add('message-date');

    div.classList.add('message-div');
    div.classList.add('rounded');
    if(data.sender === user){
        div.classList.add('float-right');
    } else {
        div.classList.add('float-left');
    }
    div.appendChild(senderDiv);
    div.appendChild(contentDiv);
    div.appendChild(dateDiv);

    return div;
}