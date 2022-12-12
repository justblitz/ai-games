struct Player {
    name: String,
    hit_points: u32,
  }
  
  struct Monster {
    name: String,
    hit_points: u32,
  }
  
  fn attack_monster(player: &mut Player, monster: &mut Monster) {
    monster.hit_points -= player.hit_points;
  
    if monster.hit_points <= 0 {
      println!("{} has defeated the {}!", player.name, monster.name);
    } else {
      println!("{} has {} hit points remaining.", player.name, player.hit_points);
      println!("{} has {} hit points remaining.", monster.name, monster.hit_points);
    }
  }
  
  fn main() {
    let mut player = Player {
      name: "Hero".to_string(),
      hit_points: 100,
    };
  
    let mut monster = Monster {
      name: "Dragon".to_string(),
      hit_points: 150,
    };
  
    attack_monster(&mut player, &mut monster);
    attack_monster(&mut player, &mut monster);
    attack_monster(&mut player, &mut monster);
  }
  