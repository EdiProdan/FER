#include <iostream>
#include <string.h>
using namespace std;

struct Zapis
{
   int sifra;
   string naziv;
};

void obicanBubbleSort(Zapis A[], int n, char smjer)
{
   for (int i = 0; i < n - 1; i++)
      for (int j = 0; j < n - 1 - i; j++)
      {
         if (smjer == '0')
         {
            if (A[j + 1].sifra < A[j].sifra)
               swap(A[j + 1], A[j]);
         }
         else if (smjer == '1')
         {
            if (A[j + 1].sifra > A[j].sifra)
               swap(A[j + 1], A[j]);
         }
      }
}

int main()
{
   /*
   Zapis z1, z2, z3;
   z1.naziv = "Juha";
   z1.sifra = 20;

   z2.naziv = "Meso";
   z2.sifra = 70;

   z3.naziv = "Kruh";
   z3.sifra = 5;
   */

   int n;
   char c;
   cout << "Upisite n: ";
   cin >> n;
   cout << "Upisite smjer sortiranja (0 = uzlazno, 1 = silazno): ";
   cin >> c;
   Zapis A[n];
   int sifra;
   string naziv;
   for (int i = 0; i < n; i++)
   {
      cout << "Zapis " << i + 1 << endl;
      cout << "Upisite sifru: ";
      cin >> A[i].sifra;
      cout << "Upisite naziv: ";
      cin >> A[i].naziv;
   }


   obicanBubbleSort(A, n, c);

   if (c == '0')
      cout << "Ispisujemo niz uzlazno..." << endl;
   else if (c == '1')
      cout << "Ispisujemo niz silazno..." << endl;




   return 0;
}