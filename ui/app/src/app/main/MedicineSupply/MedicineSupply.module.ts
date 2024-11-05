import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {MEDICINESUPPLY_MODULE_DECLARATIONS, MedicineSupplyRoutingModule} from  './MedicineSupply-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    MedicineSupplyRoutingModule
  ],
  declarations: MEDICINESUPPLY_MODULE_DECLARATIONS,
  exports: MEDICINESUPPLY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MedicineSupplyModule { }