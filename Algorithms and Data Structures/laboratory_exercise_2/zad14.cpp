#include <iostream>
#include <string.h>

using namespace std;

void zamijeni(string *prvi, string *drugi)
{
   string tmp = *prvi;
   *prvi = *drugi;
   *drugi = tmp;
}

void BubbleSortPoboljsani(string A[], int n, int smjer)
{
   int i, j;
   bool flag = 1;
   for (i = 0; flag == 1; i++)
   {
      flag = 0;
      for (j = 0; j < n - 1 - i; j++)
      {
         if (smjer == 0)
         {
            if (strcmp(A[j + 1].c_str(), A[j].c_str()) >= 0)
            {
               zamijeni(&A[j + 1], &A[j]);
               flag = 1;
            }
         }
         else if (smjer == 1)
         {
            if (strcmp(A[j + 1].c_str(), A[j].c_str()) < 0)
            {
               zamijeni(&A[j + 1], &A[j]);
               flag = 1;
            }
         }
      }
   }
}

int main()
{
   int n, smjer;
   cout << "Upisite n: ";
   cin >> n;
   cout << "Upisite smjer sortiranja (0 = uzlazno, 1 = silazno): ";
   cin >> smjer;
   // string A[10] = {"Ivo", "Marko", "Juraj", "Pero"};
   //string *A = (string *)malloc(sizeof(*A) * 10);
   string *A = new string[10];
   for (int i = 0; i < n; i++)
   {
      cin >> A[i]; 
   }
   

   BubbleSortPoboljsani(A, n, smjer);

   for (int i = 0; i < n; i++)
      cout << A[i] << " ";

   return 0;
}