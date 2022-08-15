/** Oportunidad de mejorar **/

const input = document.getElementById("quantity");
const form = document.getElementById("form");

form.addEventListener("submit", (e) => {
  if (input.value == "" || input.value == null) {
    input.className = "form-control is-invalid";
    e.preventDefault();
  }
  var numbers = /^[0-9]+$/;
  if (!input.value.match(numbers)) {
    input.className = "form-control is-invalid";
    e.preventDefault();
  }
});

