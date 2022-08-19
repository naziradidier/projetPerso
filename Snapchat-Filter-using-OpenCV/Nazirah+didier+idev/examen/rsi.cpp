//-------------------RSI--------------------------------------------------------


#pragma hdrstop

#include "Unit3.h"

rsi::rsi(int a, String b, String c, float x, float y, float z){
        this->Age = a;
        this->Nom = b;
        this->Prenom = c;
        this->note1 = x;
        this->note2 = y ;
        this->note3 = z;
}

void rsi::setNote(){
        this->moyen = (this->note1 + this->note2 + this->note3)/3;
}

float rsi::getmoyen(){
        return (this->moyen);
}

String rsi::getBulletin(){
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

