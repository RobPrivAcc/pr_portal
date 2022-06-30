//
$( "#book_in_search" )
.click(function () {
    let shop = $("#shop option:selected").value();
    let month = $("#months option:selected").value();
    let year = $("#years option:selected").value();

  var brandName = $("#brandName option:selected").text();
  //var storeOrAway = $("[name='shopNo']:checked").val();
    if (brandName != 'Choose Brand'){
        var spinner = '<Div Class="text-center"><i Class="fa fa-cog fa-spin fa-3x fa-fw"></i><span Class="sr-only">Loading...</span></DIV>';
        $('#result').html(spinner);

      $.post( "sql/sqlProductsPerBrand.php", { brandName: brandName })
          .done(function( data ) {
              $('#result').html(data);
          });
    }
})
.change();