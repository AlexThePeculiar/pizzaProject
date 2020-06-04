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

	$("#form-checkout").submit(function(e){
        if(parseFloat($('#total').text()) < 12.00){
                alert('Минимальная сумма заказа - 12.00 рублей')
                e.preventDefault();
        }
    });
});