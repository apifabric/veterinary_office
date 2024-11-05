import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Allergy-card.component.html',
  styleUrls: ['./Allergy-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Allergy-card]': 'true'
  }
})

export class AllergyCardComponent {


}