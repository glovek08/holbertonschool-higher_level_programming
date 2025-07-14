/*
Write a JavaScript script that toggles the class of the header 
element when the user clicks on the tag id toggle_header:

The header element must always have one class: red or green, 
never both in the same time and never empty. 
If the current class is red, when the user click on id toggle_header element,
the class must be updated to green ; and the reverse.
*/

const header = document.querySelector("header");
const toggleHeader = document.querySelector("#toggle_header");

if (!header.classList.contains("red") && !header.classList.contains("green")) {
  header.classList.add("green");
}


toggleHeader.addEventListener("click", () => {
  if (header.classList.contains("red")){
    header.classList.remove("red");
    header.classList.add("green");
    console.log("Green added");
  } else {
    header.classList.remove("green");
    header.classList.add("red");
    console.log("Red added");
  }
})
