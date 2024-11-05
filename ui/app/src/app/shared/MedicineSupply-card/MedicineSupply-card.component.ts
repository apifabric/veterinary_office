import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './MedicineSupply-card.component.html',
  styleUrls: ['./MedicineSupply-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.MedicineSupply-card]': 'true'
  }
})

export class MedicineSupplyCardComponent {


}