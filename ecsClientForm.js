//ecs client form javascript

const form = document.querySelector("form");
form.addEventListener("submit", e => {
    e.preventDefault();
    const url = document.querySelector('input[name="url"]').value;
    const formData = new FormData();
    formData.append("csv_file", document.querySelector('input[name="csv_file"]').files[0]);
    formData.append("url", url);
    fetch("/extract-classify", {
        method: "POST",
        body: formData
    }).then(response => {
        if (!response.ok) {
            throw new Error(response.statusText);
        }
        return response.json();
    }).then(data => {
        // Handle the successful response here
        // update the UI
        let table = document.getElementById("outputTable");
        let tbody = table.getElementsByTagName("tbody")[0];
        tbody.innerHTML = "";
        // data[0] = sorted_keywords
        // data[1] = sorted_keyphrases
        .then(data => {
    // Handle the response data here
    var keywords = data.keywords;
    var keyphrases = data.keyphrases;
    var classifications = data.classifications;
    // create a table element for classifications
    var table3 = document.createElement("table");
    // add the table to the body
    document.body.appendChild(table3);

    // create a table row for the header
    var header3 = table3.createTHead();
    var row3 = header3.insertRow();

    // create the header cells
    var cell13 = row3.insertCell();
    var cell23 = row3.insertCell();

    // add the header text
        cell13.innerHTML = "Classification";
    cell23.innerHTML = "Confidence";

    //create a table body
    var tbody3 = document.createElement("tbody");
    table3.appendChild(tbody3);

    //iterate through the classifications
    for (var key in classifications) {
        // create a new row
        var row3 = tbody3.insertRow();

        // create the cells
        var cell13 = row3.insertCell();
        var cell23 = row3.insertCell();

        // add the data to the cells
        cell13.innerHTML = classifications[key];
        cell23.innerHTML = key;
    }
});
