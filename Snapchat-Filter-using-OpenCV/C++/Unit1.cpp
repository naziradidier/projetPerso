//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
String operation = "";
float ans = StrToFloat(Form1->Operation->Caption);
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
        : TForm(Owner)
{
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Button0Click(TObject *Sender)
{

        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"0";

}
//---------------------------------------------------------------------------

void __fastcall TForm1::Button1Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"1";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button2Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"2";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button3Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"3";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button4Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"4";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button5Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"5";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button6Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"6";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button7Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"7";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button8Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"8";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button9Click(TObject *Sender)
{
        Form1->Resultat->Caption = (Form1->Resultat->Caption)+"9";        
}
//---------------------------------------------------------------------------
void __fastcall TForm1::ButtonPlusClick(TObject *Sender)
{
        operation = operation+(Form1->Resultat->Caption)+"+";
        Form1->Operation->Caption = operation;
}
//---------------------------------------------------------------------------

void __fastcall TForm1::ButtonMoinsClick(TObject *Sender)
{
        operation = operation+(Form1->Resultat->Caption)+"-";
        Form1->Operation->Caption = operation;        
}
//---------------------------------------------------------------------------

void __fastcall TForm1::ButtonFoisClick(TObject *Sender)
{
        operation = operation+(Form1->Resultat->Caption)+"*";
        Form1->Operation->Caption = operation;        
}
//---------------------------------------------------------------------------

void __fastcall TForm1::ButtonDivClick(TObject *Sender)
{
        operation = operation+(Form1->Resultat->Caption)+"/";
        Form1->Operation->Caption = operation;        
}
//---------------------------------------------------------------------------

void __fastcall TForm1::ButtonClearClick(TObject *Sender)
{
        Form1->Operation->Caption = "0";
        Form1->Resultat->Caption = "0";        
}
//---------------------------------------------------------------------------



void __fastcall TForm1::ButtonEgalClick(TObject *Sender)
{
        operation = operation+(Form1->Resultat->Caption);
        Form1->Operation->Caption = operation;
        float res = StrToFloat(Form1->Operation->Caption);
        Form1->Resultat->Caption = FloatToStr (res);
}
//---------------------------------------------------------------------------

void __fastcall TForm1::ButtonAnsClick(TObject *Sender)
{
        Form1->Resultat->Caption = FloatToStr(ans);
}
//---------------------------------------------------------------------------




