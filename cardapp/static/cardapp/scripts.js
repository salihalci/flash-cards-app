
function showHide() {
    var x = document.getElementById("answerdiv");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }


  function nextQuestion() {
    var questionKey = document.getElementById("questionKey").textContent;
    alert(questionKey);
    questionKey = questionKey++
    document.getElementById("questionKey")=questionKey

  }