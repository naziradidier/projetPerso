//-------------RSI--------------------------------------------------------------

#ifndef Unit3H
#define Unit3H
#include <StdCtrls.hpp>

#include "Unit2.h"

class rsi : etudiant {
        private:
                float note1, note2, note3, moyen;
        public:
                rsi(int, String, String, float, float, float);
                String getBultin();
                void setNote();
                float getmoyen();
};

//---------------------------------------------------------------------------
#endif
