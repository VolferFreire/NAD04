console.log("hello from detail.js");

const backBtn = document.getElementById("back-btn");
backBtn.addEventListener("click", () => {
  history.back();
});
