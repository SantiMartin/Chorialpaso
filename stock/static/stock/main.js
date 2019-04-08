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


function filtrar_categoria(id) {
		$.ajax({
			type: "POST",
			url: "http://127.0.0.1:8000/stock/filtrar_categoria",
			data: {'csrfmiddlewaretoken':'{{csrf_token}}','id_categoria':id},
			success: function(data){
				$('#mostrar_producto').html(data);
			},
			error:function( jqXhr, textStatus, errorThrown ){
        console.log( errorThrown );
    }
		});
}
/*
$menues.click(function(){
     // eliminamos activo de todos los elementos
     //menues.removeClass("activo");
     //anchor.removeClass("letra");
     // activamos el elemento clicado.
     $(this).addClass("activo");
     //$(this a).addClass("letra");
  
});*/
async function openModal(codigo, valor_nombre, valor_costo, valor_venta) {
	
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
		$.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/stock/modificar_producto",
			data: {'codigo': codigo, 'nombre': formValues[0],'precio_costo': formValues[1],'precio_venta': formValues[2]},
			success: function(data){
				Swal.fire(JSON.stringify(formValues));
			},
			error:function( jqXhr, textStatus, errorThrown ){
       			console.log( errorThrown );
    		}
		});
  		//Swal.fire(JSON.stringify(formValues))//aca va una funcion de confirmar que muestre la nueva info.
	}

	
}	



