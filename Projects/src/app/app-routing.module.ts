import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RegressionComponent } from './regression/regression.component';
import { ClassificationComponent } from './classification/classification.component';


const routes: Routes = [
  {
  path : "regression",
  component : RegressionComponent
  },
  {
  path : "classification",
  component : ClassificationComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
