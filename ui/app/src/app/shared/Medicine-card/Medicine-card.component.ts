import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Medicine-card.component.html',
  styleUrls: ['./Medicine-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Medicine-card]': 'true'
  }
})

export class MedicineCardComponent {


}