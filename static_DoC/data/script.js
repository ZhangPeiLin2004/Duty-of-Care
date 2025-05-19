
// ############################################################################################################
// Relevant Stories 
// ############################################################################################################

document.addEventListener("DOMContentLoaded", function () {
    const titles = document.querySelectorAll(".story-title");
    const previewBox = document.querySelector(".story-preview");
    const titleText = document.getElementById("story-title");
    const descText = document.getElementById("story-desc");

    titles.forEach(title => {
        title.addEventListener("mouseover", function () {
            previewBox.style.backgroundImage = `url(${this.dataset.img})`;
            titleText.textContent = this.dataset.title;
            descText.textContent = this.dataset.desc;
        });
    });
});
// Define the stories with titles, images, descriptions, and links
const stories = [
    {
        title: "Clean Water Initiative",
        image: "/Images/RT_clean-affordable-water_hero_shutterstock_1486636016-e1656539325171.jpg",
        description: "A global effort to provide access to clean water.",
        link: "https://example.com/clean-water"
    },
    {
        title: "Ocean Conservation",
        image: "/Images/ocean_conservation.jpg",
        description: "Efforts to protect marine life and ecosystems.",
        link: "https://example.com/ocean-conservation"
    },
    {
        title: "Renewable Energy Solutions",
        image: "/Images/renewable_energy.jpg",
        description: "Innovative approaches to sustainable energy.",
        link: "https://example.com/renewable-energy"
    },
    {
        title: "Community Sustainability Projects",
        image: "/Images/community_sustainability.jpg",
        description: "Local communities taking action for a better future.",
        link: "https://example.com/community-sustainability"
    }
];

// Select elements
const storyTitles = document.querySelectorAll(".story-title");
const storyPreview = document.querySelector(".story-preview");
const storyDescription = document.getElementById("story-description");
const storyLink = document.getElementById("story-link");

// Add hover effect to update the preview dynamically
storyTitles.forEach((title, index) => {
    title.addEventListener("mouseover", () => {
        storyPreview.style.backgroundImage = `url(${stories[index].image})`;
        storyDescription.textContent = stories[index].description;
        storyLink.href = stories[index].link;  // Update the link dynamically
    });
});

// Relevant Stories 
// ############################################################################################################
