$(document).ready(function(){
	$("header ul li:nth-child(2)").addClass("activo");
	$("header ul li:nth-child(2) > a").addClass("letra");
});

$(function() {
   $("li").click(function() {
      // remove classes from all
      $("li").removeClass("activo");
      $("li a").removeClass("letra");
      // add class to the one we clicked
      $(this).addClass("activo");
      $(this).find('a').addClass("letra");
      $(".cabecera").text($(this).text());
   });
});

/*
$menues.click(function(){
     // eliminamos activo de todos los elementos
     //menues.removeClass("activo");
     //anchor.removeClass("letra");
     // activamos el elemento clicado.
     $(this).addClass("activo");
     //$(this a).addClass("letra");
  
});*/
async function openModal(valor_nombre, valor_costo, valor_venta) {
		
	const {value: formValues} = await Swal.fire({
	  title: 'Edicion de artículo',
	  html:
	    '<input id="nombre" class="swal2-input" value="'+valor_nombre+'">'+'<label>Nombre articulo</label>'+'<input id="costo" class="swal2-input"value="'+valor_costo+'">'+'<label>Costo</label>'+'<input id="pcioVta" class="swal2-input"value="'+valor_venta+'">'+'<label>Precio de venta</label>',
	  focusConfirm: false,
	  preConfirm: () => {
	    return [
	      document.getElementById('nombre').value,
	      document.getElementById('costo').value,
	      document.getElementById('pcioVta').value
	    ]
	  }
	})

	if (formValues) {
  		Swal.fire(JSON.stringify(formValues))//aca va una funcion de confirmar que muestre la nueva info.
	}

	
}	



