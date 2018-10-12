import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SignupComponent } from './pages/signup/signup.component';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { ClientComponent } from './pages/client/client.component';
import { CoachComponent } from './pages/coach/coach.component';
import { EmployerComponent } from './pages/employer/employer.component';
import { JobsComponent } from './pages/jobs/jobs.component';
import { EmployerJobComponent } from './pages/employer-job/employer-job.component';

const routes: Routes = [
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: 'signup',
    component: SignupComponent
  },
  {
    path: 'pwid',
    component: ClientComponent
  },
  {
    path: 'coach',
    component: CoachComponent
  },
  {
    path: 'employer',
    redirectTo: 'employer-jobs'
  },
  {
    path: 'employer-jobs',
    component: EmployerJobComponent
  },
  {
    path: 'employer-resume',
    component: EmployerComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: '**',
    redirectTo: 'home',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
