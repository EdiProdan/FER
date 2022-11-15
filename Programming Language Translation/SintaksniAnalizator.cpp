#include <iostream>
#include <utility>
#include <vector>
#include <fstream>

using namespace std;

class SintaksniAnalizator {
private:
    vector<string> input;
    vector<string> inputString;
    vector<string> output;
    string outputLine;
    size_t i;
    int depth;

public:
    SintaksniAnalizator(vector<string> input, vector<string> inputString) {
        this->input = std::move(input);
        this->inputString = std::move(inputString);
        i = 0;
        depth = 0;
    }

    void Program();

    void Lista_Naredbi();

    void Naredba();

    void Naredba_Pridruzivanja();

    void Za_Petlja();

    void E();

    void E_Lista();

    void T();

    void T_Lista();

    void P();

    void generateError();

    vector<string> getOutput() const { return output; }
};

void SintaksniAnalizator::Program() {
    output.push_back(string( depth, ' ' ) + "<program>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size()) {
        if (inputString[i] == "IDN" || inputString[i] == "KR_ZA") {
            Lista_Naredbi();
            depth = curDepth;
        } else generateError();
    } else {
        output.push_back(string( depth, ' ' ) + "$");
    }
}

void SintaksniAnalizator::Lista_Naredbi() {
    output.push_back(string( depth, ' ' ) + "<lista_naredbi>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size()) {
        if ((inputString[i] == "IDN" || inputString[i] == "KR_ZA")) {
            Naredba();
            depth = curDepth;
            Lista_Naredbi();
            depth = curDepth;
        } else if (inputString[i] == "KR_AZ") {
            output.push_back(string( depth, ' ' ) + "$");
        } else generateError();
    } else {
        output.push_back(string( depth, ' ' ) + "$");
    }
}

void SintaksniAnalizator::Naredba() {
    output.push_back(string( depth, ' ' ) + "<naredba>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size()) {
        if (inputString[i] == "IDN") {
            Naredba_Pridruzivanja();
            depth = curDepth;
        } else if (inputString[i] == "KR_ZA") {
            Za_Petlja();
            depth = curDepth;
        } else generateError();
    } else generateError();
}

void SintaksniAnalizator::Naredba_Pridruzivanja() {
    output.push_back(string( depth, ' ' ) + "<naredba_pridruzivanja>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size() && inputString[i] == "IDN") {
        output.push_back(string( depth, ' ' ) + input[i++]);
        if (i < inputString.size() && inputString[i] == "OP_PRIDRUZI") {
            output.push_back(string( depth, ' ' ) + input[i++]);
            E();
            depth = curDepth;
        } else generateError();
    } else generateError();
}

void SintaksniAnalizator::Za_Petlja() {
    output.push_back(string( depth, ' ' ) + "<za_petlja>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size() && inputString[i] == "KR_ZA") {
        output.push_back(string( depth, ' ' ) + input[i++]);
        if (i < inputString.size() && inputString[i] == "IDN") {
            output.push_back(string( depth, ' ' ) + input[i++]);
            if (i < inputString.size() && inputString[i] == "KR_OD") {
                output.push_back(string( depth, ' ' ) + input[i++]);
                E();
                depth = curDepth;
                if (i < inputString.size() && inputString[i] == "KR_DO") {
                    output.push_back(string( depth, ' ' ) + input[i++]);
                    E();
                    depth = curDepth;
                    Lista_Naredbi();
                    depth = curDepth;
                    if (i < inputString.size() && inputString[i] == "KR_AZ") {
                        output.push_back(string( depth, ' ' ) + input[i++]);
                        depth = curDepth;
                    } else generateError();
                } else generateError();
            } else generateError();
        } else generateError();
    } else generateError();
}

