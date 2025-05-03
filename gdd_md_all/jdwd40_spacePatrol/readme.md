### Space Patrol Game Design Document

#### Game Overview:
"Space Patrol" is a turn-based strategy game where the player pilots a space ship around a 3x3 grid to fight pirate space ships, earn money, and upgrade their ship at Earth Starbase. Each sector in the grid represents a different location in space, with Earth Starbase in sector 1. The player navigates the grid, engages in battles with pirates, and uses earned money to buy better weapons and fuel.

#### Data Structures:

1. **Player:**
   - `name`: The name of the player.
   - `health`: Current health of the player's ship.
   - `max_health`: Maximum health of the player's ship.
   - `fuel`: Current fuel level.
   - `max_fuel`: Maximum fuel level.
   - `money`: Current money available.
   - `weapons`: List of weapons the player owns.
   - `current_sector`: The current sector the player is in.

2. **Weapon:**
   - `name`: The name of the weapon.
   - `damage`: The amount of damage the weapon can inflict.
   - `cost`: The cost of the weapon.

3. **Sector:**
   - `number`: The sector number (1 to 9).
   - `has_pirates`: Boolean indicating if there are pirates in the sector.
   - `is_starbase`: Boolean indicating if the sector is the Earth Starbase.

4. **Pirate:**
   - `health`: Current health of the pirate ship.
   - `max_health`: Maximum health of the pirate ship.
   - `weapons`: List of weapons the pirate owns.
   - `strategy`: Current strategy of the pirate (attack or defense pattern).

5. **Game:**
   - `sectors`: Array of sectors.
   - `player`: The player object.
   - `pirate`: The current pirate object the player is engaged with (if any).

#### Game Design Patterns:

1. **Game Loop:**
   - The game loop is the central component that runs the game. It handles player input, updates game state, and renders the game. The loop continues until the player wins, loses, or decides to quit.

2. **Model-View-Controller (MVC):**
   - **Model:** Manages the game data (Player, Weapon, Sector, Pirate).
   - **View:** Responsible for displaying the game state to the player (e.g., showing the grid, displaying battle results).
   - **Controller:** Handles player inputs and updates the game state accordingly (e.g., moving to a sector, engaging in battle).

3. **State:**
   - The game maintains different states (e.g., exploring, battling, at starbase). The behavior of the game changes based on the current state.

4. **Factory Method:**
   - Used to create instances of pirates, weapons, and sectors. This pattern helps in encapsulating the creation logic.

5. **Strategy:**
   - Implemented for battle strategies (attack patterns, defense patterns). Both player and AI can choose different strategies during a battle, and the game resolves the round based on these strategies.

6. **Observer:**
   - Used to notify the view of changes in the game state so that the UI can be updated accordingly.

### Detailed Data Structure Definitions:

```c
// Weapon structure
typedef struct {
    char name[20];
    int damage;
    int cost;
} Weapon;

// Player structure
typedef struct {
    char name[20];
    int health;
    int max_health;
    int fuel;
    int max_fuel;
    int money;
    Weapon weapons[5]; // Assuming the player can have up to 5 weapons
    int current_sector;
} Player;

// Sector structure
typedef struct {
    int number;
    int has_pirates;
    int is_starbase;
} Sector;

// Pirate structure
typedef struct {
    int health;
    int max_health;
    Weapon weapons[3]; // Assuming the pirate can have up to 3 weapons
    int strategy; // 0: Attack, 1: Defense
} Pirate;

// Game structure
typedef struct {
    Sector sectors[9];
    Player player;
    Pirate pirate;
} Game;
```

### Game Flow and Logic:

1. **Initialization:**
   - Initialize the player with default values (health, fuel, money, etc.).
   - Initialize the sectors, marking sector 1 as the Earth Starbase and randomly assigning pirates to other sectors.
   - Set up initial weapons available for purchase at Earth Starbase.

2. **Main Game Loop:**
   - Display the grid and current player status.
   - Accept player input for actions (move to a sector, scan for pirates, visit starbase).
   - Update game state based on player actions.
   - Check for pirate encounters and initiate battles if necessary.
   - Handle battles using the Strategy pattern (rock-paper-scissors logic).
   - Resolve battle outcomes and update player and pirate health.
   - Allow player to earn money and purchase upgrades at the starbase.
   - Continue until the player wins, loses, or quits.

3. **Battle System:**
   - Both player and pirate choose a strategy (attack or defense).
   - Resolve the round based on chosen strategies.
   - Calculate and apply damage.
   - Repeat until one side flees or is destroyed.

4. **Upgrading at Starbase:**
   - Allow player to purchase new weapons and refuel.
   - Update player attributes based on purchases.

### Example of the Game Loop:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_WEAPONS 5
#define MAX_SECTORS 9
#define MAX_PIRATE_WEAPONS 3

