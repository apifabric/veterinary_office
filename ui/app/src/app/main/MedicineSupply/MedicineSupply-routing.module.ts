import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MedicineSupplyHomeComponent } from './home/MedicineSupply-home.component';
import { MedicineSupplyNewComponent } from './new/MedicineSupply-new.component';
import { MedicineSupplyDetailComponent } from './detail/MedicineSupply-detail.component';

const routes: Routes = [
  {path: '', component: MedicineSupplyHomeComponent},
  { path: 'new', component: MedicineSupplyNewComponent },
  { path: ':id', component: MedicineSupplyDetailComponent,
    data: {
      oPermission: {
        permissionId: 'MedicineSupply-detail-permissions'
      }
    }
  }
];

export const MEDICINESUPPLY_MODULE_DECLARATIONS = [
    MedicineSupplyHomeComponent,
    MedicineSupplyNewComponent,
    MedicineSupplyDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MedicineSupplyRoutingModule { }