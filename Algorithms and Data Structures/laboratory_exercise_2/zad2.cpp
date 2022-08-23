#include <iostream>
#include <string.h>
using namespace std;

template <class T>
class List
{

   template <class X>
   struct Cvor
   {
      X element;
      Cvor<X> *next;
      Cvor<X> *prev;
   };
   Cvor<T> *head = nullptr;
   Cvor<T> *tail = nullptr;

private:
public:
   bool upis(string element)
   {
      Cvor<string> *newElement = new (nothrow) Cvor<string>;
      if (newElement == nullptr)
         return false;

      newElement->element = element;
      newElement->next = nullptr;
      if (!tail)
         head = newElement;
      else
         tail->next = newElement;
         
      tail = newElement;

      return true;
   }
   void ispis()
   {
      Cvor<string> **p;
      for (p = &head; *p; p = &((*p)->next))
         cout << (*p)->element << " ";      
   }
};
int main()
{
   List<string> l;
   l.upis("ab");
   l.upis("bsd");
   l.upis("abdsf");
   l.upis("fdsa");
   l.upis("absdafaf");
   l.ispis();

   return 0;
}