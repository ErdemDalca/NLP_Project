# Game Design Document: Realistic World Generation System

## 1. Introduction

### 1.1 Purpose
This document outlines the requirements and design for a procedural world generation system capable of creating realistic planetary environments. The system will generate detailed, scientifically plausible worlds based on a set of input parameters and a seed value, producing consistent and varied results suitable for a 2D game where a ship crash-lands on an unknown planet.

### 1.2 Scope
The world generation system will:
- Create realistic planetary terrain based on geological principles
- Simulate tectonic plate movement and interactions
- Generate appropriate water features including oceans, lakes, and rivers
- Model atmospheric circulation and weather patterns
- Produce biomes based on environmental factors
- Provide a consistent world that can be explored in a 2D game environment

### 1.3 Game Experience
The game will have two distinct phases:

1. **World Generation Phase**:
   - Standalone UI and renderer separate from the main game
   - Planet viewed from space (satellite view)
   - Limited detail but shows global features
   - User can adjust parameters and regenerate until satisfied

2. **Gameplay Phase**:
   - Uses existing layer and tile system
   - Detailed local view for colony management
   - Loads data from the generated world

## 2. Input Parameters

### 2.1 Star Properties
| Parameter | Description | Range | Effect on World |
|-----------|-------------|-------|----------------|
| Mass | Mass of the star being orbited | 0.1 - 50 solar masses | Affects habitable zone, radiation levels, and day/night cycle |
| Radius | Physical size of the star | 0.1 - 1000 solar radii | Influences apparent size in sky and radiation received |
| Temperature | Surface temperature of the star | 2000K - 50000K | Determines light spectrum and energy received |
| Age | Age of the star | 1 million - 10 billion years | Affects stability and radiation patterns |

### 2.2 Planet Properties
| Parameter | Description | Range | Effect on World |
|-----------|-------------|-------|----------------|
| Orbital Parameters | Defines the planet's orbit around its star | See below | Determines temperature, day length, and seasonal variations |
| Radius | Size of the planet | 0.1 - 10 Earth radii | Affects gravity, atmospheric retention, and surface area |
| Mass | Mass of the planet | 0.1 - 10 Earth masses | Influences gravity, atmospheric density, and geological activity |
| Rotation Rate | How quickly the planet rotates | 0.1 - 100 Earth days per rotation | Affects day/night cycle, weather patterns, and Coriolis effect |
| Number of Plates | Number of tectonic plates | 2 - 30 plates | Determines mountain ranges, volcanic activity, and continental shapes |
| Water Amount | Percentage of surface covered by water | 0 - 100% | Influences ocean size, humidity, and climate patterns |
| Atmosphere Strength | Density and composition of atmosphere | 0.1 - 10 Earth atmospheres | Affects temperature regulation, weather intensity, and erosion rates |
| Planet Age | Age of the planet | 10 million - 10 billion years | Determines erosion levels, geological maturity, and biome development |

#### 2.2.1 Orbital Parameters
| Parameter | Description | Range | Effect on World |
|-----------|-------------|-------|----------------|
| Semi-major axis (a) | Half the longest diameter of the orbital ellipse | 0.1 - 100 AU | Determines average distance from star and orbital period |
| Eccentricity (e) | How much the orbit deviates from a perfect circle | 0 - 0.95 | Affects seasonal variations and temperature extremes |
| Periapsis | Closest approach to the star | Calculated from a and e | Creates temperature maximums and affects tidal forces |
| Apoapsis | Farthest distance from the star | Calculated from a and e | Creates temperature minimums and affects habitability |
| Orbital Period | Time to complete one orbit | Calculated using Kepler's third law | Determines year length and seasonal cycle duration |

The orbital period (T) is calculated using Kepler's third law: T² = (4π²/GM) × a³, where G is the gravitational constant, M is the star's mass, and a is the semi-major axis.

Periapsis distance = a(1-e) and Apoapsis distance = a(1+e)

### 2.3 Generator Properties
| Parameter | Description | Range | Effect on Generation |
|-----------|-------------|-------|---------------------|
| Resolution | Resolution of terrain sectors | 100 - 10,000,000 tiles | Determines detail level and computational requirements |
| Seed | Random seed for generation | 32 or 64-bit integer | Ensures reproducibility while allowing variation |

## 3. Generation Phases

### 3.1 Tectonic Plate Generation
The system will divide the planetary sphere into a specified number of tectonic plates using a modified Voronoi diagram approach.

