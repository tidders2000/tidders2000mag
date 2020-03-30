jQuery(document).ready(function($) {
		const form_text = ()=>{
        const html=`<div class='slug_text'>Enter in search words seperated by '-' for example pipework-drains-kitchens (max 50 char)</div>`;
        document.querySelector('#div_id_slug').insertAdjacentHTML('beforebegin', html);
	
        };

   
		
	  $('#back').tooltip()

	  $('.toast').toast()
	  $('document').toast('show')
	  
	  $('#fade').hide()
	  
	  $('#alert').mouseover(function(){
	  	 $('#fade').show()
	  })

	  /*hide alert box */
	  $('#fade').click(function() {
	    $('#alert').hide();;
	  });


	 

form_text();

});
	