$window = $(window);
$(window).scroll(function(){

if($window.scrollTop() > 300)
    $("#header").addClass('active');
else    
    $("#header").removeClass('active');
});