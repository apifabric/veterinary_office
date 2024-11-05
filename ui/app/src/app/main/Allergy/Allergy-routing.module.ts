import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AllergyHomeComponent } from './home/Allergy-home.component';
import { AllergyNewComponent } from './new/Allergy-new.component';
import { AllergyDetailComponent } from './detail/Allergy-detail.component';

const routes: Routes = [
  {path: '', component: AllergyHomeComponent},
  { path: 'new', component: AllergyNewComponent },
  { path: ':id', component: AllergyDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Allergy-detail-permissions'
      }
    }
  }
];

export const ALLERGY_MODULE_DECLARATIONS = [
    AllergyHomeComponent,
    AllergyNewComponent,
    AllergyDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AllergyRoutingModule { }