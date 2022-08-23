#include <iostream>
using namespace std;

template <class T>
class List
{
   template <class X>
   struct Cvor
   {
      X element;
      Cvor<X> *next;
   };

   Cvor<T> *head = nullptr;

public:
   bool upis(T element)
   {
      Cvor<T> *newElement = new (nothrow) Cvor<T>;
      if (newElement == nullptr)
         return false;
      newElement->element = element;
      Cvor<T> **p;
      for (p = &head; *p && element > (*p)->element; p = &((*p)->next))
         ;
      newElement->next = *p;
      *p = newElement;

      return true;
   }

   void ispis()
   {

      Cvor<T> **p;
      for (p = &head; *p; p = &((*p)->next))
         cout << (*p)->element << " ";

      return;
   }
};

int main()
{
   List<int> l;
   l.upis(2);
   l.upis(3);
   l.upis(5);
   l.upis(7);
   l.upis(4);
   l.upis(8);
   l.ispis();
   return 0;
}