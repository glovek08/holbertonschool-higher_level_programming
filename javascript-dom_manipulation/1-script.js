/*
Write a JavaScript script that updates the text color of the header
element to red (#FF0000) when the user clicks on the tag with id red_header:
*/

const RED = "#FF0000";
const red_header = document.querySelector("#red-reader");
const header = document.querySelector("header");

red_header.addEventListener('click', () => header.style.color = RED);

}
header.style.color = RED;
