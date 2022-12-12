#include <iostream>

using namespace std;

// Define a player struct with name and hit points
struct Player {
  string name;
  int hitPoints;
};

// Define a monster struct with name and hit points
struct Monster {
  string name;
  int hitPoints;
};

// Define a function to attack the monster
void attackMonster(Player& player, Monster& monster) {
  // Reduce the monster's hit points by the player's attack strength
  monster.hitPoints -= player.hitPoints;

  // Check if the monster is dead
  if (monster.hitPoints <= 0) {
    cout << player.name << " has defeated the " << monster.name << "!" << endl;
  } else {
    cout << player.name << " has " << player.hitPoints << " hit points remaining." << endl;
    cout << monster.name << " has " << monster.hitPoints << " hit points remaining." << endl;
  }
}

int main() {
  // Create a player object
  Player player = { "Hero", 100 };

  // Create a monster object
  Monster monster = { "Dragon", 150 };

  // Attack the monster three times
  attackMonster(player, monster);
  attackMonster(player, monster);
  attackMonster(player, monster);

  return 0;
}
