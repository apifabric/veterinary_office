import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ANIMAL_MODULE_DECLARATIONS, AnimalRoutingModule} from  './Animal-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AnimalRoutingModule
  ],
  declarations: ANIMAL_MODULE_DECLARATIONS,
  exports: ANIMAL_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AnimalModule { }