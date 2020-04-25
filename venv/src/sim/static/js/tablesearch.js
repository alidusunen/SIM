$(document).ready(function() {

    // Setup - add a text input to each footer cell
    $('#mainTable thead tr').clone(true).appendTo( '#mainTable thead' );
    $('#mainTable thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text" class="form-control form-control-sm table-search" placeholder="" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );

    var table = $('#mainTable').DataTable( {
        orderCellsTop: true,
        fixedHeader: true,
        "pageLength": 50,
        "ordering": false,
        "lengthMenu": [ [10, 25, 50, 75, 100, -1], [10, 25, 50, 75, 100, "All"] ],
        'dom': 'BRflrtip',
        colReorder: true,

        buttons: [
            {
                extend: 'excel',
                text: 'Export View to Excel'
            }
        ],

    } );
//           ### Hide Columns via Checkboxes
//           ### Group Hide
            $('#sect1').change(function() {table.columns([7,8,9,10,11]).visible(!$(this).is(':checked'))});
            $('#sect2').change(function() {table.columns([12,13,14,15,16,17]).visible(!$(this).is(':checked'))});
            $('#sect3').change(function() {table.columns([1,2,5,12,13,14,15,16,17]).visible(!$(this).is(':checked'))});
//           ### Column Hide
//           ### Asset Properties
            $('#col1').change(function() {table.columns(1).visible(!$(this).is(':checked'))});
            $('#col2').change(function() {table.columns(2).visible(!$(this).is(':checked'))});
            $('#col3').change(function() {table.columns(3).visible(!$(this).is(':checked'))});
            $('#col5').change(function() {table.columns(5).visible(!$(this).is(':checked'))});
            $('#col6').change(function() {table.columns(6).visible(!$(this).is(':checked'))});
//           ### Usage Properties
            $('#col7').change(function() {table.columns(7).visible(!$(this).is(':checked'))});
            $('#col8').change(function() {table.columns(8).visible(!$(this).is(':checked'))});
            $('#col9').change(function() {table.columns(9).visible(!$(this).is(':checked'))});
            $('#col10').change(function() {table.columns(10).visible(!$(this).is(':checked'))});
            $('#col11').change(function() {table.columns(11).visible(!$(this).is(':checked'))});
//           ### Procurement Information
            $('#col12').change(function() {table.columns(12).visible(!$(this).is(':checked'))});
            $('#col13').change(function() {table.columns(13).visible(!$(this).is(':checked'))});
            $('#col14').change(function() {table.columns(14).visible(!$(this).is(':checked'))});
            $('#col15').change(function() {table.columns(15).visible(!$(this).is(':checked'))});
            $('#col16').change(function() {table.columns(16).visible(!$(this).is(':checked'))});
            $('#col17').change(function() {table.columns(17).visible(!$(this).is(':checked'))});
            $('#col18').change(function() {table.columns(18).visible(!$(this).is(':checked'))});

// working code for button click columm removal
//    document.getElementById("tester").onclick = function () { table.column( 0 ).visible( false ); };



} );



