// #include <iostream>

// using namespace std;

// class SanitizedString
// {
// private:
//    std::string str;

// public:
//    SanitizedString(std::string str)
//    {
//       this->str = str;
//    }
//    void removeDuplicateWhiteSpace(std::string ulaz)
//    {
//       for (int i = 0; i < ulaz.length(); i++)
//       {
//          if (isspace(ulaz[i]) && isspace(ulaz[i + 1]))
//          {
//             ulaz.erase(i, 1);
//             i--;
//          }
//       }
//       cout << ulaz;
//    }
//    void removeNonAlphaChars(std::string ulaz)
//    {
//       for (int i = 0; i < ulaz.length(); i++)
//       {
//          if (!isalpha(ulaz[i]))
//          {
//             ulaz.erase(i, 1);
//             i--;
//          }
//       }
//       cout << ulaz;
//    }

//    friend ostream &operator<<(ostream &os, const SanitizedString str)
//    {
//       os << str.str;
//       return os;
//    }
// };

// int main()
// {
//    std::string ulaz = "M~ir4ko&";

//    SanitizedString ss(ulaz);
//    ss.removeNonAlphaChars(ulaz);

//    return 0;
// }

#include <iostream>

class SanitizedString
{
private:
   std::string str;

public:
   SanitizedString(std::string str)
   {
      this->str = str;
   }
   void removeDuplicateWhiteSpace(std::string ulaz)
   {
   }

   friend std::ostream &operator<<(std::ostream &os, const SanitizedString str)
   {
      os << str.str;
      return os;
   }
};

int main(){
   
}
