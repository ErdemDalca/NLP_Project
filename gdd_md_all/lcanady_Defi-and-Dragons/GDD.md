## DeFi & Dragons: Game Design Document (GDD) - Implemented Features

**Version:** 0.2
**Date:** 2025-03-28

### 1. Introduction & Vision

*   **Title:** DeFi & Dragons
*   **Concept:** A blockchain-based RPG where player characters (NFTs) engage in quests and combat, with core gameplay mechanics driven by the player's real DeFi actions on associated protocols. Progress involves acquiring better NFT equipment, completing quests tied to combat or DeFi activity, and earning token rewards.
*   **Genre:** RPG, GameFi, Action-Triggered Combat.
*   **Platform:** Web Browser (implied by documentation examples).
*   **Target Chain:** EVM-compatible (likely L2/Sidechain due to gas optimization focus).
*   **Core Pillars:** NFT Characters & Equipment, DeFi Action-Driven Combat, Questing System, On-Chain Rewards.

### 2. Gameplay Mechanics

*   **Core Loop:**
    1.  **Mint/Acquire:** Obtain a Character NFT (`Character.sol`).
    2.  **Quest:** Accept quests (`Quest.sol`, `CombatQuest.sol`, `ProtocolQuest.sol`) which may involve defeating monsters or performing DeFi actions.
    3.  **DeFi Action / Combat:** Perform actions on integrated DeFi protocols (e.g., trading, providing liquidity). These actions are validated (`ActionCombatManager.sol`) and trigger combat "Moves" (`CombatActions.sol`) that deal damage to quest targets, influenced by character stats and equipment. Direct combat (e.g., Boss Fights in `CombatQuest.sol`) involves using abilities (`CombatAbilities.sol`) and calculating damage (`CombatDamageCalculator.sol`).
    4.  **Reward:** Complete quests or defeat monsters to earn token rewards (`GameToken`) and potentially Equipment NFTs (`ItemDrop.sol`).
    5.  **Farm/Stake:** Stake tokens in `ResourceFarm.sol` to earn resource tokens.
    6.  **Equip/Trade:** Equip better gear (`Equipment.sol`) obtained via drops or purchased on the `Marketplace.sol` to improve combat effectiveness.
    7.  **Repeat:** Take on harder quests and engage further with DeFi protocols.
*   **RPG Elements:**
    *   **Character:** ERC721 NFTs (`Character.sol`) with randomized base stats (Strength, Agility, Magic) determined at mint using `ProvableRandom.sol`. Characters have a Level and Alignment. Each character has an associated `CharacterWallet.sol` for managing items. *Note: Base stats appear fixed after minting in current contracts; $GOLD training mentioned in docs is not implemented.*
    *   **Combat System:** Primarily driven by off-chain DeFi actions triggering on-chain combat moves (`ActionCombatManager`, `CombatActions`). Damage scales with the DeFi `actionValue` and character/weapon stats (`CombatDamageCalculator`). A separate system (`CombatAbilities`) handles elemental damage, status effects, and combos, used within specific `CombatQuest` encounters (e.g., Boss Fights). Critical hits are possible (`ProvableRandom`). PvP is not implemented in reviewed contracts.
    *   **Quests:** Defined by `QuestTemplate` (`Quest.sol`) with objectives like Kills, Damage Dealt, Trades Made, Liquidity Provided, etc. Specific types exist: `CombatQuest` (Monster Hunts, Boss Fights), `ProtocolQuest` (requires interactions validated by approved protocols). Parties (`Party.sol`) can undertake quests.
    *   **Items/Gear:** Equipment (Weapons, Armor) are ERC1155 NFTs (`Equipment.sol`) with stat bonuses (Str, Agi, Mag) and stat affinity. Acquired via random drops (`ItemDrop.sol`). Equipping/unequipping managed via `CharacterWallet`. Basic NFT `Marketplace.sol` allows trading. *Note: Crafting mentioned in docs is not detailed in contracts.*
    *   **Progression:** Primarily through acquiring and equipping better NFT gear. Character leveling exists (`Character.sol`) but its direct impact beyond potential quest requirements isn't specified in contracts.
*   **DeFi Integration:**
    *   **Action-Driven Combat:** Specific DeFi actions (Trades, NFT Sales, Liquidity Adds, Staking - defined in `ActionCombatManager`) trigger combat moves and damage.
    *   **Protocol Quests:** Quests require a minimum number of interactions or volume on whitelisted external protocols (`ProtocolQuest.sol`).
    *   **Resource Farming:** Stake tokens (LP or governance) to passively earn resource tokens (`ResourceFarm.sol`).
    *   **Economy:** Uses `GameToken` (fungible token) for rewards/trading and NFTs (`Character`, `Equipment`) for core assets. `Marketplace.sol` facilitates NFT exchange.

### 3. Game World & Setting

