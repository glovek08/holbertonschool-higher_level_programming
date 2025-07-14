/*
Write a JavaScript script that updates the text of the header element to New Header!!!
when the user clicks on the element with id update_header
*/

const header = document.querySelector("header");
const update_header = document.querySelector("#update_header");

update_header.addEventListener("click", () => header.innerText = "New Header!!!");