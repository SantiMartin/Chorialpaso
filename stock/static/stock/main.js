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
			data: {'id_categoria':id},
			success: function(data){
				$('#mostrar_producto').html(data);
			},
			error:function( jqXhr, textStatus, errorThrown ){
        console.log( errorThrown );
    }
		});
}

function busqueda_ajax(codigo) {
		$.ajax({
			type: "POST",
			url: "http://127.0.0.1:8000/stock/busqueda_producto",
			data: {'codigo':codigo,'descripcion_categoria': $('.activo').text()},
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

	$.ajax({
		type: "POST",
		url: "http://127.0.0.1:8000/stock/modificar_producto",
		data: {'codigo': codigo, 'nombre': formValues[0],'precio_costo': formValues[1],'precio_venta': formValues[2]},
		success: function(data){
			//Swal.fire(JSON.stringify(formValues));
			window.location = data;
		},
		error:function( jqXhr, textStatus, errorThrown ){
       		console.log( errorThrown );
    	}
	});
  		//Swal.fire(JSON.stringify(formValues))//aca va una funcion de confirmar que muestre la nueva info.
}
















// Solucion al error del missing token CSRF
$(function(){
    //Obtenemos la información de csfrtoken que se almacena por cookies en el cliente
    var csrftoken = getCookie('csrftoken');

    //Agregamos en la configuración de la funcion $.ajax de Jquery lo siguiente:
    $.ajaxSetup({
                    beforeSend: function(xhr, settings) {
                        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                            // Send the token to same-origin, relative URLs only.
                            // Send the token only if the method warrants CSRF protection
                            // Using the CSRFToken value acquired earlier
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        }
                    }
    });

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

// usando jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


    function csrfSafeMethod(method) {
        // estos métodos no requieren CSRF
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
});



