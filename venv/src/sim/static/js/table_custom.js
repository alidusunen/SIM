// Full search function for right aligned bar
function fullSearchFunction() {

  // Declare variables
  var input = document.getElementById("mainSearch");
  var filter = input.value.toUpperCase();
  var table = document.getElementById("mainTable");
  var trs = table.tBodies[0].getElementsByTagName("tr");

  // Loop through first tbody's rows
  for (var i = 0; i < trs.length; i++) {
    // define the row's cells
    var tds = trs[i].getElementsByTagName("td");
    // hide the row
    trs[i].style.display = "none";
    // loop through row cells
    for (var i2 = 0; i2 < tds.length; i2++) {
      // if there's a match
      if (tds[i2].innerHTML.toUpperCase().indexOf(filter) > -1) {
        // show the row
        trs[i].style.display = "";
        // skip to the next row
        continue;
      }
    }
  }
}

//Column Search Function WORKING
//Search0
function subSearchFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("subSearch");
  filter = input.value.toUpperCase();
  table = document.getElementById("mainTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
//
////search01
function subSearchFunction1() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("subSearch1");
  filter = input.value.toUpperCase();
  table = document.getElementById("mainTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

//search02
function subSearchFunction2() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("subSearch2");
  filter = input.value.toUpperCase();
  table = document.getElementById("mainTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[2];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

//search03
function subSearchFunction3() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("subSearch3");
  filter = input.value.toUpperCase();
  table = document.getElementById("mainTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[3];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}


