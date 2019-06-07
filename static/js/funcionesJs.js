function ver_menu_items(id_menu)
{

	$.ajax({
	  type:"GET",
	  url: "http://127.0.0.1:8000/menu/modificar_menu/"+id_menu ,
	  data: { },

	  success: function(data)
	  {
	  	Swal.fire({	  	  
	  	  html: data,
	  	  focusConfirm: false,
	  	  showCancelButton: false,
  		showConfirmButton: false
	  	})

	  }
	  
	});
}

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