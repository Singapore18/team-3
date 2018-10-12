import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  registerClient(name, age, location, interests) {
    this.http.post('http://127.0.0.1:8000/chatbotResult', {
      userData: {
        name,
        age,
        location,
        interests
      }
    }).toPromise();
  }

}
