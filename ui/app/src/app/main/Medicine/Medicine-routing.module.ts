import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MedicineHomeComponent } from './home/Medicine-home.component';
import { MedicineNewComponent } from './new/Medicine-new.component';
import { MedicineDetailComponent } from './detail/Medicine-detail.component';

const routes: Routes = [
  {path: '', component: MedicineHomeComponent},
  { path: 'new', component: MedicineNewComponent },
  { path: ':id', component: MedicineDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Medicine-detail-permissions'
      }
    }
  },{
    path: ':medicine_id/MedicineSupply', loadChildren: () => import('../MedicineSupply/MedicineSupply.module').then(m => m.MedicineSupplyModule),
    data: {
        oPermission: {
            permissionId: 'MedicineSupply-detail-permissions'
        }
    }
},{
    path: ':medicine_id/Prescription', loadChildren: () => import('../Prescription/Prescription.module').then(m => m.PrescriptionModule),
    data: {
        oPermission: {
            permissionId: 'Prescription-detail-permissions'
        }
    }
}
];

export const MEDICINE_MODULE_DECLARATIONS = [
    MedicineHomeComponent,
    MedicineNewComponent,
    MedicineDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MedicineRoutingModule { }