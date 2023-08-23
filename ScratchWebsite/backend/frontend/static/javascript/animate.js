document.addEventListener("DOMContentLoaded", function () {
    const list_item = document.querySelector(".list-item");
    list_item.classList.add("animate-fade-in");
    const title = document.querySelector(".offer");
    title.classList.add("animate-fade-in");
    const bttn = document.querySelector(".team");
    bttn.classList.add("animate-fade-in");
    const bttn2 = document.querySelector("button");
    bttn2.classList.add("animate-fade-in");
});

var images= [];
for (var i = 0; i < 36; i++) {
  images.push({
    title: "Image " + (i + 1),
    source: "https://picsum.photos/500/500?random&img=" + i
  });
}

var perPage = 8;
var page = 1;
var pages = Math.ceil(images.length / perPage)