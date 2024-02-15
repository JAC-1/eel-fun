const nitCode = document.getElementById("nit-code");
const nitCodeForm = document.getElementById("nit-code-form");


nitCodeForm.addEventListener("submit", (e) => {
  e.preventDefault();
});

const bookForm = document.getElementById("book-form");

bookForm.addEventListener("submit", (e) => {
  e.preventDefault();
});

const populateFieldsWithDefaults = (data) =>  {
  document.getElementById("isbn").value = data.ISBN
  document.getElementById("title").value = data.Title
  document.getElementById("author").value = data.Author
  document.getElementById("level").value = data.Level
  document.getElementById("pages").value = data.Pages
  document.getElementById("about").value = data.About
}

nitCode.addEventListener("keydown", async (e) => {
  if (e.key === "Enter") {
    const bookData = await eel.find_book(nitCode.value)();
    console.log(bookData);
    populateFieldsWithDefaults(bookData)

  }
});
