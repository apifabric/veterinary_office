import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Allergy', loadChildren: () => import('./Allergy/Allergy.module').then(m => m.AllergyModule) },
    
        { path: 'Animal', loadChildren: () => import('./Animal/Animal.module').then(m => m.AnimalModule) },
    
        { path: 'Appointment', loadChildren: () => import('./Appointment/Appointment.module').then(m => m.AppointmentModule) },
    
        { path: 'Medicine', loadChildren: () => import('./Medicine/Medicine.module').then(m => m.MedicineModule) },
    
        { path: 'MedicineSupply', loadChildren: () => import('./MedicineSupply/MedicineSupply.module').then(m => m.MedicineSupplyModule) },
    
        { path: 'Owner', loadChildren: () => import('./Owner/Owner.module').then(m => m.OwnerModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'Prescription', loadChildren: () => import('./Prescription/Prescription.module').then(m => m.PrescriptionModule) },
    
        { path: 'Schedule', loadChildren: () => import('./Schedule/Schedule.module').then(m => m.ScheduleModule) },
    
        { path: 'Supplier', loadChildren: () => import('./Supplier/Supplier.module').then(m => m.SupplierModule) },
    
        { path: 'Treatment', loadChildren: () => import('./Treatment/Treatment.module').then(m => m.TreatmentModule) },
    
        { path: 'Vet', loadChildren: () => import('./Vet/Vet.module').then(m => m.VetModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }