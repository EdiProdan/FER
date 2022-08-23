#include <iostream>
using namespace std;

char *ostaviSlova(string ulaz)
{
   int len = ulaz.length();
   char *A = new char[len];
   int j = 0;
   for (int i = 0; i < len; i++)
   {
      if (isalpha(ulaz[i]))
      {
         A[j] = ulaz[i];
         j++;
      }
   }
   return A;
}

int main()
{
   string ulaz = "asp1";
   char *c = ostaviSlova(ulaz);
   for (int i = 0; i < ulaz.length(); i++)
      cout << c[i];

   delete c;
}