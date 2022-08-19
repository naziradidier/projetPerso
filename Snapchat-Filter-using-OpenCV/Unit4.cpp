//-------------------IDEV--------------------------------------------------------


#pragma hdrstop

#include "Unit4.h"

idev::idev(int a, String b, String c, float x, float y){
        this->Age = a;
        this->Nom = b;
        this->Prenom = c;
        this->note1 = x;
        this->note2 = y ;
}

void idev::setNote(){
        this->moyen = (this->note1 + this->note2 )/2;
}

float idev::getmoyen(){
        return (this->moyen);
}

String idev::getBultin(){
        return (
                this->identity()
                +
                "Sa moyenne: "
                +
                this->getmoyen()
        );
}


//---------------------------------------------------------------------------

#pragma package(smart_init)

