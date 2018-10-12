import { NgModule } from '@angular/core';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CommonModule } from '@angular/common';
import { NgSpinKitModule } from 'ng-spin-kit';
import { RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ClientComponent } from './client/client.component';
import { CoachComponent } from './coach/coach.component';
import { EmployerComponent } from './employer/employer.component';
import { PendingResumeComponent } from './pending-resume/pending-resume.component';
import { ResumeComponent } from './resume/resume.component';

const PAGES = [
  SignupComponent,
  HomeComponent,
  LoginComponent,
  ClientComponent,
  CoachComponent,
  EmployerComponent
];

const COMPONENTS = [];

@NgModule({
  declarations: [
    ...PAGES,
    PendingResumeComponent,
    ResumeComponent,
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
