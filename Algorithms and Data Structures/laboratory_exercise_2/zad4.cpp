#include <iostream>
#include <time.h>
using namespace std;

template <class T>
class Stack
{
private:
   template <class X>
   struct StackElement
   {
      X item;
      StackElement<X> *next;
   };
   StackElement<T> *top = nullptr;

public:
   Stack() : top(nullptr){};

   bool push(T item)
   {
      StackElement<T> *newElement = new (nothrow) StackElement<T>;
      if (newElement == nullptr)
      {
         return false;
      }
      newElement->item = item;
      newElement->next = top;
      top = newElement;
      return true;
   }
   void ispis()
   {
      StackElement<T> *p = top;
      while (p)
      {
         cout << p->item << " ";
         p = p->next;
      }
   }
};

int main()
{
   srand(unsigned(time(NULL)));
   Stack<int> s;
   for (int i = 0; i < 101; i++)
   {
      s.push(rand() % 1000);
   }

   s.ispis();

   return 0;
}