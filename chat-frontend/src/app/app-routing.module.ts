import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [{ path: '', loadChildren: () => import('./chat/chat.module').then(m => m.ChatModule) },
{ path: 'login', loadChildren: () => import('./login/login.module').then(m => m.LoginModule) },
{ path: 'sign_in', loadChildren: () => import('./sign-in/sign-in.module').then(m => m.SignInModule) }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