typedef struct {
    char name[20];
    int damage;
    int cost;
} Weapon;

typedef struct {
    char name[20];
    int health;
    int max_health;
    int fuel;
    int max_fuel;
    int money;
    Weapon weapons[MAX_WEAPONS];
    int current_sector;
} Player;

typedef struct {
    int number;
    int has_pirates;
    int is_starbase;
} Sector;

typedef struct {
    int health;
    int max_health;
    Weapon weapons[MAX_PIRATE_WEAPONS];
    int strategy; // 0: Attack, 1: Defense
} Pirate;

typedef struct {
    Sector sectors[MAX_SECTORS];
    Player player;
    Pirate pirate;
} Game;

// Function prototypes
void initialize_game(Game *game);
void display_grid(Game *game);
void move_player(Game *game);
void scan_for_pirates(Game *game);
void engage_battle(Game *game);
void visit_starbase(Game *game);
void purchase_weapons(Game *game);
void refuel_ship(Game *game);
void game_loop(Game *game);

int main() {
    Game game;
    initialize_game(&game);
    game_loop(&game);
    return 0;
}

// Initialize the game state
void initialize_game(Game *game) {
    // Initialize player
    strcpy(game->player.name, "Player");
    game->player.health = 100;
    game->player.max_health = 100;
    game->player.fuel = 100;
    game->player.max_fuel = 100;
    game->player.money = 500;
    game->player.current_sector = 1;

    // Initialize sectors
    for (int i = 0; i < MAX_SECTORS; i++) {
        game->sectors[i].number = i + 1;
        game->sectors[i].has_pirates = (i != 0) ? rand() % 2 : 0;
        game->sectors[i].is_starbase = (i == 0);
    }

    // Initialize player weapons (empty at start)
    for (int i = 0; i < MAX_WEAPONS; i++) {
        strcpy(game->player.weapons[i].name, "Empty");
        game->player.weapons[i].damage = 0;
        game->player.weapons[i].cost = 0;
    }

    // Initialize a default pirate
    game->pirate.health = 50;
    game->pirate.max_health = 50;
    for (int i = 0; i < MAX_PIRATE_WEAPONS; i++) {
        strcpy(game->pirate.weapons[i].name, "Laser");
        game->pirate.weapons[i].damage = 10;
        game->pirate.weapons[i].cost = 0;
    }
    game->pirate.strategy = 0;
}

// Display the grid
void display_grid(Game *game) {
    printf("Space Grid:\n");
    for (int i = 0; i < MAX_SECTORS; i++) {
        if (i == game->player.current_sector - 1) {
            printf("[P] ");
        } else if (game->sectors[i].is_starbase) {
            printf("[S] ");
        } else if (game->sectors[i].has_pirates) {
            printf("[*] ");
        } else {
            printf("[ ] ");
        }

        if ((i + 1) % 3 == 0) {
            printf("\n");
        }
    }
}

// Move the player to a new sector
void move_player(Game *game) {
    int sector;
    printf("Enter the sector number to move to (1-9): ");
    scanf("%d", &sector);
    if (sector < 1 || sector > 9) {
        printf("Invalid sector!\n");
        return;
    }
    if (sector == game->player.current_sector) {
        printf("You are already in this sector!\n");
        return;
    }

    int turns = abs

(sector - game->player.current_sector) * 3;
    if (game->player.fuel < turns) {
        printf("Not enough fuel to move!\n");
        return;
    }

    game->player.fuel -= turns;
    game->player.current_sector = sector;
    printf("Moved to sector %d. It took %d turns.\n", sector, turns);
}

// Scan for pirates in the current sector
void scan_for_pirates(Game *game) {
    Sector *current_sector = &game->sectors[game->player.current_sector - 1];
    if (current_sector->has_pirates) {
        printf("Pirates detected in sector %d!\n", current_sector->number);
        engage_battle(game);
    } else {
        printf("No pirates in this sector.\n");
    }
}

// Engage in a battle with pirates
void engage_battle(Game *game) {
    // Simplified battle logic (rock-paper-scissors)
    char *strategies[] = {"Attack", "Defense"};
    while (game->player.health > 0 && game->pirate.health > 0) {
        int player_choice, pirate_choice;
        printf("Choose your strategy (0: Attack, 1: Defense): ");
        scanf("%d", &player_choice);
        pirate_choice = rand() % 2;

        printf("You chose %s, Pirate chose %s.\n", strategies[player_choice], strategies[pirate_choice]);

        // Rock-paper-scissors logic
        if (player_choice == pirate_choice) {
            printf("It's a draw!\n");
        } else if ((player_choice == 0 && pirate_choice == 1) || (player_choice == 1 && pirate_choice == 0)) {
            printf("You win this round!\n");
            game->pirate.health -= 10; // Simplified damage calculation
        } else {
            printf("Pirate wins this round!\n");
            game->player.health -= 10; // Simplified damage calculation
        }

        printf("Player health: %d, Pirate health: %d\n", game->player.health, game->pirate.health);
    }

    if (game->player.health > 0) {
        printf("You defeated the pirates!\n");
        game->player.money += 100; // Earn money for defeating pirates
    } else {
        printf("You were defeated by the pirates!\n");
    }
}

