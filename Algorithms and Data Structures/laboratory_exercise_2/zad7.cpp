#include <iostream>
using namespace std;
class Red
{
private:
   struct Cvor
   {
      double element;
      Cvor *next;
   };
   Cvor *read = nullptr;
   Cvor *write = nullptr;

public:
   Red() : read(nullptr), write(nullptr){};
   ~Red()
   {
      double x;
      while (skini(&x))
         ;
   }
   bool dodaj(double broj)
   {
      Cvor *newElement = new (nothrow) Cvor;
      if (newElement == nullptr)
         return false;
      newElement->next = nullptr;
      newElement->element = broj;
      if (!write)
         read = newElement;
      else
         write->next = newElement;
      
      write = newElement;

      return true;
   }
   bool skini(double *broj)
   {
      if (read == nullptr)
         return false;
      *broj = read->element;
      Cvor *tmp = read;
      read = read->next;
      if (read == nullptr)
         write = nullptr;
      delete tmp;
      return true;
   }
};

int main()
{
   Red q;
   q.dodaj(4);
   q.dodaj(3);
   q.dodaj(1);
   q.dodaj(6);
   double el;
   while (q.skini(&el))
      cout << el << " ";
   

   return 0;
}