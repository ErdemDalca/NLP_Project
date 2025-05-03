# WeaveNet Hacker

A 2D hacking simulation game built with Phaser 3, featuring a simulated OS experience with integrated terminal and browser functionalities.

## Project Overview

WeaveNet Hacker is a game that simulates the experience of navigating through computer networks, solving puzzles, and completing hacking challenges in a user-friendly graphical interface.

## Features

- Simulated OS interface with draggable windows
- Terminal emulator for command-line interactions
- Network visualization and navigation
- Browser-based puzzle solving
- Modern, minimalistic UI design

## Tech Stack

- **Game Engine**: Phaser 3
- **Build Tool**: Vite
- **Language**: JavaScript (ES6+)

## Project Structure

```
WeaveNetHacker_Dev/
├── src/                    # Source code
│   ├── scenes/            # Phaser game scenes
│   │   ├── Game.js       # Main game scene
│   │   └── Preloader.js  # Asset loading scene
│   ├── ui/               # UI components
│   │   └── WindowManager.js  # Window management system
│   └── main.js           # Entry point
├── public/               # Static assets
├── logs/                 # Logging directory
│   ├── important/        # Important logs (tracked)
│   └── errors/          # Error logs (tracked)
├── docs/                # Documentation
│   ├── GAME_CONCEPT.md  # Game design document
│   ├── TASKLIST.md      # Development roadmap
│   └── SESSION_SUMMARY_2025-03-30.md  # Development session notes
├── style.css           # Global styles
├── index.html          # Entry HTML file
└── vite.config.js      # Vite configuration
```

## Getting Started

1. **Prerequisites**
   - Node.js (v14 or higher)
   - npm or yarn

2. **Installation**
   ```bash
   # Clone the repository
   git clone https://github.com/chromewillow/WeaveNetHacker.git
   cd WeaveNetHacker

   # Install dependencies
   npm install
   ```

3. **Development**
   ```bash
   # Start development server
   npm run dev
   ```

4. **Building**
   ```bash
   # Create production build
   npm run build
   ```

## Development Guidelines

- Follow ESLint configuration for code style
- Write clear commit messages following conventional commits format
- Document new features and API changes
- Test thoroughly before committing

## Error Logging

Error logs are stored in the `logs/` directory (not tracked by git). The logging system captures:
- Runtime errors
- Performance metrics
- Debug information

## Security

- Environment variables should be stored in `.env` files (not tracked by git)
- API keys and credentials should never be committed
- Use secure protocols for network communications
- Regular security audits are recommended

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
