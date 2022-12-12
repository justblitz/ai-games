// Define a player object with name, hit points, and attack strength
const player = {
    name: "Hero",
    hitPoints: 100,
    attackStrength: 10
  };
  
  // Define a monster object with name, hit points, and attack strength
  const monster = {
    name: "Dragon",
    hitPoints: 150,
    attackStrength: 15
  };
  
  // Define a function to attack the monster
  const attackMonster = () => {
    // Reduce the monster's hit points by the player's attack strength
    monster.hitPoints -= player.attackStrength;
  
    // Check if the monster is dead
    if (monster.hitPoints <= 0) {
      console.log(`The ${monster.name} has been defeated!`);
    } else {
      console.log(`The ${monster.name} has ${monster.hitPoints} hit points remaining.`);
    }
  };
  
  // Attack the monster three times
  attackMonster();
  attackMonster();
  attackMonster();
  