*   *(Largely Undefined by Code)* Assumed High Fantasy setting based on naming conventions (Dragons, Strength, Magic, Quests). Visuals and specific lore are not detailed in the contracts.

### 4. Characters & Classes

*   **Player Characters:** ERC721 NFTs (`Character.sol`). Defined by stats (Str, Agi, Mag) and Alignment.
*   **Classes:** No explicit class system implemented in the reviewed core contracts. Character capabilities are primarily defined by stats and equipped gear. *(Docs mention classes as future plan)*.

### 5. Economy & Tokenomics

*   **Primary Token (`GameToken`):** Fungible token (likely ERC-20) used for quest rewards and marketplace transactions. Minted as rewards in `ProtocolQuest.sol`, `CombatQuest.sol`.
*   **Resource Tokens:** Fungible tokens earned via staking in `ResourceFarm.sol`. Utility likely intended for crafting (not implemented).
*   **Stake Token:** Token required for staking in `ResourceFarm.sol` (potentially LP token or Governance Token - not specified).
*   **NFTs:**
    *   `Character` (ERC721): The player avatar.
    *   `Equipment` (ERC1155): Weapons, Armor providing stats.
*   **Economic Flow:** Players complete Quests (Combat/DeFi) -> Earn `GameToken` + potential Equipment NFTs -> Use `GameToken` on Marketplace -> Stake tokens in `ResourceFarm` -> Earn Resource Tokens. Better gear improves combat triggered by DeFi actions, potentially leading to better quest rewards.
*   **Faucets:** Quest completion rewards (`Quest`, `CombatQuest`, `ProtocolQuest`), Monster drops (`ItemDrop`), Resource Farming (`ResourceFarm`).
*   **Sinks:** Marketplace transaction fees (implicit if implemented in frontend/integration layer, not explicit in `Marketplace.sol` viewed), potentially repairs/crafting (not implemented).

### 6. Technical Implementation

*   **Blockchain/Stack:** Solidity, OpenZeppelin Contracts. Assumed Foundry development environment. Gas optimization techniques (packed structs, custom errors) suggest deployment on L2/Sidechain is intended.
*   **Smart Contracts:**
    *   `Character.sol`: ERC721 for characters, stats, state.
    *   `Equipment.sol`: ERC1155 for gear, stats, bonuses.
    *   `CharacterWallet.sol`: Manages equipment per character.
    *   `Quest.sol`, `CombatQuest.sol`, `ProtocolQuest.sol`: Manage different quest types and progress.
    *   `ActionCombatManager.sol`, `CombatActions.sol`: Core DeFi-action-to-combat logic.
    *   `CombatDamageCalculator.sol`: Calculates damage based on stats/affinity.
    *   `CombatAbilities.sol`: Elemental/status effect system.
    *   `ItemDrop.sol`: Handles randomized NFT drops.
    *   `ProvableRandom.sol`: On-chain (pseudo?)randomness for stats, crits, drops.
    *   `ResourceFarm.sol`: Staking contract for resource generation.
    *   `Marketplace.sol`: Basic NFT trading.
    *   `Party.sol`: Party management.
    *   `CombatQuestValidator.sol`, `QuestFacade.sol`, `GameFacade.sol`: Appear to be supporting/validation contracts.
    *   *Security:* Uses `ReentrancyGuard`, `AccessControl`, `Ownable`. Requires Audits. Upgradeability likely via Proxies (not confirmed).
*   **Randomness:** `ProvableRandom.sol` is used, requires secure seed generation/management off-chain or via VRF if true provability is needed.
*   **Wallet Integration:** Standard EVM wallet support required (MetaMask, WalletConnect, etc.).
*   **Backend/Client:** Significant off-chain infrastructure implied:
    *   Game Client (Web - React/Vue/etc.) for UI, interacting with contracts.
    *   Backend server for managing non-critical game state, potentially relaying some actions.
    *   "Platform Validator" service to monitor DeFi actions and trigger `ActionCombatManager.sol`.

### 7. Art Style & Audio

*   *(TBD)

### 8. Monetization Strategy

*   **Implemented Potential:**
    *   NFT Sales.
    *   Marketplace Fees: A percentage fee could be added to `Marketplace.sol` trades.

### 9. Target Audience

*   Crypto-native Gamers (GameFi enthusiasts).
*   DeFi users interested in gamified applications of their activity.
*   RPG players interested in NFT ownership and novel mechanics.

### 10. Current Status & Future Development (Based on Code vs. Docs)

*   **Implemented:** Core NFT system (Character, Equipment), Action-Driven Combat triggered by DeFi, multiple Quest types (Combat, Protocol), basic Item Drops, basic Marketplace, Resource Farming via Staking, Party system.
*   **Future/Discrepancies:** Advanced crafting, $GOLD-based stat training, PvP, Guilds/DAOs, Land gameplay, DeFi-powered abilities, advanced social features are mentioned in documentation but not present in the reviewed core contracts.

