// #include <iostream>
// #include <cmath>
//using namespace std;
// double exp(double x, int n, int *fakt, double *xpot)
// {
//    if (n == 0)
//    {
//             cout << n << "n 0   ";

//       *fakt = 1;
//       *xpot = 1;
//       return 1;
//    }
//    else
//    {

//       double retVal = exp(x, n - 1, fakt, xpot) + (*xpot) / (*fakt);
//                   cout << n << "n x   ";

//       (*fakt) *= n + 1;
//       (*xpot) *= x;
//       return retVal;
//    }
// }

// int main()
// {
//    int x, n;
//    cin >> x;
//    cin >> n;
//    int fakt;
//    double pot;
//    double *A = new double[n];
//    for (int i = 0; i < n; i++)
//    {
//       cout << i << endl;
//       A[i] = exp(x, i, &fakt, &pot);
//       cout << A[i] << " ";
//    }

//    return 0;
// }

#include <iostream>
double exp(double x, int n, int *fakt, double *xpot)
{
   if (n == 0)
   {
      *fakt = 1;
      *xpot = 1;
      return 1;
   }
   else
   {
      double retVal = exp(x, n - 1, fakt, xpot) + (*xpot) / (*fakt);
      (*xpot) *= x;
      (*fakt) *= n + 1;
      return retVal;
   }
}

int main()
{
   int fakt;
   double xpot;
   int n = 4;
   double x = 1;

   double *A = new double[n];
   for (int i = 0; i < n; i++)
   {
      A[i] = exp(x, i, &fakt, &xpot);
      std::cout << A[i] << " ";
   }
}