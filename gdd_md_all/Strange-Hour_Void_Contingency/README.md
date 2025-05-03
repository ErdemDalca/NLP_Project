# Void Contingency

A cooperative space survival game where you and your crew must navigate through the dangerous void, manage ship systems, and survive against all odds.

## Overview

Void Contingency is a top-down 2D space game that combines tactical combat, resource management, and crew coordination. Play solo or with up to 4 players as you explore procedurally generated sectors, upgrade your ship, and face increasingly dangerous challenges.

## Features

- **Cooperative Multiplayer**: Work together with up to 4 players
- **Unique Ship Classes**: Choose from various ship types with different capabilities
- **Dynamic System**: Ship-specific configurations and upgrade paths
- **Crew Roles**: Captain, Engineering, Weapons, and Operations positions
- **Procedural Generation**: Explore unique sectors with different challenges
- **Resource Management**: Balance power, repairs, and combat resources
- **Progressive Difficulty**: Face increasingly dangerous encounters

## Project Structure

```
void-contingency/
├── assets/                    # Game assets including sprites, sounds, and UI elements
│   ├── audio/                # Sound effects and music files
│   ├── data/                 # Game configuration and content data
│   └── graphics/             # Visual assets (sprites, textures, animations)
├── docs/                     # Project documentation
│   ├── phase_one/           # Phase one development documentation
│   ├── phase_two/           # Phase two development documentation
│   ├── action_plan.md       # Development roadmap and milestones
│   └── GDD.md              # Game Design Document
├── include/                  # Header files for the game engine and core systems
│   ├── core/                # Core engine systems and interfaces
│   ├── game/                # Game-specific systems and components
│   ├── graphics/            # Graphics and rendering systems
│   ├── input/               # Input handling and controls
│   ├── network/             # Networking and multiplayer systems
│   ├── physics/             # Physics engine and collision systems
│   ├── ui/                  # User interface components
│   └── utils/               # Utility functions and helpers
├── scripts/                  # Build scripts, tools, and utility scripts
├── src/                     # Source code for the game engine and game systems
│   ├── core/                # Core engine implementation
│   ├── game/                # Game systems implementation
│   ├── graphics/            # Graphics engine implementation
│   ├── input/               # Input system implementation
│   ├── network/             # Network system implementation
│   ├── physics/             # Physics system implementation
│   ├── ui/                  # UI system implementation
│   └── utils/               # Utility functions implementation
├── tests/                   # Unit tests and integration tests
│   ├── integration/         # Integration test suites
│   └── unit/               # Unit test suites
├── third_party/             # Third-party libraries and dependencies
└── .vscode/                 # VS Code configuration files
```

### Directory Details

