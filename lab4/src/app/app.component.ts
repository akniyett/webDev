import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'lab4';
  number: number = 20;
  message: string = "djfsdkf";
  numbers: number[] = [1,2,3];
  students: any[];
  isMsg: boolean;
  display: string;
  items: string[];
  constructor(){
    console.log("okey")
    this.number = 7;
    this.numbers = [2,3,4];
    this.students = [
      {
        id: '19BDsakjds',
        full_name: 'Name',
        gpa: 3.0
      },
      {
        id: '20BDsakjds',
        full_name: 'ame',
        gpa: 3.8
      },
      {
        id: '19BDsa99ds',
        full_name: 'mName',
        gpa: 3.2
      }
    ];
    this.isMsg = true;
    this.display='lol';
    this.items = []; 
  }
  btnClick(){
    this.isMsg = !this.isMsg;
  }
  addItem(){
    if(this.display != "") {
      this.items.push(this.display);
      this.display="";
    }
  }
  remove(i:number){
    this.items.splice(i, 1);
  }
   

}
