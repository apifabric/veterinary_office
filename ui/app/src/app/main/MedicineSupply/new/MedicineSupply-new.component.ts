import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'MedicineSupply-new',
  templateUrl: './MedicineSupply-new.component.html',
  styleUrls: ['./MedicineSupply-new.component.scss']
})
export class MedicineSupplyNewComponent {
  @ViewChild("MedicineSupplyForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}