void SintaksniAnalizator::E() {
    output.push_back(string( depth, ' ' ) + "<E>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size() && (inputString[i] == "IDN" || inputString[i] == "BROJ" || inputString[i] == "OP_PLUS" ||
                                   inputString[i] == "OP_MINUS" || inputString[i] == "L_ZAGRADA")) {
        T();
        depth = curDepth;
        E_Lista();
        depth = curDepth;
    } else generateError();
}

void SintaksniAnalizator::E_Lista() {
    output.push_back(string( depth, ' ' ) + "<E_lista>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size()) {
        if (inputString[i] == "OP_PLUS" || inputString[i] == "OP_MINUS") {
            output.push_back(string( depth, ' ' ) + input[i++]);
            E();
            depth = curDepth;
        } else if (inputString[i] == "IDN" || inputString[i] == "KR_ZA" || inputString[i] == "KR_DO" ||
                   inputString[i] == "KR_AZ" || inputString[i] == "D_ZAGRADA") {
            output.push_back(string( depth, ' ' ) + "$");
        } else generateError();
    } else {
        output.push_back(string( depth, ' ' ) + "$");
    }
}

void SintaksniAnalizator::T() {
    output.push_back(string( depth, ' ' ) + "<T>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size() && (inputString[i] == "IDN" || inputString[i] == "BROJ" || inputString[i] == "OP_PLUS" ||
                                   inputString[i] == "OP_MINUS" || inputString[i] == "L_ZAGRADA")) {
        P();
        depth = curDepth;
        T_Lista();
        depth = curDepth;
    } else generateError();
}

void SintaksniAnalizator::T_Lista() {
    output.push_back(string( depth, ' ' ) + "<T_lista>");
    depth++;
    int curDepth = depth;
    if (i < input.size()) {
        if (inputString[i] == "OP_PUTA" || inputString[i] == "OP_DIJELI") {
            output.push_back(string( depth, ' ' ) + input[i++]);
            T();
            depth = curDepth;
        } else if (inputString[i] == "IDN" || inputString[i] == "KR_ZA" || inputString[i] == "KR_DO" ||
                   inputString[i] == "KR_AZ" || inputString[i] == "OP_PLUS" || inputString[i] == "OP_MINUS" ||
                   inputString[i] == "D_ZAGRADA") {
            output.push_back(string( depth, ' ' ) + "$");
        } else generateError();
    } else {
        output.push_back(string( depth, ' ' ) + "$");
    }
}

void SintaksniAnalizator::P() {
    output.push_back(string( depth, ' ' ) + "<P>");
    depth++;
    int curDepth = depth;
    if (i < inputString.size()) {
        if (inputString[i] == "OP_PLUS" || inputString[i] == "OP_MINUS") {
            output.push_back(string( depth, ' ' ) + input[i++]);
            P();
            depth = curDepth;
        } else if (inputString[i] == "L_ZAGRADA") {
            output.push_back(string( depth, ' ' ) + input[i++]);
            E();
            depth = curDepth;
            if (i < inputString.size() && inputString[i] == "D_ZAGRADA") {
                output.push_back(string( depth, ' ' ) + input[i++]);
            } else generateError();
        } else if (inputString[i] == "BROJ" || inputString[i] == "IDN") {
            output.push_back(string( depth, ' ' ) + input[i++]);
        } else generateError();
    } else generateError();
}

void SintaksniAnalizator::generateError() {
    cout << ((i < input.size()) ? "err " + input[i] + "\n" : "err kraj");
    exit(0);
}

int main() {
    vector<string> input, inputString;
    string inputLine;

    while (getline(cin, inputLine)) {
        if (inputLine == "q") break;
        if (inputLine.empty()) continue;
        input.push_back(inputLine);
        inputString.push_back(inputLine.substr(0, inputLine.find(' ')));
    }

    SintaksniAnalizator sa = SintaksniAnalizator(input, inputString);
    sa.Program();

    vector<string> output = sa.getOutput();
    for(const string& s : output) cout << s << "\n";

    return 0;
}
