import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth/auth.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {

  constructor(private auth:AuthService) { }

  ngOnInit() {
    this.auth.onSignIn({
      username: 'matheus',
      email: 'jordy@gmail.com',
      password: '123456'
    }).subscribe(res => {
      console.log(res)
    })
  }

}
