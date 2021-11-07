$(document).ready(function(){

    var a =getElementByTagName("a");
   var  href=a.href;
    a.on('click',function(){
        $(location).attr('href',href);
    });
});