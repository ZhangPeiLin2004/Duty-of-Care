### README of Duty of Care (DoC) Project


Modularity and better Maintenance for html web pages
root
│── templates_DoC
│   ├── index.html               (Home Page - contains main navigation bar)
│   ├── duty-of-care.html         (Page for "Duty of Care")
│   ├── toolbox.html              (Page for "Toolbox")
│   ├── relevant-stories.html     (Page for "Relevant Stories")
│   ├── about-us.html             (Page for "About Us")
│   ├── login.html                (Login Page)
│
├── static_DoC
│   ├── webstyle.css              (CSS for styling)
│   ├── scripts.js                (JavaScript file for interactivity)
│
├── images_DoC
│   ├── freshwater_glass.png      (Example image)
│   ├── other-images.png          (Other relevant images)

1. Navigation Bar (Common in All Pages)
Since the navigation bar is reused on every page, you can copy-paste the same <header> section into all HTML files.
Example Navigation Bar (Put in All HTML Files)
<header>
    <div class="logo">Your Logo Here</div>
    <nav>
        <a class="nav-item" href="index.html">Home</a>
        <a class="nav-item" href="duty-of-care.html">Duty of Care</a>
        <a class="nav-item" href="toolbox.html">Toolbox</a>
        <a class="nav-item" href="relevant-stories.html">Relevant Stories</a>
        <a class="nav-item" href="about-us.html">About Us</a>
        <a class="nav-item" href="login.html">Login</a>
    </nav>
    <div class="search-icon">🔍</div>
</header>


2. Individual Page Files
Each page will have its own HTML structure but reuse the navigation bar.
Example of index.html (Home Page)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Duty of Care</title>
    <link rel="stylesheet" href="static_DoC/webstyle.css">
</head>
<body>

    <!-- Include Navigation Bar -->
    <header>
        <div class="logo">Your Logo Here</div>
        <nav>
            <a class="nav-item" href="index.html">Home</a>
            <a class="nav-item" href="duty-of-care.html">Duty of Care</a>
            <a class="nav-item" href="toolbox.html">Toolbox</a>
            <a class="nav-item" href="relevant-stories.html">Relevant Stories</a>
            <a class="nav-item" href="about-us.html">About Us</a>
            <a class="nav-item" href="login.html">Login</a>
        </nav>
        <div class="search-icon">🔍</div>
    </header>

    <section class="image-section">
        <img src="images_DoC/freshwater_glass.png" alt="Glass of Water">
    </section>

</body>
</html>

Example of duty-of-care.html (Duty of Care Page)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duty of Care</title>
    <link rel="stylesheet" href="static_DoC/webstyle.css">
</head>
<body>

    <!-- Navigation Bar -->
    <header>
        <div class="logo">Your Logo Here</div>
        <nav>
            <a class="nav-item" href="index.html">Home</a>
            <a class="nav-item" href="duty-of-care.html">Duty of Care</a>
            <a class="nav-item" href="toolbox.html">Toolbox</a>
            <a class="nav-item" href="relevant-stories.html">Relevant Stories</a>
            <a class="nav-item" href="about-us.html">About Us</a>
            <a class="nav-item" href="login.html">Login</a>
        </nav>
        <div class="search-icon">🔍</div>
    </header>

    <section>
        <h1>Understanding Duty of Care</h1>
        <p>Duty of Care is an essential legal obligation to ensure safety and well-being.</p>
    </section>

</body>
</html>

(Repeat the same structure for toolbox.html, relevant-stories.html, etc.)
