import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RegressionComponent } from './regression/regression.component';
import { ClassificationComponent } from './classification/classification.component';
import { ClusteringComponent } from './clustering/clustering.component';
import { SalaryComponent } from './salary/salary.component';
import { HomePageComponent } from './home-page/home-page.component';
import { AboutPageComponent } from './about-page/about-page.component';


const routes: Routes = [
  {
  path : "regression",
  component : RegressionComponent
  },
  {
  path : "classification",
  component : ClassificationComponent
  },
  {
  path : "clustering",
  component : ClusteringComponent
  },
  {
  path : "salary",
  component : SalaryComponent
  },
  {
  path : "home",
  component : HomePageComponent
  },
  {
  path : "about",
  component : AboutPageComponent
  },
  {
  path : "",
  component : HomePageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
