/*
Write a JavaScript script that adds a li element to a list when the user clicks on the element
with id add_item:
The new element must be: <li>Item</li>
The new element must be added to the ul element with class my_list
*/

const add_item = document.querySelector("#add_item")

add_item.addEventListener("click", () => {
  const new_li = document.createElement("li");
  new_li.textContent = "Item";
  document.querySelector(".my_list").appendChild(new_li);
});