// Visit Earth Starbase
void visit_starbase(Game *game) {
    int choice;
    printf("Welcome to Earth Starbase!\n");
    printf("1. Purchase Weapons\n");
    printf("2. Refuel Ship\n");
    printf("3. Leave Starbase\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            purchase_weapons(game);
            break;
        case 2:
            refuel_ship(game);
            break;
        case 3:
            printf("Leaving Earth Starbase.\n");
            break;
        default:
            printf("Invalid choice!\n");
            break;
    }
}

// Purchase weapons at the starbase
void purchase_weapons(Game *game) {
    Weapon available_weapons[] = {
        {"Laser", 10, 100},
        {"Plasma Cannon", 20, 200},
        {"Photon Torpedo", 30, 300}
    };

    int choice;
    printf("Available Weapons:\n");
    for (int i = 0; i < 3; i++) {
        printf("%d. %s (Damage: %d, Cost: %d)\n", i + 1, available_weapons[i].name, available_weapons[i].damage, available_weapons[i].cost);
    }
    printf("Enter the number of the weapon to purchase: ");
    scanf("%d", &choice);

    if (choice < 1 || choice > 3) {
        printf("Invalid choice!\n");
        return;
    }

    Weapon selected_weapon = available_weapons[choice - 1];
    if (game->player.money < selected_weapon.cost) {
        printf("Not enough money to purchase this weapon!\n");
        return;
    }

    for (int i = 0; i < MAX_WEAPONS; i++) {
        if (strcmp(game->player.weapons[i].name, "Empty") == 0) {
            game->player.weapons[i] = selected_weapon;
            game->player.money -= selected_weapon.cost;
            printf("Purchased %s for %d money.\n", selected_weapon.name, selected_weapon.cost);
            return;
        }
    }

    printf("No empty slots available to purchase this weapon!\n");
}

// Refuel the ship at the starbase
void refuel_ship(Game *game) {
    int fuel_needed = game->player.max_fuel - game->player.fuel;
    int cost = fuel_needed * 2; // Assume refuel cost is 2 money per unit of fuel

    if (game->player.money < cost) {
        printf("Not enough money to refuel the ship!\n");
        return;
    }

    game->player.fuel = game->player.max_fuel;
    game->player.money -= cost;
    printf("Refueled the ship for %d money.\n", cost);
}

// Main game loop
void game_loop(Game *game) {
    int choice;

    while (1) {
        display_grid(game);
        printf("Player status: Health = %d, Fuel = %d, Money = %d\n", game->player.health, game->player.fuel, game->player.money);
        printf("1. Move to a sector\n");
        printf("2. Scan for pirates\n");
        printf("3. Visit Earth Starbase\n");
        printf("4. Quit game\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                move_player(game);
                break;
            case 2:
                scan_for_pirates(game);
                break;
            case 3:
                visit_starbase(game);
                break;
            case 4:
                printf("Quitting game. Final status: Health = %d, Fuel = %d, Money = %d\n", game->player.health, game->player.fuel, game->player.money);
                return;
            default:
                printf("Invalid choice! Please try again.\n");
                break;
        }

        if (game->player.health <= 0) {
            printf("Game over! Your ship was destroyed.\n");
            return;
        }
    }
}
```

### Explanation:
1. **Initialization:**
   - `initialize_game`: Sets up the initial state of the game, including the player, sectors, and a default pirate.
2. **Display Grid:**
   - `display_grid`: Shows the current state of the 3x3 grid, indicating the player's position, Earth Starbase, and sectors with pirates.
3. **Player Movement:**
   - `move_player`: Moves the player to a selected sector, adjusting fuel accordingly.
4. **Scanning for Pirates:**
   - `scan_for_pirates`: Checks if the current sector has pirates and engages in battle if necessary.
5. **Battle System:**
   - `engage_battle`: Handles the battle logic using a simplified rock-paper-scissors mechanism.
6. **Starbase Interaction:**
   - `visit_starbase`: Allows the player to purchase weapons and refuel at Earth Starbase.
   - `purchase_weapons` and `refuel_ship`: Handle purchasing weapons and refueling the ship.
7. **Main Game Loop:**
   - `game_loop`: The main loop that runs the game, handling player input and updating the game state.

This design and implementation provide a structured approach to developing "Space Patrol" using key game design patterns. If you have further questions or need additional features, feel free to ask!