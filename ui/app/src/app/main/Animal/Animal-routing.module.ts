import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnimalHomeComponent } from './home/Animal-home.component';
import { AnimalNewComponent } from './new/Animal-new.component';
import { AnimalDetailComponent } from './detail/Animal-detail.component';

const routes: Routes = [
  {path: '', component: AnimalHomeComponent},
  { path: 'new', component: AnimalNewComponent },
  { path: ':id', component: AnimalDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Animal-detail-permissions'
      }
    }
  },{
    path: ':animal_id/Allergy', loadChildren: () => import('../Allergy/Allergy.module').then(m => m.AllergyModule),
    data: {
        oPermission: {
            permissionId: 'Allergy-detail-permissions'
        }
    }
},{
    path: ':animal_id/Appointment', loadChildren: () => import('../Appointment/Appointment.module').then(m => m.AppointmentModule),
    data: {
        oPermission: {
            permissionId: 'Appointment-detail-permissions'
        }
    }
}
];

export const ANIMAL_MODULE_DECLARATIONS = [
    AnimalHomeComponent,
    AnimalNewComponent,
    AnimalDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AnimalRoutingModule { }