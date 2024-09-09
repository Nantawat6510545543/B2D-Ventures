$(document).ready(() => {
    $('.slick-carousel').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        arrows: true
    });
});

function toggleDetails() { 
    var detailsSection = document.getElementById("details-section");
    var discussionSection = document.getElementById("discussion-section");

    detailsSection.style.display = "block";
    discussionSection.style.display = "none";
}

function toggleDiscussion() { 
    var detailsSection = document.getElementById("details-section");
    var discussionSection = document.getElementById("discussion-section");

    discussionSection.style.display = "block";
    detailsSection.style.display = "none";
} 
