#include <iostream>
#include <string.h>
using namespace std;

class Vozilo
{
private:
   string model;
   int godina;

public:
   Vozilo(string model, int godina)
   {
      this->model = model;
      this->godina = godina;
   }

   void setModel(string model)
   {
      this->model = model;
   }

   string getModel()
   {
      return model;
   }
   void setGodina(int godina)
   {
      this->godina = godina;
   }

   int getGodina()
   {
      return godina;
   }
   friend bool operator<(const Vozilo &first,
                         const Vozilo &second)
   {
      if (strcmp(first.model.c_str(), second.model.c_str()) == 0)
         return first.godina > second.godina;
      else if (strcmp(first.model.c_str(), second.model.c_str()) < 0)
         return true;
      else
         return false;
   }
};

void zamijeni(Vozilo &prvi, Vozilo &drugi)
{
   Vozilo tmp = prvi;
   prvi = drugi;
   drugi = tmp;
}

template <typename T>
void selectionSort(T A[], int n)
{
   int min;

   for (int i = 0; i < n; i++)
   {
      min = i;
      for (int j = i + 1; j < n; j++)
         if (A[j] < A[min])
            min = j;

      if (A[min] < A[i])
         zamijeni(A[min], A[i]);
   }
}

void print(Vozilo A[], int n)
{
   for (int i = 0; i < n; i++)
      cout << A[i].getModel() << " " << A[i].getGodina() << endl;

   cout << endl;
}

int main()
{
   // int n = 6;
   // Vozilo v1("Pauegot", 1981);
   // Vozilo v2("Pauegot", 1983);
   // Vozilo v3("Ranulet", 1967);
   // Vozilo v4("Fait", 1972);
   // Vozilo v5("BWM", 1985);
   // Vozilo v6("Merdesec", 1983);

   // Vozilo A[6] = {v1, v2, v3, v4, v5, v6};
   int n;
   cout << "Upisite n: ";
   cin >> n;

   
   Vozilo *A = (Vozilo *)malloc(sizeof(*A) * 10);
   string model;
   int godina;
   for (int i = 0; i < n; i++)
   {
      cout << i + 1 << ". vozilo" << endl;
      cout << "Upisite model: ";
      cin >> model;
      cout << "Upisite godinu: ";
      cin >> godina;
      A[i].setModel(model);
      A[i].setGodina(godina);
   }

   cout << endl;
   print(A, n);

   selectionSort(A, n);

   print(A, n);

   return 0;
}