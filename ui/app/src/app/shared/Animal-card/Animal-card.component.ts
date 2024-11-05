import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Animal-card.component.html',
  styleUrls: ['./Animal-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Animal-card]': 'true'
  }
})

export class AnimalCardComponent {


}