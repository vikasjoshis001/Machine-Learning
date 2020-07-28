import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
@Component({
  selector: 'app-salary',
  templateUrl: './salary.component.html',
  styleUrls: ['./salary.component.css']
})
export class SalaryComponent implements OnInit {
  salary;
  url = "https://machine-learning-api.herokuapp.com/salary/";
  show = false; 

  constructor(private http:HttpClient) { }

  onSubmit(data){
    console.log(data.value)
    return this.http.post(this.url,data.value).subscribe((result)=>{
      this.salary = result
      this.show=true;
    })
  }

  onClose(){
    this.show=false;
  }

  ngOnInit(): void {
  }

}
