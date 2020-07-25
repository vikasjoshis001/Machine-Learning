import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-regression',
  templateUrl: './regression.component.html',
  styleUrls: ['./regression.component.css']
})
export class RegressionComponent {
  rank;
  url = "http://127.0.0.1:8000/rank/";
  show = false;

  constructor(private http: HttpClient) { }

  onSubmit(data) {
    return this.http.post(this.url,data.value).subscribe((result)=>{
      this.rank = result
      console.log(this.rank)
      this.show=true;
    })
  }

  onClose(){
    this.show=false;
  }
}
