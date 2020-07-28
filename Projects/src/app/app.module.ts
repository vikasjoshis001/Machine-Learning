import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from "@angular/forms";
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegressionComponent } from './regression/regression.component';
import { ClassificationComponent } from './classification/classification.component';
import { ClusteringComponent } from './clustering/clustering.component';
import { SalaryComponent } from './salary/salary.component';
import { HomePageComponent } from './home-page/home-page.component';
import { AboutPageComponent } from './about-page/about-page.component';

@NgModule({
  declarations: [
    AppComponent,
    RegressionComponent,
    ClassificationComponent,
    ClusteringComponent,
    SalaryComponent,
    HomePageComponent,
    AboutPageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
