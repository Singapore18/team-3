import { NgModule } from '@angular/core';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CommonModule } from '@angular/common';
import { NgSpinKitModule } from 'ng-spin-kit';

const PAGES = [
  SignupComponent,
  HomeComponent
];

const COMPONENTS = [];

@NgModule({
  declarations: [
    ...PAGES
  ],
  imports: [
    CommonModule,
    NgbModule,
    NgSpinKitModule
  ],
  exports: [
    ...PAGES
  ]
})
export class PagesModule { }
