#include <iostream>
using namespace std;

class Red
{
private:
   struct Cvor
   {
      double data;
      Cvor *next;
   };
   Cvor *read = nullptr;
   Cvor *write = nullptr;

public:
   bool dodaj(double broj)
   {
      Cvor *newElement = new (nothrow) Cvor;
      if (newElement == nullptr)
         return false;
      newElement->data = broj;
      newElement->next = nullptr;
      if (!write)
         read = newElement;
      else
         write->next = newElement;

      write = newElement;
      return true;
   }

   bool poljeURed(int polje[], int n)
   {
      if (n == 0)
         return true;

      if (!dodaj(polje[n - 1]))
         return false;

      cout << "Upisujem " << polje[n - 1] << endl;
      return poljeURed(polje, n - 1);
   }
  
};

int main()
{
   Red q;
   int arr[] = {1, 2, 3, 4, 5};
   int n = 5;
   q.poljeURed(arr, n);

   return 0;
}