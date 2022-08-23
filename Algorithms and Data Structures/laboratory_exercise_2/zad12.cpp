#include <iostream>
#include <string.h>
using namespace std;

class Osoba
{
private:
   string ime;
   unsigned short int dob;

public:
   // Osoba(string ime, unsigned short int dob)
   // {
   //    this->ime = ime;
   //    this->dob = dob;
   // }

   void setIme(string ime)
   {
      this->ime = ime;
   }

   string getIme()
   {
      return ime;
   }
   void setDob(int dob)
   {
      this->dob = dob;
   }

   int getDob()
   {
      return dob;
   }

   friend bool operator<(const Osoba &first,
                         const Osoba &second)
   {
      if (first.dob < second.dob)
      {
         return true;
      }
      else if (first.dob == second.dob)
      {
         if (strcmp(first.ime.c_str(), second.ime.c_str()) < 0)
         {
            return true;
         }
         else
         {
            return false;
         }
      }
      return false;
   }
};

template <typename T>
void InsertionSort(T A[], int n)
{
   int i, j;
   for (i = 1; i < n; i++)
   {
      Osoba temp = A[i];
      for (j = i; j > 0 && temp < A[j - 1]; j--)
         A[j] = A[j - 1];

      A[j] = temp;
   }
}



int main()
{
   // Osoba o1("Ana", 20);
   // Osoba o2("Ivo", 9);
   // Osoba o3("Marko", 9);

   // Osoba o4("Lidija", 22);
   // Osoba o5("Pero", 19);

   // Osoba A[n] = {o1, o2, o3, o4, o5};

   int n;
   cout << "Upisite n: ";
   cin >> n;

   //Osoba A[10];
   Osoba *A = (Osoba *)malloc(sizeof(*A) * 10);
   string ime;
   int dob;
   for (int i = 0; i < n; i++)
   {
      cout << i + 1 << ". osoba" << endl;
      cout << "Upisite ime: ";
      cin >> ime;
      cout << "Upisite dob: ";
      cin >> dob;
      A[i].setIme(ime);
      A[i].setDob(dob);
   }

   cout << endl;
   InsertionSort(A, n);

   

   return 0;
}