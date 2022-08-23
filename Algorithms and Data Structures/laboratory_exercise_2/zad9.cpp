#include <iostream>
#include <string>
using namespace std;

struct Zapis
{
   int postanskiBroj;
   string mjesto;
};

void insertionSort(Zapis A[], int n, char smjer)
{
   int i, j;
   Zapis tempZ;
   for (i = 1; i < n; i++)
   {
      tempZ = A[i];
      if (smjer == '0')
         for (j = i; j > 0 && A[j - 1].postanskiBroj > tempZ.postanskiBroj; j--)
            A[j] = A[j - 1];

      else if (smjer == '1')
         for (j = i; j > 0 && A[j - 1].postanskiBroj < tempZ.postanskiBroj; j--)
            A[j] = A[j - 1];

      A[j] = tempZ;
   }
}


int main()
{
   /*
   int n = 5;
   Zapis a1, a2, a3, a4, a5;

   a1.mjesto = "Rijeka";
   a1.postanskiBroj = 51000;

   a2.mjesto = "Zagreb";
   a2.postanskiBroj = 10000;

   a3.mjesto = "Split";
   a3.postanskiBroj = 21000;

   a4.mjesto = "Osijek";
   a4.postanskiBroj = 31000;

   a5.mjesto = "Dubrovnik";
   a5.postanskiBroj = 20000;
   Zapis A[5] = {a1, a2, a3, a4, a5};
   */
   int n;
   char c;
   cout << "Upisite n: ";
   cin >> n;
   cout << "Upisite smjer sortiranja (0 = uzlazno, 1 = silazno): ";
   cin >> c;
   Zapis A[10];
   string mjesto;
   int postanskiBroj;
   for (int i = 0; i < n; i++)
   {
      cout << "Zapis " << i + 1 << endl;
      cout << "Upisite mjesto: ";
      cin >> A[i].mjesto;
      cout << "Upisite postanski broj: ";
      cin >> A[i].postanskiBroj;
   }

   insertionSort(A, n, c);
   return 0;
}