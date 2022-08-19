//----------------IDEV-----------------------------------------------------------

#ifndef Unit4H
#define Unit4H
#include <StdCtrls.hpp>

#include "Unit2.h"

class idev : etudiant {
        private:
                float note1, note2, moyen;
        public:
                idev(int, String, String, float, float);
                String getBultin();
                void setNote();
                float getmoyen();
};

//---------------------------------------------------------------------------
#endif
 