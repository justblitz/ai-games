public class Game {
  // Define a player class with name and hit points
  public class Player {
    public string Name { get; set; }
    public int HitPoints { get; set; }

    public Player(string name, int hitPoints) {
      Name = name;
      HitPoints = hitPoints;
    }
  }

  // Define a monster class with name and hit points
  public class Monster {
    public string Name { get; set; }
    public int HitPoints { get; set; }

    public Monster(string name, int hitPoints) {
      Name = name;
      HitPoints = hitPoints;
    }
  }

  // Define a function to attack the monster
  static void AttackMonster(Player player, Monster monster) {
    // Reduce the monster's hit points by the player's attack strength
    monster.HitPoints -= player.HitPoints;

    // Check if the monster is dead
    if (monster.HitPoints <= 0) {
      Console.WriteLine(player.Name + " has defeated the " + monster.Name + "!");
    } else {
      Console.WriteLine(player.Name + " has " + player.HitPoints + " hit points remaining.");
      Console.WriteLine(monster.Name + " has " + monster.HitPoints + " hit points remaining.");
    }
  }

  static void Main(string[] args) {
    // Create a player object
    Player player = new Player("Hero", 100);

    // Create a monster object
    Monster monster = new Monster("Dragon", 150);

    // Attack the monster three times
    AttackMonster(player, monster);
    AttackMonster(player, monster);
    AttackMonster(player, monster);
  }
}
