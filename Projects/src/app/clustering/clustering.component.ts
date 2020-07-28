import { Component, OnInit } from '@angular/core';
import * as XLSX from 'xlsx';
import { HttpClient } from "@angular/common/http";

@Component({
  selector: 'app-clustering',
  templateUrl: './clustering.component.html',
  styleUrls: ['./clustering.component.css']
})
export class ClusteringComponent implements OnInit {

  name = 'This is XLSX TO JSON CONVERTER';
  willDownload = false;
  x = []
  y = []
  z = []
  Excel;
  count;
  profit;
  url = "http://127.0.0.1:8000/profit/";

  constructor(private http:HttpClient) { }

  onFileChange(ev) {
    let workBook = null;
    let jsonData = null;
    const reader = new FileReader();
    const file = ev.target.files[0];
    reader.onload = (event) => {
      const data = reader.result;
      workBook = XLSX.read(data, { type: 'binary' });
      jsonData = workBook.SheetNames.reduce((initial, name) => {
        const sheet = workBook.Sheets[name];
        initial[name] = XLSX.utils.sheet_to_json(sheet);
        this.Excel = initial[name]
        this.count = initial[name].length
        var i = 0
        while (i < initial[name].length){
        this.x.push(initial[name][i]['x'])
        this.y.push(initial[name][i]['y'])
        this.z.push({"x":initial[name][i]['x'],"y":initial[name][i]['y']})
        i++
        }
        console.log(this.x)
        console.log(this.y)
        console.log("data")
        console.log(this.z)
        this.http.post(this.url,this.z).subscribe((result)=>{
          this.profit = result})
          console.log(this.profit)
        }
    , {});
      const dataString = JSON.stringify(jsonData);
      document.getElementById('output').innerHTML = dataString.slice(0, 300).concat("   ");
      // this.setDownload(dataString);
    }
    reader.readAsBinaryString(file);

  }

  // setDownload(data) {
  //   this.willDownload = true;
  //   setTimeout(() => {
  //     const el = document.querySelector("#download");
  //     el.setAttribute("href", `data:text/json;charset=utf-8,${encodeURIComponent(data)}`);
  //     el.setAttribute("download", 'xlsxtojson.json');
  //   }, 1000)
  // }

  ngOnInit(): void {
  }

}
