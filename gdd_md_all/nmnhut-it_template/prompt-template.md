# Cocos2d-JS Game Development Prompt
## Project Setup
1. This project uses Cocos2d-JS as the game engine, located at
   `./libs/cocos-min.js`.
2. Before starting, run `npm install` to ensure all dependencies are installed.
3. The game resources and images are located in the `res` directory.
4. The game code files are located in the `src` directory.
5. Do not look into `node_modules`
6. Use the MCP tool to get image positioning information. Specify
   absolute paths when using this tool.
7. Existing JavaScript files in the project are only examples. Modify them to
   accommodate user's needs.

## Technical Requirements
1. Game canvas and background:
   - Set the window size in `project.json` to match the dimensions of
     `res/background.png`.
   - Ensure the canvas dimensions in the HTML file are consistent with this
     setting.
2. Code structure and quality:
   - Properly set up resources.
   - Implement the game logic in one or two well-organized JavaScript files.
   - Separate game logic from UI components for better maintainability and
     testability.
   - Follow coding best practices.
   - Add clear debug logs for every function and conditional branch to aid in troubleshooting.

## Testing Framework Implementation
1. Since Cocos2d-JS doesn't natively support testing, implement a simple test framework directly into your game code:
   - Create a `TestRunner` class in a separate file (e.g., `src/TestRunner.js`).
   - Design the framework to run tests in a non-blocking way that doesn't interfere with game execution.
   - Implement test functions like `assert()`, `assertEqual()`, `assertNotEqual()`, and `assertInRange()`.
   - Create a visual test report or console output format that clearly shows test results.

2. Test implementation requirements:
   - Each game component should have corresponding test functions.
   - Tests should be organized by component/feature.
   - Tests should verify both positive scenarios (expected behavior) and edge cases.
   - Test coverage should include:
     - Game initialization
     - Asset loading
     - Game mechanics
     - Physics (if applicable)
     - User input handling
     - State transitions
     - Score/progression tracking

3. Test execution:
   - Create a debug mode flag that can be toggled to run tests.
   - Tests should execute automatically when the game starts in debug mode.
   - All test results should be logged to the console with clear PASS/FAIL indicators.
   - Failed tests should provide detailed information about expected vs. actual results.

4. Example test structure:
   ```javascript
   // TestRunner.js
   var TestRunner = {
     tests: [],
     passed: 0,
     failed: 0,
     
     registerTest: function(component, testName, testFn) {
       this.tests.push({component: component, name: testName, fn: testFn});
     },
     
     assert: function(condition, message) {
       if (!condition) {
         console.error("TEST FAILED: " + message);
         return false;
       }
       return true;
     },
     
     assertEqual: function(expected, actual, message) {
       return this.assert(expected === actual, 
         message + " - Expected: " + expected + ", Got: " + actual);
     },
     
     runAllTests: function() {
       console.log("=== RUNNING ALL TESTS ===");
       this.passed = 0;
       this.failed = 0;
       
       for (var i = 0; i < this.tests.length; i++) {
         var test = this.tests[i];
         console.log("Running test: [" + test.component + "] " + test.name);
         try {
           var result = test.fn();
           if (result) {
             console.log("✓ PASSED: [" + test.component + "] " + test.name);
             this.passed++;
           } else {
             console.log("✗ FAILED: [" + test.component + "] " + test.name);
             this.failed++;
           }
         } catch (e) {
           console.error("✗ ERROR: [" + test.component + "] " + test.name + " - " + e.message);
           this.failed++;
         }
       }
       
       console.log("=== TEST RESULTS ===");
       console.log("Total tests: " + this.tests.length);
       console.log("Passed: " + this.passed);
       console.log("Failed: " + this.failed);
     }
   };
   ```

5. Example test implementation:
   ```javascript
   // Game component code
   var Player = function() {
     this.x = 0;
     this.y = 0;
     this.speed = 5;
     
     this.move = function(direction) {
       switch(direction) {
         case "up": this.y -= this.speed; break;
         case "down": this.y += this.speed; break;
         case "left": this.x -= this.speed; break;
         case "right": this.x += this.speed; break;
       }
     };
   };
   
   // Test code
   TestRunner.registerTest("Player", "Player Movement", function() {
     var player = new Player();
     var initialX = player.x;
     var initialY = player.y;
     
     player.move("right");
     var rightOk = TestRunner.assertEqual(initialX + player.speed, player.x, 
       "Player should move right");
     
     player.move("down");
     var downOk = TestRunner.assertEqual(initialY + player.speed, player.y, 
       "Player should move down");
     
     return rightOk && downOk;
   });
   ```

6. Test automation:
   - Run `node get-console-log.js` to capture and analyze test output.
   - Implement a simple test report parser to extract test results from console logs.
   - Add a command to automatically run all tests and display results.

## Implementation Instructions
1. Review the game design document thoroughly before starting implementation.
2. Implement all features as specified in the game design.
3. Break down implementation into steps.
4. Write tests for each component as you implement them.
5. Follow good coding practices:
   - Use meaningful variable and function names
   - Add comments for complex logic
   - Organize code into logical sections or classes
   - Implement error handling where appropriate
6. After implementation is completed, run `node get-console-log.js` to view console logs for smoke testing and test results. You need to wait to get the log.  

## Deliverables
1. Complete implementation of the game according to the design specifications
2. Well-structured JavaScript code files with appropriate documentation
3. Comprehensive test coverage with detailed test cases.
4. Run the tests, analyze console log, detect bugs and try your best to fix the bugs.  