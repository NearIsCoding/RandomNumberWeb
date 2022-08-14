carousel = document.querySelector(".custom_carousel");

console.log(carousel);

carousel.addEventListener("scroll", function (event) {
  var element = event.target;
  console.log(element);
  console.log("scrolled");
});
