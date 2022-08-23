#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <string.h>
using namespace std;

void printNeighbourDetails(int l, vector<int> &neighbours, vector<int> &neighbourColors)
{
   cout << "Vrh " << l << " je susjedan s vrhovima: ";
   for (int i = 0; i < neighbours.size(); i++)
      cout << neighbours[i] << " ";
   cout << endl;

   cout << "Susjedi vrha " << l << " su obojani bojama: ";
   for (int i = 0; i < neighbourColors.size(); i++)
      cout << neighbourColors[i] << " ";
   cout << endl
        << endl;
}

void printMapDetails(map<int, int> &mapOfVertexes)
{
   map<int, int>::iterator itr;
   cout << "Mapa vrhova i njihovih obojenja: \n";
   cout << "\tKEY\tELEMENT\n";
   for (itr = mapOfVertexes.begin(); itr != mapOfVertexes.end(); ++itr)
   {
      cout << '\t' << itr->first
           << '\t' << itr->second << '\n';
   }
   cout << endl;
}

int colorGraph(int n, vector<vector<int> > adj)
{
   map<int, int> mapOfVertexes;
   vector<int> colorsUsed;
   int k, l;
   for (k = 0; k < n; k++)
   {
      // bojamo v0 bojom 0
      if (mapOfVertexes.empty())
      {
         mapOfVertexes.insert(pair<int, int>(k, 0));
         colorsUsed.push_back(0);
      }

      for (l = 0; l < n; l++)
      {
         // ako je element jednak 1, tj. susjedan je
         if (adj[k][l] == 1)
         {
            // provjera ako je vrh vec obojan
            if (mapOfVertexes.find(l) == mapOfVertexes.end())
            {
               // nije obojan

               // pronalazimo susjede vrha l
               vector<int> neighbours;
               for (int i = 0; i < n; i++)
                  if (adj[l][i] == 1)
                     neighbours.push_back(i);

               // pamtimo boje kojima su susjedi obojani
               vector<int> neighbourColors;
               for (int i = 0; i < neighbours.size(); i++)
               {
                  // pronasli smo kljuc susjeda, stavljamo njegovu vrijednost
                  if (mapOfVertexes.find(neighbours[i]) != mapOfVertexes.end())
                     neighbourColors.push_back(mapOfVertexes.find(neighbours[i])->second);
                  // inace ako kljuc susjeda ne postoji, zanemari
               }

               // printNeighbourDetails(l, neighbours, neighbourColors);

               int i;
               for (i = 0; i < n; i++)
               {
                  // ako se broj od 0 do n ne nalazi u bojama susjeda, izlazimo iz petlje
                  if (find(neighbourColors.begin(), neighbourColors.end(), i) == neighbourColors.end())
                     break;
               }
               // i sada ima vrijednost kojom bojamo vrh l

               mapOfVertexes.insert(pair<int, int>(l, i));
               if (find(colorsUsed.begin(), colorsUsed.end(), i) == colorsUsed.end())
                  colorsUsed.push_back(i);

               // upisujemo najmanji prirodan broj koji se ne nalazi u polju
            }
            // inace je obojan
         }
      }
   }
   // printMapDetails(mapOfVertexes);
   return colorsUsed.size();
}

void changeMatrix(vector<vector<int> > &adj, int n, int permutation)
{
   for (int i = 0; i < n; i++)
      swap(adj[0][i], adj[permutation][i]);
   for (int i = 0; i < n; i++)
      swap(adj[i][0], adj[i][permutation]);
}

void readGraph(int &n, int &lenS, vector<int> &S)
{
   string f;
   cout << "Upisite naziv datoteke: ";
   getline(cin, f);

   ifstream graphFile(f);

   if (graphFile.is_open())
   {
      int fn, flenS, fs;
      graphFile >> fn;
      n = fn;
      graphFile >> flenS;
      lenS = flenS;
      while (graphFile.good())
      {
         graphFile >> fs;
         S.push_back(fs);
      }
   }
   else
      graphFile.close();
}

int main()
{
   int n, lenS;
   vector<int> S;
   vector<int> results;

   readGraph(n, lenS, S);

   // inicijalizacija matrice susjedstva
   vector<vector<int> > adj(n, vector<int>(n, 0));
   for (int k = 0; k < n; k++)
   {
      for (int l = 0; l < n; l++)
      {
         int dif = k - l;
         if (find(S.begin(), S.end(), abs(dif)) != S.end())
            adj[k][l] = 1;
      }
   }

   // ispis matrice susjedstva
  
   for (int i = 0; i < n; i++)
   {
      for (int j = 0; j < n; j++)
         cout << adj[i][j] << " ";
      cout << endl;
   }
   cout << endl;
   

   int permutation;
   // start of for
   for (permutation = 1; permutation < n; permutation++)
   {
      int kromatskiBroj = colorGraph(n, adj);
      results.push_back(kromatskiBroj);

      changeMatrix(adj, n, permutation);
   }
   // end of for

   cout << "Kromatski broj zadanog grafa je " << *min_element(results.begin(), results.end()) << endl;

   return 0;
}