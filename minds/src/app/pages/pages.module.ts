import { NgModule } from '@angular/core';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CommonModule } from '@angular/common';
import { NgSpinKitModule } from 'ng-spin-kit';
import { RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';

const PAGES = [
  SignupComponent,
  HomeComponent
];

const COMPONENTS = [];

@NgModule({
  declarations: [
    ...PAGES,
    LoginComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    NgbModule,
    NgSpinKitModule
  ],
  exports: [
    ...PAGES
  ]
})
export class PagesModule { }
