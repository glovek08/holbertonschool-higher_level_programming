/*
Write a JavaScript script that adds the class red to the header
 element when the user clicks on the tag with id red_header
*/

const header = document.querySelector("header");
const red_header_el = document.querySelector("#red_header");

red_header_el.addEventListener("click", () => header.classList.add("red"));