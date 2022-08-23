#include <iostream>
#include <cmath>
using namespace std;

long double rekurzija(int n, long double lambda1, long double lambda2, long double a0, long double a1)
{
   if (n == 0)
      return a0;
   
   else if (n == 1)
      return a1;
   
   else
   
      return (lambda1 * rekurzija(n - 1, lambda1, lambda2, a0, a1)) + (lambda2 * rekurzija(n - 2, lambda1, lambda2, a0, a1));
}

long double formula(int n, long double lambda1, long double lambda2, long double a0, long double a1)
{
   double x1, x2, alfa, beta, trazeni_clan, diskriminanta;

   diskriminanta = pow(lambda1, 2.) - 4 * (-lambda2);

   x1 = ((lambda1) + sqrt(diskriminanta)) / 2.;
   x2 = ((lambda1)-sqrt(diskriminanta)) / 2.;

   if (diskriminanta == 0)
   {
      alfa = a0;
      beta = (a1 - a0) / x1;
      trazeni_clan = alfa * pow(x1, n) + beta * n * pow(x2, n);
   }
   else
   {
      beta = (a1 - a0 * x1) / (x2 - x1);
      alfa = a0 - beta;
      trazeni_clan = alfa * pow(x1, n) + beta * pow(x2, n);
   }

   return trazeni_clan;
}

int main()
{
   long double lambda1, lambda2, a0, a1;
   int n;

   cout << "Unesite prvi koeficijent λ_1 rekurzivne relacije: ";
   cin >> lambda1;
   cout << "Unesite drugo koeficijent λ_2 rekurzivne relacije: ";
   cin >> lambda2;
   cout << "Unesite vrijednost nultog clana niza a_0: ";
   cin >> a0;
   cout << "Unesite vrijednost prvog clana niza a_1: ";
   cin >> a1;
   cout << "Unesite redni broj n trazenog clana niza: ";
   cin >> n;
   cout << endl;

   cout << "Vrijednost n-tog clana niza pomocu formule: " << formula(n, lambda1, lambda2, a0, a1) << endl;
   cout << "Vrijednost n-tog clana niza pomocu rekurzije: " << rekurzija(n, lambda1, lambda2, a0, a1);

   return 0;
}