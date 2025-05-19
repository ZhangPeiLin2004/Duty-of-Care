window.addEventListener("scroll", function() {
    let scrollPos = window.scrollY; // Get vertical scroll position
    document.getElementById("ribbon").style.top = scrollPos + "px"; // Move ribbon down
});
