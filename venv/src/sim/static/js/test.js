
//function subSearchFunction() {
//
//    //Declare needed variables
//    var input, input1, input2, filter,filter1, filter2, table, tr, td0, td1, td2, i;
//
//    //Set inputs by getElementById
//    input = document.getElementById('subSearch');
//    input1 = document.getElementById('subSearch1');
//    input2 = document.getElementById('subSearch2');
//
//    //Set filters
//    filter = input.value.toUpperCase();
//    filter1 = input1.value.toUpperCase();
//    filter2 = input2.value.toUpperCase();
//    //Set the table and tr variables
//    table = document.getElementById("mainTable");
//    tr = document.getElementsByTagName("tr");
//
//    //Loop through items and hide those that don't match the query -->
//    for (i = 0; i < tr.length; i++) {
//
//        //Name is at index 0
//        td0 = tr[i].getElementsByTagName("td")[0];
//        td1 = tr[i].getElementsByTagName("td")[1];
//        td2 = tr[i].getElementsByTagName("td")[2];
//
//        if (td0.innerHTML.toUpperCase().indexOf(filter) > -1 && td1.innerHTML.toUpperCase().indexOf(filter1) > -1 && td2.innerHTML.toUpperCase().indexOf(filter2) > -1) {
//            tr[i].style.display = "";
//        }
//        else {
//            tr[i].style.display = "none";
//        }
//    }
//}
//
//}