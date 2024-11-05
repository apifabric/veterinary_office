import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {MEDICINE_MODULE_DECLARATIONS, MedicineRoutingModule} from  './Medicine-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    MedicineRoutingModule
  ],
  declarations: MEDICINE_MODULE_DECLARATIONS,
  exports: MEDICINE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MedicineModule { }