- **assets/**: Contains all game resources including:

  - **audio/**: Sound effects, background music, and audio assets
  - **data/**: Game configuration files, level data, and content definitions
  - **graphics/**: Visual assets including sprites, textures, and animations

- **docs/**: Project documentation including:

  - **phase_one/**: Documentation specific to the first development phase
  - **phase_two/**: Documentation for the second development phase
    - **ship_system/**: Ship systems design and implementation details
    - **game_loop/**: Core game loop and mechanics documentation
    - **README.md**: Phase two overview and guidelines
  - **action_plan.md**: Development roadmap and milestone tracking
  - **GDD.md**: Comprehensive game design document

- **include/**: Header files for:

  - **core/**: Core engine systems and interfaces
  - **game/**: Game-specific systems and component interfaces
  - **graphics/**: Graphics and rendering system interfaces
  - **input/**: Input handling and control system interfaces
  - **network/**: Networking and multiplayer system interfaces
  - **physics/**: Physics engine and collision system interfaces
  - **ui/**: User interface component interfaces
  - **utils/**: Utility function interfaces

- **src/**: Main source code including:

  - **core/**: Core engine implementation
  - **game/**: Game systems implementation
  - **graphics/**: Graphics engine implementation
  - **input/**: Input system implementation
  - **network/**: Network system implementation
  - **physics/**: Physics system implementation
  - **ui/**: UI system implementation
  - **utils/**: Utility functions implementation

- **tests/**: Test suite containing:

  - **integration/**: Integration tests for system interactions
  - **unit/**: Unit tests for individual components

- **scripts/**: Various utility scripts for:

  - Build automation
  - Asset processing
  - Development tools
  - Deployment scripts

- **third_party/**: External dependencies:
  - Game engine libraries
  - Network libraries
  - Asset processing tools
  - Testing frameworks

## Development Status

Currently in early development. More details coming soon.

## Getting Started

[Installation and setup instructions will be added as development progresses]

## Building and Compilation

### Prerequisites

- CMake 3.15 or higher
- C++17 compatible compiler
- PowerShell (for using the automated build script on Windows)
- Xcode Command Line Tools (for macOS)

### Building the Project

#### Option 1: Automated Build (Recommended)

##### Windows

Run the PowerShell build script from the project root:

```powershell
.\scripts\build.ps1
```

If you encounter a PowerShell execution policy error, you can either:

1. Run the script with a bypass for this session:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\scripts\build.ps1
   ```

2. Or permanently allow signed scripts for your user account:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

##### Linux

Run the shell script from the project root:

```bash
chmod +x ./scripts/build.sh  # Make the script executable (first time only)
./scripts/build.sh
```

By default, the script will build in Debug mode. To specify a different build type:

```bash
./scripts/build.sh Release
```

Available build types:

- Debug (default)
- Release
- RelWithDebInfo
- MinSizeRel

The script will:

- Check for required prerequisites
- Create the build directory if needed
- Configure and build the project
- Optionally run tests
- Show the location of the compiled executable

##### macOS

First, ensure you have Xcode Command Line Tools installed:

```bash
xcode-select --install
```

Then run the shell script from the project root:

```bash
chmod +x ./scripts/build.sh  # Make the script executable (first time only)
./scripts/build.sh
```

By default, the script will build in Debug mode. To specify a different build type:

```bash
./scripts/build.sh Release
```

Available build types:

- Debug (default)
- Release
- RelWithDebInfo
- MinSizeRel

The script will:

- Check for required prerequisites
- Create the build directory if needed
- Configure and build the project
- Optionally run tests
- Show the location of the compiled executable

#### Option 2: Manual Build

If you prefer to build manually, follow these steps:

1. Create a build directory and navigate to it:

   ```bash
   mkdir build
   cd build
   ```

2. Configure the project with CMake:

   ```bash
   cmake ..
   ```

   For a specific build type (Debug, Release, RelWithDebInfo, MinSizeRel):

   ```bash
   cmake -DCMAKE_BUILD_TYPE=Release ..
   ```

3. Build the project:
   ```bash
   cmake --build .
   ```
   Or use your system's build tool directly:
   - Windows: `msbuild VoidContingency.sln`
   - Linux/macOS: `make`
   - macOS (with Xcode): `xcodebuild -project VoidContingency.xcodeproj`

The compiled executable will be located in the `build/bin` directory.

### Running Tests

After building, you can run the test suite:

```bash
cd build
ctest
```

## Running the Game

After successfully building the project, you can run the game using the following instructions:

### Windows

1. Navigate to the build directory:

   ```powershell
   cd build
   ```

2. Run the executable:

   ```powershell
   .\bin\VoidContingency.exe
   ```

   If you're using Visual Studio, you can also run the game directly from the IDE by:

   1. Opening the solution file (`VoidContingency.sln`) in Visual Studio
   2. Setting `VoidContingency` as the startup project
   3. Pressing F5 or clicking the "Start" button

### Linux

1. Navigate to the build directory:

   ```bash
   cd build
   ```

2. Run the executable:

   ```bash
   ./bin/VoidContingency
   ```

   If you encounter a permission error, you may need to make the executable file executable:

   ```bash
   chmod +x ./bin/VoidContingency
   ```

### macOS

1. Navigate to the build directory:

   ```bash
   cd build
   ```

2. Run the executable:

   ```bash
   ./bin/VoidContingency
   ```

   If you encounter a permission error, you may need to make the executable file executable:

   ```bash
   chmod +x ./bin/VoidContingency
   ```

### Command Line Arguments

The game supports the following command line arguments:

- `--debug`: Enable debug mode with additional logging
- `--fullscreen`: Start the game in fullscreen mode
- `--windowed`: Start the game in windowed mode
- `--resolution <width>x<height>`: Set a specific resolution (e.g., `--resolution 1920x1080`)

Example usage:

```bash
# Windows
.\bin\VoidContingency.exe --fullscreen --resolution 1920x1080

# Linux
./bin/VoidContingency --fullscreen --resolution 1920x1080

# macOS
./bin/VoidContingency --fullscreen --resolution 1920x1080
```

## Contributing

[Contribution guidelines will be added as development progresses]

## License

[License information will be added as development progresses]
