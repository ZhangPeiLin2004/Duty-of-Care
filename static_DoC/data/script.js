
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
        title: "SiliconGuard Innovations: Biological Breakthroughs in Semiconductor PFAS Remediation",
        image: "../static_DoC/images_DoC/stories_images/story8img.jpg",
        description: "SiliconGuard Innovations showcases a groundbreaking biological treatment approach for PFAS within the semiconductor industry. This pioneering effort demonstrates the potential for sustainable, environmentally friendly methods to address complex industrial PFAS challenges.",
        link: "/effective-efforts.html"
    },
    {
        title: "CoatClean Technologies: Eliminating PFAS from Paint Manufacturing Wastewater",
        image: "../static_DoC/images_DoC/stories_images/story6img.jpg",
        description: "A leading paint and coating manufacturer, in partnership with a specialized technology provider, has successfully deployed an innovative PFAS destruction solution. This collaboration showcases how advanced treatment can eliminate PFAS from industrial effluents, setting a new standard for environmental stewardship in the sector.",
        link: "/effective-efforts.html"
    },
    {
        title: "EcoPlate Solutions: A New Standard in Responsible Plating",
        image: "../static_DoC/images_DoC/stories_images/story2img.jpg",
        description: "EcoPlate Solutions leads the charge in sustainable electroplating by implementing a revolutionary PFAS destruction technology. This initiative showcases their commitment to environmental responsibility, demonstrating how advanced destruction methods can eliminate persistent PFAS compounds from industrial wastewater and sludge.",
        link: "/effective-efforts.html"
    },
    {
        title: "ChemGuard Systems: Pioneering Biological Solutions for PFAS in Manufacturing",
        image: "../static_DoC/images_DoC/stories_images/story4img.jpg",
        description: "ChemGuard Systems is at the forefront of chemical manufacturing innovation, deploying advanced biological treatment processes to address PFAS contamination. Their work demonstrates the viability of biological degradation as a sustainable and effective solution for complex industrial wastewaters containing PFAS.",
        link: "/effective-efforts.html"
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
