#include <iostream>
using namespace std;

class Red
{
private:
   static const int MAX = 10;
   double *queue;
   int read;
   int write;

public:
   Red() : queue(new double[MAX]), read(0), write(0) {}
   ~Red() { delete[] queue; }

   bool dodaj(double broj)
   {
      if ((write + 1) % MAX == read)
         return false;
      queue[write] = broj;
      write = (write + 1) % MAX;
      return true;
   }
   bool skini(double *broj)
   {
      if (write == read)
         return false;
      *broj = queue[read];
      read = (read + 1) % MAX;
      return true;
   }
};




int main()
{
   Red q;
   q.dodaj(5);
   q.dodaj(7);
   q.dodaj(2);
   q.dodaj(3);
   double el;
   while (q.skini(&el))
   {
      cout << el << " ";
   }

   return 0;
}