#### 3.1.1 Requirements
- Generate the specified number of plates with realistic shapes
- Ensure plates cover the entire planetary surface
- Assign each plate appropriate properties (continental or oceanic)
- Store plate boundaries for later processing

#### 3.1.2 Algorithm Overview
1. Generate initial seed points on the sphere using a [Poisson disk sampling algorithm](https://www.jasondavies.com/poisson-disc/) - a technique that creates randomly distributed points that maintain a minimum distance from each other, resulting in a natural-looking pattern
2. Create Voronoi cells from these points using a spherical Voronoi diagram - a mathematical method that divides space into regions based on distance to points
3. Apply noise and distortion to create more natural plate boundaries
4. Classify each plate as continental or oceanic based on distribution parameters

### 3.2 Plate Movement Simulation
The system will simulate the movement of tectonic plates based on geological principles observed on Earth.

#### 3.2.1 Requirements
- Assign realistic movement vectors to each plate
- Ensure the sum of all movement vectors maintains conservation of momentum
- Model rotational components as well as translational movement
- Create a time-based simulation to show plate positions over geological time

#### 3.2.2 Algorithm Overview
1. Generate a mantle convection model to drive plate movement
2. Assign each plate a movement vector (direction and speed)
3. Include rotational components for larger plates
4. Simulate plate movement over time to reach the current geological epoch

### 3.3 Boundary Interaction Analysis
The system will analyze how plates interact at their boundaries to determine geological features.

#### 3.3.1 Requirements
- Identify three types of plate boundaries:
  - Convergent (collision) boundaries
  - Divergent (spreading) boundaries
  - Transform (sliding) boundaries
- Calculate relative movement vectors at each boundary segment
- Store boundary type information for terrain generation

#### 3.3.2 Algorithm Overview
1. For each boundary segment between plates:
   - Calculate relative movement vector between plates
   - Determine boundary type based on angle and magnitude of relative movement
   - Classify as convergent, divergent, or transform
2. For convergent boundaries, determine subduction direction based on plate types
3. Store boundary information in a data structure for terrain generation

### 3.4 Terrain Height Generation
The system will divide the world into tiles and generate height values based on plate information.

#### 3.4.1 Requirements
- Divide the sphere into the specified number of tiles
- Generate base height values for each tile
- Modify heights based on plate boundaries and types
- Create realistic mountain ranges at convergent boundaries
- Form oceanic ridges at divergent boundaries
- Generate appropriate terrain at transform boundaries

#### 3.4.2 Algorithm Overview
1. Create a grid of tiles covering the planetary sphere (hexagonal or square)
2. Assign each tile to a tectonic plate
3. Generate base height using Perlin noise modified by plate type
4. For tiles near plate boundaries:
   - Increase height at convergent boundaries (creating mountains)
   - Create ridges at divergent boundaries
   - Create fault lines at transform boundaries
5. Apply additional noise functions to create natural variation

### 3.5 Atmospheric Circulation
The system will simulate atmospheric circulation patterns based on planetary properties.

#### 3.5.1 Requirements
- Model global wind patterns based on:
  - Planetary rotation rate ([Coriolis effect](https://www.noaa.gov/jetstream/global/global-atmospheric-circulations)) - the deflection of air due to the planet's rotation
  - Temperature gradients from equator to poles
  - Topographical features (mountains, valleys)
- Create Hadley, Ferrel, and Polar cells based on planet parameters
- Generate prevailing wind directions for each latitude band
- Account for seasonal variations if applicable

#### 3.5.2 Algorithm Overview
1. Calculate temperature gradients based on latitude and star properties
2. Model air pressure systems based on temperature and rotation
3. Generate circulation cells (Hadley, Ferrel, Polar) scaled to planet size and rotation
4. Calculate prevailing wind directions for each latitude
5. Modify wind patterns based on topographical features
6. Store wind data for precipitation modeling

### 3.6 Precipitation and River Formation
The system will simulate rainfall patterns and river formation based on atmospheric circulation and terrain.

#### 3.6.1 Requirements
- Calculate precipitation levels based on:
  - Wind patterns and moisture content
  - Terrain features (rain shadows, mountain effects)
  - Distance from water bodies
- Simulate water flow across terrain to form rivers
- Model erosion effects on terrain from water flow

#### 3.6.2 Algorithm Overview
1. Calculate moisture pickup from oceans based on wind patterns
2. Simulate moisture transport across the planet
3. Calculate precipitation based on moisture content and terrain
4. Apply erosion to terrain based on rainfall intensity
5. Simulate water flow from high to low elevation
6. Form rivers along flow paths exceeding threshold values
7. Create lakes where water flow reaches depressions
8. Adjust terrain based on erosion patterns

### 3.7 Ocean and Sea Formation
The system will add water to the simulation to create oceans and seas.

#### 3.7.1 Requirements
- Fill the lowest areas of the terrain with water based on the water amount parameter
- Calculate and store water depth for each underwater tile
- Define coastlines where land meets water
- Store water body information for later use

#### 3.7.2 Algorithm Overview
1. Sort tiles by height
2. Fill tiles from lowest to highest until the specified water percentage is reached
3. Calculate water depth for each underwater tile
4. Identify and classify major water bodies (oceans, seas)
5. Define and smooth coastlines

### 3.8 Biome Generation
The system will assign biomes to each tile based on environmental factors.

#### 3.8.1 Requirements
- Determine biome types based on:
  - Temperature (influenced by latitude, altitude, and star properties)
  - Precipitation levels
  - Soil types (derived from underlying geology)
  - Elevation and slope
- Create realistic transitions between biomes
- Ensure biome distribution follows scientific principles

#### 3.8.2 Algorithm Overview
1. Calculate temperature maps based on latitude, altitude, and star properties
2. Combine temperature and precipitation data to create climate zones
3. Determine soil fertility based on geological history and erosion
4. Assign primary biome types based on climate and soil data
5. Apply noise and variation to create natural biome boundaries
6. Generate sub-biomes and transitional zones

### 3.9 Snow and Glacier Formation
The system will calculate snow and glacier formation based on climate conditions.

#### 3.9.1 Requirements
- Calculate snow potential based on:
  - Temperature (monthly averages and extremes)
  - Precipitation during cold months
  - Elevation and latitude
  - Solar exposure (slope and aspect)
- Determine snow persistence and glacier formation
- Visualize snow and ice features

#### 3.9.2 Algorithm Overview
1. Calculate snow accumulation vs. melt rates for each tile
2. Identify areas with persistent snow accumulation
3. Model glacier formation in areas with sufficient snow accumulation
4. Calculate glacier flow based on topography
5. Visualize seasonal snow, permanent snow fields, and glaciers

## 4. Terrestrial Biome Types

The system will classify terrestrial areas into the following detailed biome types:

### 4.1 Forest Biomes
1. **Tropical Rainforest**
   - High precipitation (>200 cm/year)
   - High temperature (>20°C annual average)
   - Low seasonal variation
   - High biodiversity

2. **Tropical Seasonal Forest**
   - Moderate to high precipitation (100-200 cm/year)
   - Distinct wet and dry seasons
   - High temperature (>20°C annual average)
   - Deciduous or semi-deciduous vegetation

3. **Temperate Deciduous Forest**
   - Moderate precipitation (75-150 cm/year)
   - Distinct seasons with cold winters and warm summers
   - Broad-leaved trees that shed leaves seasonally

4. **Temperate Rainforest**
   - High precipitation (>140 cm/year)
   - Mild temperatures with low seasonal variation
   - Dominated by coniferous trees
   - Often coastal with high humidity

5. **Boreal Forest (Taiga)**
   - Low to moderate precipitation (30-85 cm/year)
   - Long, cold winters and short, cool summers
   - Dominated by coniferous trees
   - High latitude (50°-70°N)

6. **Montane Forest**
   - Variable precipitation depending on elevation and aspect
   - Cooler temperatures due to elevation
   - Vegetation zones change with altitude
   - Often transitions to alpine meadows at higher elevations

### 4.2 Grassland Biomes
1. **Tropical Savanna**
   - Seasonal precipitation (50-130 cm/year)
   - Warm temperatures year-round (>20°C)
   - Mixture of grasses and scattered trees
   - Distinct wet and dry seasons

2. **Temperate Grassland (Prairie/Steppe)**
   - Moderate precipitation (25-75 cm/year)
   - Hot summers and cold winters
   - Dominated by grasses with few trees
   - Rich soil with deep root systems

3. **Alpine Grassland (Meadow)**
   - Variable precipitation
   - Cool temperatures due to high elevation
   - Short growing season
   - Located above tree line but below permanent snow

### 4.3 Desert and Xeric Biomes
1. **Hot Desert**
   - Very low precipitation (<25 cm/year)
   - High temperatures (>18°C annual average)
   - Extreme temperature variations between day and night
   - Sparse vegetation adapted to drought

2. **Cold Desert**
   - Very low precipitation (<25 cm/year)
   - Low temperatures (<18°C annual average)
   - Often found in rain shadows of mountains
   - Vegetation adapted to both cold and drought

3. **Semi-Desert (Semi-Arid)**
   - Low precipitation (25-50 cm/year)
   - Variable temperatures
   - More vegetation than true deserts
   - Often transitional zones between deserts and grasslands

4. **Xeric Shrubland**
   - Low precipitation (25-60 cm/year)
   - Dominated by drought-resistant shrubs
   - Often found in Mediterranean climates
   - Includes chaparral, matorral, and fynbos ecosystems

### 4.4 Tundra and Cold Biomes
1. **Arctic Tundra**
   - Low precipitation (15-25 cm/year)
   - Very cold temperatures (annual average <0°C)
   - Permafrost layer
   - No trees, dominated by mosses, lichens, and small shrubs

2. **Alpine Tundra**
   - Variable precipitation
   - Cold temperatures due to high elevation
   - No trees, similar vegetation to arctic tundra
   - Located above tree line on mountains

3. **Polar Desert**
   - Very low precipitation (<10 cm/year)
   - Extremely cold temperatures
   - Minimal vegetation
   - Found in polar regions

### 4.5 Wetland Biomes (Terrestrial)
1. **Temperate Wetland**
   - Saturated soils
   - Moderate temperatures
   - Dominated by water-tolerant vegetation
   - Includes marshes, swamps, and bogs

2. **Tropical Wetland**
   - Saturated soils
   - Warm temperatures
   - High biodiversity
   - Includes mangroves and tropical swamps

## 5. Output Data Structures

### 5.1 World Data
The final output will include:
- Complete planetary parameters
- Tectonic plate information
- Terrain height map
- Water body data
- Climate and weather patterns
- River and lake networks
- Biome distribution
- Snow and glacier data

### 5.2 Tile Data
Each tile will contain:
- Position (coordinates on the sphere)
- Elevation
- Water depth (if underwater)
- Moisture level
- Temperature range
- Biome type
- River presence and flow direction
- Parent tectonic plate
- Snow and ice information
- Additional metadata for game mechanics

## 6. User Interface

### 6.1 World Generation UI
The standalone world generation UI will include:
- Parameter adjustment controls
- 3D globe visualization
- Different visualization modes (terrain, temperature, precipitation, biomes, snow)
- Generation progress tracking
- Save/load functionality

### 6.2 Visualization Modes
The system will provide various visualization modes:
- Topographical view (elevation)
- Tectonic plate view
- Precipitation map
- Temperature map
- Biome view
- River and water body view
- Snow and glacier view

### 6.3 User Flow
1. User launches game and sees landing screen
2. User selects "Generate World" option
3. World generation UI appears with default parameters
4. User adjusts parameters if desired
5. User initiates generation process
6. Progress is displayed during generation
7. Generated world is displayed in space view
8. User can save/load worlds or regenerate with different parameters
9. When satisfied, user selects "Start Game"
10. World data is transferred to game system
11. Game begins with existing layer and tile system

## 7. Performance Considerations

### 7.1 Optimization Strategies
- Use multi-threading for independent calculations
- Implement spatial partitioning for regional calculations
- Cache intermediate results where appropriate
- Use level-of-detail approaches for visualization

### 7.2 Memory Management
- Store only essential data for each tile
- Use compression for stored data
- Implement streaming for large worlds
- Consider procedural generation of details on-demand

## 8. Extensibility

### 8.1 Future Enhancements
The system is designed to accommodate future additions:
- Seasonal variations
- Dynamic weather systems
- Geological events (earthquakes, volcanic eruptions)
- Flora and fauna distribution
- Resource generation
- Cave systems and underground features

### 8.2 Integration with Game Systems
The world generation system will provide hooks for:
- Colony building mechanics
- Resource gathering
- Navigation and pathfinding
- Environmental challenges
- Story and mission generation

## 9. Conclusion

This world generation system will create scientifically plausible, detailed, and varied planetary environments for the game. By simulating real geological, atmospheric, and hydrological processes, it will produce worlds that feel natural and consistent while offering diverse gameplay experiences. The two-phase approach allows users to create and customize their world before starting the game, enhancing player engagement and replayability.
