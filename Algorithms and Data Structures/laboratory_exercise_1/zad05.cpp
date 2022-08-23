#include <iostream>
using namespace std;

template <typename T>
int binarnoTrazi(T polje[], int n, T x)
{
   int dg = 0, gg = n - 1, sredina;
   while (dg <= gg)
   {
      sredina = (dg + gg) / 2;
      if (x == polje[sredina])
         return sredina;
      else if (x < polje[sredina])
         gg = sredina - 1;
      else
         dg = sredina + 1;
   }
   return -1;
}

int main()
{
   int n;
   cout << "Upisite n: ";
   cin >> n;
   float x;
   cout << "Upisite x: ";
   cin >> x;

   float *A1 = new float[n];
   int *A2 = new int[n];

   for (int i = 0; i < n; i++)
      A1[i] = i * 1.1;

   for (int i = 0; i < n; i++)
      cout << A1[i] << " ";

   cout << binarnoTrazi(A1, n, x);

   // for (int i = 0; i < n; i++)
   //    A2[i] = i * 3;

   // for (int i = 0; i < n; i++)
   //    cout << A1[i] << " ";

   return 0;
}
