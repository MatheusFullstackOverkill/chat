import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {

  user_message = '';

  messages = [];

  chatSocket = new WebSocket('ws://localhost:8000/ws/chat/01/');

  channelName = '';

  roomId = '';

  constructor() { }

  ngOnInit() {

    this.chatSocket.onopen = (e) => {
      console.log(e)
    }

    this.chatSocket.onmessage = (e) => {
        var data = JSON.parse(e.data);
        var message_data = JSON.parse(data['data']);
        if(this.channelName == '') {
            this.channelName = message_data.channel_name;
            this.roomId = message_data.room_id;
            this.messages = message_data.messages;
        } else {
          this.messages.push(message_data);
        };
        console.log(message_data);
        // console.log(this.channelName, this.roomId, this.messages);
    };

    this.chatSocket.onclose = (e) => {
        console.error('Chat socket closed unexpectedly');
    };
  }

  onSend() {
    this.chatSocket.send(JSON.stringify({
      'data': {
        'channel_name': this.channelName,
        'message': this.user_message,
        'room_id': this.roomId,
        'from_user_id': parseInt(localStorage.getItem('userId'))
      }
    }));
    this.user_message = '';
  }

}
