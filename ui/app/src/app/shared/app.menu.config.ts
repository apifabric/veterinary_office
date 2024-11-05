import { MenuRootItem } from 'ontimize-web-ngx';

import { AllergyCardComponent } from './Allergy-card/Allergy-card.component';

import { AnimalCardComponent } from './Animal-card/Animal-card.component';

import { AppointmentCardComponent } from './Appointment-card/Appointment-card.component';

import { MedicineCardComponent } from './Medicine-card/Medicine-card.component';

import { MedicineSupplyCardComponent } from './MedicineSupply-card/MedicineSupply-card.component';

import { OwnerCardComponent } from './Owner-card/Owner-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { PrescriptionCardComponent } from './Prescription-card/Prescription-card.component';

import { ScheduleCardComponent } from './Schedule-card/Schedule-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { TreatmentCardComponent } from './Treatment-card/Treatment-card.component';

import { VetCardComponent } from './Vet-card/Vet-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Allergy', name: 'ALLERGY', icon: 'view_list', route: '/main/Allergy' }
    
        ,{ id: 'Animal', name: 'ANIMAL', icon: 'view_list', route: '/main/Animal' }
    
        ,{ id: 'Appointment', name: 'APPOINTMENT', icon: 'view_list', route: '/main/Appointment' }
    
        ,{ id: 'Medicine', name: 'MEDICINE', icon: 'view_list', route: '/main/Medicine' }
    
        ,{ id: 'MedicineSupply', name: 'MEDICINESUPPLY', icon: 'view_list', route: '/main/MedicineSupply' }
    
        ,{ id: 'Owner', name: 'OWNER', icon: 'view_list', route: '/main/Owner' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Prescription', name: 'PRESCRIPTION', icon: 'view_list', route: '/main/Prescription' }
    
        ,{ id: 'Schedule', name: 'SCHEDULE', icon: 'view_list', route: '/main/Schedule' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'Treatment', name: 'TREATMENT', icon: 'view_list', route: '/main/Treatment' }
    
        ,{ id: 'Vet', name: 'VET', icon: 'view_list', route: '/main/Vet' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AllergyCardComponent

    ,AnimalCardComponent

    ,AppointmentCardComponent

    ,MedicineCardComponent

    ,MedicineSupplyCardComponent

    ,OwnerCardComponent

    ,PaymentCardComponent

    ,PrescriptionCardComponent

    ,ScheduleCardComponent

    ,SupplierCardComponent

    ,TreatmentCardComponent

    ,VetCardComponent

];