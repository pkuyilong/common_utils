#include <iostream>


class Monster {
public:
    Monster(int hp): hp(hp){}
    virtual ~Monster() {}
public:
    int hp;
};

class Assassin: public Monster {
public:
    Assassin(int hp=500, int attack=2500): Monster(hp),  attack(attack) { 
        std::cout << "Assassin created, hp: " << this->hp << " attack " 
                << this->attack << std::endl;
    }

    ~Assassin() {}

public:
    int attack;
};

class Undead: public Monster {
public:
    Undead(int hp, int magic): magic(magic), Monster(hp) {
        std::cout << "wangling created hp " << this->hp  << " magic: " 
                << this->magic << std::endl;
    }
private:
    int magic;
};

class MonsterFactory {
public:
    MonsterFactory() {}

    ~MonsterFactory() {}

    Monster* create (std::string mon_type) {
        if (mon_type == "udd") {
            ptr = new Undead(1230, 1000);
        }
        else if (mon_type == "ass") {
            ptr = new Assassin();
        }
        return ptr;
    }
public:
    Monster* ptr;
};


int main() {
    MonsterFactory mf;
    Monster* p = mf.create("udd");
    Monster* p2 = mf.create("ass");
    // Monster*p = new Undead(3000, 999);
}
