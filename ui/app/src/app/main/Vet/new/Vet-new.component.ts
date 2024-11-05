import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Vet-new',
  templateUrl: './Vet-new.component.html',
  styleUrls: ['./Vet-new.component.scss']
})
export class VetNewComponent {
  @ViewChild("VetForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}