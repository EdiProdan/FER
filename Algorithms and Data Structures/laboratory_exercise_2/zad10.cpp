#include <iostream>
using namespace std;

void selection2Sort(int *arr, int n, char smjer)
{
   for (int i = 0, j = n - 1; i < j; i++, j--)
   {
      int min = arr[i], max = arr[i];
      int min_i = i, max_i = i;
      if (smjer == '0')
      {
         for (int k = i; k <= j; k++)
         {
            if (arr[k] > max)
            {
               max = arr[k];
               max_i = k;
            }
            else if (arr[k] < min)
            {
               min = arr[k];
               min_i = k;
            }
         }

         // shifting the min.
         swap(arr[i], arr[min_i]);

         if (arr[min_i] == max)
            swap(arr[j], arr[min_i]);
         else
            swap(arr[j], arr[max_i]);
      }else if(smjer == '1'){
         for (int k = i; k <= j; k++)
         {
            if (arr[k] < max)
            {
               max = arr[k];
               max_i = k;
            }
            else if (arr[k] > min)
            {
               min = arr[k];
               min_i = k;
            }
         }

         // shifting the min.
         swap(arr[i], arr[min_i]);

         if (arr[min_i] == max)
            swap(arr[j], arr[min_i]);
         else
            swap(arr[j], arr[max_i]);
      }
   }
}

int main()
{

   int n;
   char c;
   cout << "Upisite n: ";
   cin >> n;
   cout << "Upisite smjer sortiranja (0 = uzlazno, 1 = silazno): ";
   cin >> c;

   int A[n];
   for (int i = 0; i < n; i++)
      cin >> A[i];

   selection2Sort(A, n, c);

   if (c == '0')
      cout << "Ispisujemo niz uzlazno..." << endl;
   else if (c == '1')
      cout << "Ispisujemo niz silazno..." << endl;

   for (int i = 0; i < n; i++)
      cout << A[i] << " ";

   return 0;
}