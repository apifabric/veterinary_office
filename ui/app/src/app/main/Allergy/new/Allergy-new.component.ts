import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Allergy-new',
  templateUrl: './Allergy-new.component.html',
  styleUrls: ['./Allergy-new.component.scss']
})
export class AllergyNewComponent {
  @ViewChild("AllergyForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}