$(document).ready(function(){
	$(window).scroll(function(){
        if ($(window).scrollTop() >= $('#header').height()) {
            $('#menu-container').addClass('fixed-menu');
            $('#content').addClass('fix-body-onscroll');
        }
        else {
            $('#menu-container').removeClass('fixed-menu');
            $('#content').removeClass('fix-body-onscroll');
        }
    });

	// $("#form-edit-mode").submit(function(e){
    //     e.preventDefault();
    // });
});