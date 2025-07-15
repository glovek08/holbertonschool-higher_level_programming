/*

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

    You should use this API service: https://hellosalut.stefanbohacek.dev/
    The language code will be the value selected in the select box with id language_code (es, fr, en etc.)
    The translation must be fetched when the user clicks on element with id btn_translate
    The translation of “Hello” must be displayed in the HTML tag with id hello
    You script must work when imported from the <head> tag

    Disclaimer: I've changed the element's id to be more conscise and
    use proper kebab-case.

*/

const langSelectBox = document.querySelector("#lang-select");
const translateBtn = document.querySelector("#translate-btn");
const helloEl = document.querySelector("#hello-div");

translateBtn.onclick = () => {
  // console.log(langSelectBox.value);
  switch (langSelectBox.value) {
    case "en":
      fetchGreeting("en");
      break;
    case "es":
      fetchGreeting("es");
      break;
    case "fr":
      fetchGreeting("fr");
      break;
    default:
      console.log("Invalid language prefix");
  }
}

async function fetchGreeting (langPrefix = "") {
  const url = `https://hellosalut.stefanbohacek.dev${langPrefix ? '?lang=' + langPrefix : ''}`;
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const helloJson = await response.json();
    const helloMsg = helloJson["hello"];
    if (helloMsg !== undefined) {
      console.log(`JSON: ${JSON.stringify(helloJson)}`);
      // console.log(`MSG: ${helloMsg}`)
      helloEl.textContent = helloMsg;
      return true;
    }
  } catch (fetchError) {
    console.warn(`Error: ${fetchError}`);
  }
  return false;
};