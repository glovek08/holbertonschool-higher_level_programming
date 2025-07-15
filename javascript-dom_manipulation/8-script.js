/*
Write a JavaScript script that fetches from
https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch
in the HTML element with id hello.
*/

const helloBtn = document.querySelector("#hello-btn");
const helloDiv = document.querySelector("#hello-div");


helloBtn.addEventListener("click", () => {
  getHello();
})

async function getHello () {
  const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    };

    const hello_json = await response.json();
    const helloMsg = hello_json["hello"];

    if (helloMsg !== undefined) {
      helloDiv.textContent = helloMsg;
      console.log(`Message: ${helloMsg}`);
    }
  } catch (fetch_error) {
    console.warn(fetch_error);
  }
}