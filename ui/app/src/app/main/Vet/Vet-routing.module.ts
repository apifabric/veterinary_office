import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { VetHomeComponent } from './home/Vet-home.component';
import { VetNewComponent } from './new/Vet-new.component';
import { VetDetailComponent } from './detail/Vet-detail.component';

const routes: Routes = [
  {path: '', component: VetHomeComponent},
  { path: 'new', component: VetNewComponent },
  { path: ':id', component: VetDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Vet-detail-permissions'
      }
    }
  },{
    path: ':vet_id/Appointment', loadChildren: () => import('../Appointment/Appointment.module').then(m => m.AppointmentModule),
    data: {
        oPermission: {
            permissionId: 'Appointment-detail-permissions'
        }
    }
},{
    path: ':vet_id/Schedule', loadChildren: () => import('../Schedule/Schedule.module').then(m => m.ScheduleModule),
    data: {
        oPermission: {
            permissionId: 'Schedule-detail-permissions'
        }
    }
}
];

export const VET_MODULE_DECLARATIONS = [
    VetHomeComponent,
    VetNewComponent,
    VetDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class VetRoutingModule { }