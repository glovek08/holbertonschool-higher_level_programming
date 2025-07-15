/*
Write a JavaScript script that adds, removes and clears li elements
from a list when the user clicks:

    The new element must be: <li>Item</li>
    The new element must be added to the element with id my_list
    When the user clicks on the element with id add_item: a new element
      is added to the list
    When the user clicks on the element with id remove_item: the last
      element is removed from the list
    When the user clicks on the element with id clear_list: all elements
      of the list are removed.
*/

const listBtns = document.querySelectorAll(".list-btn");
const myList = document.querySelector(".my-list");

// Will be used to delete specific list items.
// Update on success or failure inside event listener.
// It's dirty af but f! it.
let myListLength = myList.children.length;

// console.log(listBtns);

listBtns.forEach(btn => {
  btn.addEventListener("click", (event) => {
    // console.log(event.target.id + 'pressed');
    switch (event.target.id) {
      case 'add-item-btn':
        if (!addListItem("Item")) {
          console.log("Couldn't create list item");
        } else {
          myListLength++;
        }
        break;
      case 'remove-item-btn':
        if (myListLength !== 0) {
          if (!removeListItem()) {
            console.log("Couldn't delete list item");
          } else {
            myListLength--;
            break;
          }
        } else {
          console.log("List is empty!");
        }
        break;
      case 'clear-list-btn':
        if (!clearList()) {
          console.log("Couldn't delete list");
        } else {
          console.log("myList cleared");
          myListLength = 0;
        }
        break;
    }
  })
});

const addListItem = (textContent = "n/a") => {
  try {
    new_item = document.createElement("li");
    new_item.textContent = textContent;
    myList.appendChild(new_item);
    console.log("New item added!");
    return true;
  } catch (creationError) {
    console.warn(creationError)
    return false;
  }
}

const removeListItem = (index = null) => {
  try {
    if (index === null) {
      myList.lastElementChild.remove()
    } else {
      const item = myList.children[index];
      if (item) {
        myList.removeChild(item);
      }
    }
    return true;
  } catch (removeError) {
    console.warn(removeError);
    return false;
  }
}

const clearList = () => {
  try {
    while (myList.firstChild) {
      myList.removeChild(myList.firstChild);
    }
    return true;
  } catch (clearError) {
    console.log(clearError);
    return false;
  }
}