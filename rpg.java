public class Game {
  // Define a player class with name and hit points
  static class Player {
    String name;
    int hitPoints;

    public Player(String name, int hitPoints) {
      this.name = name;
      this.hitPoints = hitPoints;
    }
  }

  // Define a monster class with name and hit points
  static class Monster {
    String name;
    int hitPoints;

    public Monster(String name, int hitPoints) {
      this.name = name;
      this.hitPoints = hitPoints;
    }
  }

  // Define a function to attack the monster
  static void attackMonster(Player player, Monster monster) {
    // Reduce the monster's hit points by the player's attack strength
    monster.hitPoints -= player.hitPoints;

    // Check if the monster is dead
    if (monster.hitPoints <= 0) {
      System.out.println(player.name + " has defeated the " + monster.name + "!");
    } else {
      System.out.println(player.name + " has " + player.hitPoints + " hit points remaining.");
      System.out.println(monster.name + " has " + monster.hitPoints + " hit points remaining.");
    }
  }

  public static void main(String[] args) {
    // Create a player object
    Player player = new Player("Hero", 100);

    // Create a monster object
    Monster monster = new Monster("Dragon", 150);

    // Attack the monster three times
    attackMonster(player, monster);
    attackMonster(player, monster);
    attackMonster(player, monster);
  }
}
