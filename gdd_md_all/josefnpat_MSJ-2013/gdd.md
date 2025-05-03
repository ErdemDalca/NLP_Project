
               +----------------+                    +-------------+       +-----------------+
               |                |  loads map         |             | uses  |                 |
               |   map (tmx)    |<------------------+|   server    |+----->| jelly-server    |
               |  BLARGET       |                    |             |       |                 |
               |                |                    |  SEPPI      |       |  SEPPI          |
               +----------------+                    +-------------+       +-----------------+
                           ^                                                         ^
                           |                                                         |
                           |            +---------------+  +----------------+        |
                           |            | buy building  |  | sell building  |        |
                           |loads map   |               |  |                |        + communication
                           |            +---------------+  +----------------+        |
                           |                        ^           ^                    |
                           |                        |           |                    |
                           |                        |           |                    |
                           |                        |           |                    v
                           +                        |           |         +------------------+
    +------------------------+                  +---+-----------+---+     |                  |
    |    Draw Map            |  updates ATL obj |GAME STATE         |     |                  |
    |(Advanced Tile Loader ) |<----------------+|-------------------|     | jelly-client     |
    |                     MVP|  with buildings  |Allow users to     |     |                  |
    +------------------------+  from server     |select a location, |     |  SEPPI           |
                                                |and then choose    |     +------------------+
                                                |what to build or if|            ^
                               +---------------+|there is already   |            | uses
                               |quit to menu    |something, confirm |      +-----+-------------+
                               |                |if they want to    |      |                   |
                               |                |sell it.        MVP|+-+-->|                   |
                               |                +-------------------+  |   |   Client API      |
                               |                           ^           |   |  SEPPI            |
                               |                           |           |   +-------------------+
                               v                           +           |   +-------------------+
     +------------+     +---------------+     +--------------------+   |   |   Fake Client API |
     |INTRO STATE |     |main menu state|     |connecting state    |   +-->|    SEPPI          |
     |------------|     |---------------|     |--------------------|       |  aka single player|
     |consider    |     |               |     |                    |       +-------------------+
     |using       |     |consider using |     |                    |
     |lovesplash  |+--->|lovemenu       |+--->|                    |
     |            |     |               |     |                    |        MVP .. Minimal
     |            |     |               |     |                    |               Viable product
     |            |     |               |     |                    |
     |            |     |               |     |                 MVP|
     +------------+     +---------------+     +--------------------+

