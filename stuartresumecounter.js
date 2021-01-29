//Get the visitors element on the page

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    // Typical action to be performed when the document is ready:
    document.getElementById("visits").innerHTML = xhttp.responseText;
  }
};
xhttp.open(
  "GET",
  "https://6pwwcau6jh.execute-api.eu-west-2.amazonaws.com/Prod/counter",
  true
);
xhttp.send();
