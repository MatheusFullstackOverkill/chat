import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class AuthService {

  constructor(private httpRequest:HttpClient) { }

  onLogin(userData):Observable<any> {
    return this.httpRequest.post('http://localhost:8000/api-token-auth/', userData)
  }
  
  onSignIn(userData):Observable<any> {
    return this.httpRequest.post('http://localhost:8000/api/users/', userData)
  }

}
