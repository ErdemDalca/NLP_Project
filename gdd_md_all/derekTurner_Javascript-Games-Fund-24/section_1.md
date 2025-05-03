# Website

This website layout utilising Bootstrap 5 can be used as container for some biographical information, a game design summary and a list of element pages which show different aspects of BasbylonJS.

This is a revision aid featuring basic BabylonJS scenes which you can draw on.  Please adapt any code you use to fit your own purpose.

The website will feature on each of these pages and code will be commented upon in the Element sections.


<iframe 
    height="1100" 
    width="100%" 
    scrolling="no" 
    title="frame animaations" 
    src="Block_4/demo/public/index.html" 
    frameborder="no" 
    loading="lazy" 
    allowtransparency="true" 
    allowfullscreen="true">
</iframe>

This is based on a template page available on the JSGF site.

The index.html page includes a navigation bar and three columns of themed information.  Essentially this is a landing page to present some biographical detail about yourself.

Reformat the page to suit and add relevant text and detail.


  **index.html**
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>JSPF - Assessment Example</title>
        <!--External CSS file-->
        <link rel="stylesheet" href="CSS/main.css" />
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" />
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <div class="container-fluid p-5 bg-primary text-white text-center">
            <h1>JavaScript Games: Programming Fundamentals</h1>
            <p>Resit Demonstration</p>
        </div>

        <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="#"><img src="assets/images/JGF_badge.png" alt="JGPF" width="60" /></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="collapsibleNavbar">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="index.html">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="game.html">Game</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Elements</a>
                            <ul class="dropdown-menu">
                                <li>
                                    <a class="dropdown-item" href="element1.html">Element 1</a>
                                </li>
                                <li>
                                    <a class="dropdown-item" href="element2.html">Element 2</a>
                                </li>
                                <li>
                                    <a class="dropdown-item" href="element3.html">Element 3</a>
                                </li>
                                <li>
                                    <a class="dropdown-item" href="element4.html">Element 4</a>
                                </li>
                                <li>
                                    <a class="dropdown-item" href="element5.html">Element 5</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <div class="row">
                <div class="col-sm-4">
                    <h3>Home Page</h3>
                    <p>Home page presents your Name and details</p>
                    <p>Name, Banner number, Experience as a games programmer</p>
                </div>
                <div class="col-sm-4">
                    <h3>Game Page</h3>
                    <p>Present a summary of your game design document</p>
                    <p>Include some illustrations and easy to read content</p>
                </div>
                <div class="col-sm-4">
                    <h3>Elements</h3>
                    <p>A collection of 5 scenes</p>
                    <p>3D scene - 3D environment - player funcion - GUI & audio - multiple scenes</p>
                </div>
            </div>
        </div>

        <div style="width: 40%; height: 40%; align-items: center; margin-left: auto; margin-right: auto">
            <!-- Carousel -->
            <div id="demo" class="carousel slide" data-bs-ride="carousel">
                <!-- Indicators/dots -->
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#demo" data-bs-slide-to="0" class="active"></button>
                    <button type="button" data-bs-target="#demo" data-bs-slide-to="1"></button>
                    <button type="button" data-bs-target="#demo" data-bs-slide-to="2"></button>
                </div>

                <!-- The slideshow/carousel -->
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="assets/images/dice1.jpg" alt="Placeholder" class="d-block" style="width: 100%" />
                        <div class="carousel-caption">
                            <h3>Dice</h3>
                            <p>
                                Photo by
                                <a href="https://unsplash.com/@aakashdhage?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
                                    >Aakash Dhage</a
                                >
                                on
                                <a href="https://unsplash.com/s/photos/3d-game?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
                                    >Unsplash</a
                                >
                            </p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="assets/images/doublesix.jpg" alt="Placeholder" class="d-block" style="width: 100%" />
                        <div class="carousel-caption">
                            <h3>Double Six</h3>
                            <p>
                                Photo by
                                <a href="https://unsplash.com/@brett_jordan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
                                    >Brett Jordan</a
                                >
                                on
                                <a href="https://unsplash.com/s/photos/dice?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
                                    >Unsplash</a
                                >
                            </p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="assets/images/throw.jpg" alt="Placeholder" class="d-block" style="width: 100%" />
                        <div class="carousel-caption">
                            <h3>Placeholder Image</h3>
                            <p>
                                Photo by
                                <a href="https://unsplash.com/@stumpie10?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
                                    >Robert Stump</a
                                >
                                on
                                <a href="https://unsplash.com/s/photos/dice?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
                                    >Unsplash</a
                                >
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Left and right controls/icons -->
                <button class="carousel-control-prev" type="button" data-bs-target="#demo" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon"></span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#demo" data-bs-slide="next">
                    <span class="carousel-control-next-icon"></span>
                </button>
            </div>
        </div>
    </body>
</html>

```

This refers to a stylesheet, but this is not doing much here, most of the styling is coming from bootstrap at the moment.

**CSS/main.css

```css
body {
    overflow: hidden;
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
}


#renderCanvas {
    width:1000px; height:600px; display: block; margin-left: auto; margin-right: auto; margin-top: 50px;
    
}

#babylonjs {
    width: 600px;
    height: 300px;
}
```

A site might typically include a game page which links from the menu and might contain a summary Game Design Document or description of scenes,  there is just placeholder text and image here.  The page should be themed to a chosen colour scheme and style.

**game.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>JSPF - Assessment Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<div class="container-fluid p-5 bg-primary text-white text-center">
  <h1>JavaScript Games: Programming Fundamentals</h1>
  <p>Summary of GDD</p> 
</div>

<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Element 1</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="index.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="game.html">Game</a>
          </li>  
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Elements</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="element1.html">Element 1</a></li>
              <li><a class="dropdown-item" href="element2.html">Element 2</a></li>
              <li><a class="dropdown-item" href="element3.html">Element 3</a></li>
              <li><a class="dropdown-item" href="element4.html">Element 4</a></li>
              <li><a class="dropdown-item" href="element5.html">Element 5</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="container mt-5">
    <div class="row">
      <div class="col-sm-4">
        <h3>Game Concept</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
      </div>
      <div class="col-sm-4">
        <h3>Game Characters</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
      </div>
      <div class="col-sm-4">
        <h3>Game Environment</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
      </div>
    </div>
  </div>
  
  <div class="container mt-3" style="width:50%; height: 50%; align-items: center; margin-left: auto; margin-right: auto;">
    <div class="card" style="width:400px">
      <img class="card-img-top" src="assets/images/profile.jpg" alt="Card image" style="width:100%">
      <div class="card-body">
        <h4 class="card-title">Johnathan Dowe</h4>
        <p class="card-text">John Doe is an architect and engineer whose design concepts have been incorporated into the current game proposal</p>
        <!-- <a href="#" class="btn btn-primary">See Profile</a> -->
      </div>
    </div>

</body>
</html>

```

The overall structure of the site is in the public folder. The detail will be discussed in the next sections.

![structure](structure.png)

