//---------------------------------------------------------------------------

#ifndef Unit1H
#define Unit1H
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
//---------------------------------------------------------------------------
class TForm1 : public TForm
{
__published:	// Composants gérés par l'EDI
        TStaticText *Operation;
        TStaticText *Resultat;
        TButton *Button1;
        TButton *Button2;
        TButton *Button3;
        TButton *Button4;
        TButton *Button5;
        TButton *Button6;
        TButton *Button7;
        TButton *Button8;
        TButton *Button9;
        TButton *Button0;
        TButton *ButtonAns;
        TButton *ButtonPlus;
        TButton *ButtonMoins;
        TButton *ButtonFois;
        TButton *ButtonDiv;
        TButton *ButtonEgal;
        TButton *ButtonDel;
        TButton *ButtonClear;
        void __fastcall Button0Click(TObject *Sender);
        void __fastcall Button1Click(TObject *Sender);
        void __fastcall Button2Click(TObject *Sender);
        void __fastcall Button3Click(TObject *Sender);
        void __fastcall Button4Click(TObject *Sender);
        void __fastcall Button5Click(TObject *Sender);
        void __fastcall Button6Click(TObject *Sender);
        void __fastcall Button7Click(TObject *Sender);
        void __fastcall Button8Click(TObject *Sender);
        void __fastcall Button9Click(TObject *Sender);
        void __fastcall ButtonPlusClick(TObject *Sender);
        void __fastcall ButtonMoinsClick(TObject *Sender);
        void __fastcall ButtonFoisClick(TObject *Sender);
        void __fastcall ButtonDivClick(TObject *Sender);
        void __fastcall ButtonClearClick(TObject *Sender);
        void __fastcall ButtonEgalClick(TObject *Sender);
        void __fastcall ButtonAnsClick(TObject *Sender);
private:	// Déclarations de l'utilisateur
public:		// Déclarations de l'utilisateur
        __fastcall TForm1(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TForm1 *Form1;
//---------------------------------------------------------------------------
#endif
