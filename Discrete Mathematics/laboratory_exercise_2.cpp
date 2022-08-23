#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int findPermutations(int arr[], int n, vector<vector<int> > &matrix)
{
   sort(arr, arr + n);
   int duljina = 0;
   int min = 99999;

   do
   {

      duljina = 0;
      int k, l;
      for (int i = 0; i < n - 1; i++)
      {
         k = arr[i];
         l = arr[i + 1];
         duljina += matrix[k][l];
      }
      duljina += matrix[arr[0]][arr[n - 1]];
      if (duljina < min)
      {
         min = duljina;
      }
   } while (next_permutation(arr, arr + n));

   return min;
}
int main()
{
   int n, a, b;

   cout << "Unesite redom, odvojene razmakom, parametre n, a i b: ";
   cin >> n >> a >> b;
   cout << endl;

   vector<vector<int> > weights(n, vector<int>(n));

   // ucitavamo matricu tezina
   for (int k = 1; k <= n; k++)
   {
      for (int l = 1; l <= n; l++)
      {
         if (l == k)
            weights[k - 1][l - 1] = 0;

         else if (l > k)
         {
            weights[k - 1][l - 1] = (pow((a * k + b * l), 2.) + 1);
            weights[l - 1][k - 1] = (pow((a * k + b * l), 2.) + 1);
         }
      }
   }

   /* printamo matricu tezina
   for (int i = 0; i < n; i++)
   {
      for (int j = 0; j < n; j++)
         printf("%4d", weights[i][j]);
      cout << endl;
   }
   cout << endl;
   */
   
   vector<int> path;

   //pohlepni

   // pronalazimo brid najmanje tezine
   int min = 99999;
   int cur, v1, v2, duljina = 0;

   for (int k = 0; k < n; k++)
   {
      for (int l = 0; l < n; l++)
      {
         cur = weights[k][l];
         if (cur > 0 && cur < min)
         {
            min = cur;
            v1 = k;
            v2 = l;
         }
      }
   }
   duljina += min;

   bool contains;
   int l1, l2, tmpV1, tmpV2;

   while (path.size() < n - 2)
   {
      // trazimo sljedeci najmanji brid za v1
      int min1 = 99999;

      for (l1 = 0; l1 < n; l1++)
      {
         cur = weights[v1][l1];
         contains = false;

         if (find(path.begin(), path.end(), l1) != path.end())
            contains = true;

         if (cur > 0 && l1 != v2 && !contains && cur < min1)
         {
            min1 = cur;
            tmpV1 = l1;
         }
      }

      // trazimo sljedeci najmanji brid za v2
      int min2 = 99999;

      for (l2 = 0; l2 < n; l2++)
      {
         cur = weights[v2][l2];
         contains = false;

         if (find(path.begin(), path.end(), l2) != path.end())
            contains = true;

         if (cur > 0 && l2 != v1 && !contains && cur < min2)
         {
            min2 = cur;
            tmpV2 = l2;
         }
      }

      // trazimo manji od svakog brida

      if (min1 <= min2)
      {
         path.push_back(v1);
         v1 = tmpV1;
         duljina += min1;
      }
      else
      {
         path.push_back(v2);
         v2 = tmpV2;
         duljina += min2;
      }

   }

   duljina += weights[v1][v2];

   // u vektor "path" ubacujemo preostala dva vrha
   if (find(path.begin(), path.end(), v1) == path.end())
      path.push_back(v1);
   if (find(path.begin(), path.end(), v2) == path.end())
      path.push_back(v2);


   // iscrpni
   int arrOfPermutations[n];
   for (int i = 0; i < n; i++)
      arrOfPermutations[i] = i;

   int duljinaIscrpnog = findPermutations(arrOfPermutations, n, weights);

   cout << "Pohlepni algoritam nalazi ciklus duljine " << duljina << endl << endl;
   cout << "Iscrpni algoritam nalazi ciklus duljine " << duljinaIscrpnog << endl << endl;
   if (duljina == duljinaIscrpnog)
      cout << "Pohlepni algoritam na ovom grafu daje optimalno rješenje!" << endl << endl;
   else
      cout << "Pohlepni algoritam na ovom grafu ne daje optimalno rješenje!" << endl << endl;

   return 0;
}