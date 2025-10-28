import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
providedIn: 'root',
})
export class AuthService {
private API_URL = 'http://127.0.0.1:8000/auth/login';

constructor(private http: HttpClient) {}

login(username: string, password: string): Observable<any> {
const formData = new FormData();
formData.append('username', username);
formData.append('password', password);

return this.http.post(`${this.API_URL}/login`, formData);


}
}