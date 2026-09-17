// saveData.js
// Sends the experiment's data to be saved, and returns a Promise that resolves
// once the save has finished (so the experiment can then show a confirmation).
//
// Two situations are handled automatically:
//   1. The page is opened through a server (e.g. the Python server in this
//      tutorial, or GitHub Pages). The data is POSTed to the server, which
//      writes it to a file in the ./data/ folder.
//   2. The page was opened by double-clicking the .html file (the address bar
//      starts with "file://"). There is no server to receive the data, so we
//      fall back to a normal browser download instead.

function saveData(filename, data) {
  if (location.protocol === "file:") {
    // No server available — just download the file in the browser.
    downloadCSV(filename + ".csv", data);
    return Promise.resolve();
  }
  // Running on a server: POST the data to the /save endpoint.
  return fetch("save", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ filename: filename, data: data })
  }).then(function (response) {
    if (!response.ok) {
      console.error("Save request failed (status " + response.status + "). Downloading instead.");
      downloadCSV(filename + ".csv", data);
    }
  }).catch(function (err) {
    console.error("Could not reach the save server. Downloading instead.", err);
    downloadCSV(filename + ".csv", data);
  });
}

function downloadCSV(name, text) {
  var blob = new Blob([text], { type: "text/csv" });
  var url = URL.createObjectURL(blob);
  var a = document.createElement("a");
  a.href = url;
  a.download = name;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
