import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-classification',
  templateUrl: './classification.component.html',
  styleUrls: ['./classification.component.css']
})
export class ClassificationComponent {

  url="https://machine-learning-api.herokuapp.com/car/";
  evaluate;
  show = false;

  constructor(private http:HttpClient) { }

  onSubmit(data){
    console.warn(data.value)
    this.http.post(this.url,data.value).subscribe((result)=>{
      this.evaluate = result
      console.warn(this.evaluate)
      if (this.evaluate == 0){
        this.evaluate = "Acceptable"
      }
      if (this.evaluate == 1){
        this.evaluate = "Good"
      }
      if (this.evaluate == 2){
        this.evaluate = "Unacceptable"
      }
      if (this.evaluate == 3){
        this.evaluate = "Very Good"
      }
      this.show=true;
    })
  }

  onClose(){
    this.show = false;
  }



}
