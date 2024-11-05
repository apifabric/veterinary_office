import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Vet-card.component.html',
  styleUrls: ['./Vet-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Vet-card]': 'true'
  }
})

export class VetCardComponent {


}